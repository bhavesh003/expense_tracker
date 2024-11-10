from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.core.paginator import Paginator
from django.db.models import Sum
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense/create_expense.html', {'form': form})

def expense_list(request):
    # Initial query for all expenses
    expenses = Expense.objects.all()

    # Handling sorting logic
    sort_by = request.GET.get('sort_by', 'date')  # Default sort by date
    sort_order = request.GET.get('sort_order', 'asc')  # Default sort order is ascending

    # Apply sorting based on the chosen column and order
    if sort_order == 'asc':
        expenses = expenses.order_by(sort_by)  # Ascending order
    elif sort_order == 'desc':
        expenses = expenses.order_by(f'-{sort_by}')  # Descending order

    # Filter by category if selected
    category_filter = request.GET.get('category', '')
    if category_filter:
        expenses = expenses.filter(category=category_filter)

    # Filter by title (search term)
    search_term = request.GET.get('search', '')
    if search_term:
        expenses = expenses.filter(title__icontains=search_term)

    # Filter by date range
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    if start_date and end_date:
        expenses = expenses.filter(date__range=[start_date, end_date])

    # Calculate the total expense before pagination
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    # Pagination: 15 expenses per page
    paginator = Paginator(expenses, 15)
    page = request.GET.get('page')
    expenses = paginator.get_page(page)

    # If 'clear_filters' is in the GET parameters, reset the filters
    if 'clear_filters' in request.GET:
        return redirect('expense_list')

    return render(request, 'expense/expense_list.html', {
        'expenses': expenses,
        'total_expense': total_expense,
        'paginator': paginator,
        'category_filter': category_filter,
        'search_term': search_term,
        'start_date': start_date,
        'end_date': end_date,
        'sort_by': sort_by,
        'sort_order': sort_order
    })

def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense) 
        if form.is_valid():
            form.save()
            return redirect('expense_list') 
    else:
        form = ExpenseForm(instance=expense) 

    return render(request, 'expense/update_expense.html', {'form': form, 'expense': expense})

def delete_expense(request, pk):

    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list') 
    
    return render(request, 'expense/delete_expense.html', {'expense': expense})
