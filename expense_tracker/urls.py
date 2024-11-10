from django.contrib import admin
from django.urls import path
from expense import views  # Import views from the expense app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('expense_list/', views.expense_list, name='expense_list'),  # List expenses with pagination and filters
    path('expense/create/', views.create_expense, name='create_expense'),  # Create new expense
    path('expense/<int:pk>/update/', views.update_expense, name='update_expense'),  # Update existing expense
    
    path('expense/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
]
