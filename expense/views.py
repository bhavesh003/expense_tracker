from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.core.paginator import Paginator
from django.db.models import Sum
from datetime import datetime

# Home page view
def home(request):
    return render(request, 'home.html')

# Create expense
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense/create_expense.html', {'form': form})

# List expenses with pagination, filtering, and total expense calculation
def expense_list(request):
    # Initial query for all expenses
    expenses = Expense.objects.all()

    # Filter by category
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

    # Calculate the total expense BEFORE pagination
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
    })

# Update expense
def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)  # Populates the form with existing data
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect to the list view after saving
    else:
        form = ExpenseForm(instance=expense)  # Pre-fill the form with the current expense details

    return render(request, 'expense/update_expense.html', {'form': form, 'expense': expense})

# Delete expense
def delete_expense(request, pk):
    # Retrieve the expense by pk
    expense = get_object_or_404(Expense, pk=pk)

    # If the request method is POST, delete the expense
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')  # Redirect back to the expense list page

    # Render the confirmation page (this will display the confirmation message)
    return render(request, 'expense/delete_expense.html', {'expense': expense})
