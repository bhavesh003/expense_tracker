from django.contrib import admin
from django.urls import path
from expense import views  

urlpatterns = [
    path('', views.home, name='home'),  
    path('expense_list/', views.expense_list, name='expense_list'),  
    path('expense/create/', views.create_expense, name='create_expense'),  
    path('expense/<int:pk>/update/', views.update_expense, name='update_expense'),  
    path('expense/<int:pk>/delete/', views.delete_expense, name='delete_expense'),
]
