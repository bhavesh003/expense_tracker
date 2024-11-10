# Expense Tracker Django Application

## Description

The **Expense Tracker** is a web application built using Django that allows users to track their daily, weekly, or monthly expenses. It provides functionality for adding, editing, and deleting expenses, filtering and sorting them by category, date, and amount, and viewing a summary of total expenses.

The app helps users stay on top of their finances by organizing expenses, providing a simple user interface to interact with and manage financial data.

## Features

- **Create Expense**: Users can add new expenses with a title, amount, category, date, and description.
- **Edit Expense**: Users can update their existing expenses.
- **Delete Expense**: Users can delete expenses that are no longer needed.
- **Expense List**: A dynamic list of all expenses with pagination.
- **Filters**: Filter expenses by category, title, and date range.
- **Sorting**: Sort expenses by title, amount, category, date, and description in both ascending and descending order.
- **Total Expense Calculation**: Displays the total sum of all expenses.
- **Responsive UI**: Mobile-friendly and clean user interface built with Bootstrap.
- **Customizable Categories**: Expenses can be assigned to different categories like Food, Transport, Entertainment, and Other.


### Functionality

1. **Home Page**:
   - Displays a welcoming message and a link to the expense list page.

2. **Expense List**:
   - Displays all the recorded expenses.
   - Filters and sorts expenses based on user input.
   - Shows the total amount of all expenses.
   - Includes pagination for easy navigation through large lists of expenses.

3. **Expense Creation**:
   - Users can input the details of a new expense including title, amount, category, date, and description.
   - Data is saved to the database once validated.

4. **Expense Update**:
   - Existing expenses can be updated with new details.
   - The current details of the expense are pre-filled in the form, making it easy for the user to edit.

5. **Expense Deletion**:
   - Users can delete any expense they no longer need.
   - A confirmation page ensures that no expenses are deleted unintentionally.

## Key Concepts in Django Development

This project demonstrates the following key concepts of Django development:

- **Model-View-Template (MVT) architecture**: 
  - **Model**: The `Expense` model defines the structure of the data.
  - **View**: Views handle the business logic (e.g., rendering templates, handling forms, querying the database).
  - **Template**: The HTML templates define the UI and present data to the user.
  
- **URL Routing**: URL patterns in `urls.py` map to views, ensuring the correct page is shown based on the user's request.
  
- **Forms**: The `ExpenseForm` is used to handle form submissions for creating and updating expenses.
  
- **Querysets**: Used to filter, sort, and paginate expenses from the database.
  
- **Django Admin (Optional)**: Can be enabled to manage the expenses directly through the Django admin interface.

## Implementation of Requirements

1. **Expense Creation**: 
   - Implemented in the `create_expense` view, where a form is rendered and processed to save expense data to the database.
  
2. **Expense Update**:
   - The `update_expense` view retrieves the expense, pre-fills the form with its existing data, and saves any changes made by the user.
  
3. **Expense Deletion**:
   - The `delete_expense` view handles the deletion process with a confirmation page to prevent accidental deletions.

4. **Filtering and Sorting**:
   - The `expense_list` view implements filtering by category, title, and date range using GET parameters.
   - Sorting is done by handling the `sort_by` and `sort_order` parameters and adjusting the queryset accordingly.

5. **Pagination**:
   - The `Paginator` class is used to break the expense list into manageable pages, improving user experience when dealing with large data sets.

6. **Total Expense Calculation**:
   - A sum of all expenses is calculated using Django's `aggregate` function and displayed at the top of the expense list.

## Additional Features or Creative Elements

- **Responsive Design**: The application uses Bootstrap for a responsive, mobile-friendly design. This ensures the app works well on devices of all sizes.
- **Expense Categories**: Expenses can be categorized into predefined categories such as Food, Transport, Entertainment, and Other. This allows users to better organize and track their spending.
- **Sorting Icons**: For better UX, sorting indicators (↑ and ↓) are displayed next to each sortable column to show the current sorting order.
- **Clear Filters Button**: A button to clear all active filters and reset the view.
