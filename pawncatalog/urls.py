from django.urls import path
from . import views

# Two different approaches for getting views:
urlpatterns = [

    # 1. From a function
    path('', views.index, name='index'),

    # 2. Class-based
    path('customers/', views.ActiveCustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerDetailsView.as_view(), {'test_context_value': 'hello :)'}, name='customer-detail'),
    path('customer/<int:pk>/change_name', views.change_customer_name, name='customer_change_name'),
    path('items/', views.ItemsListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailsView.as_view(), name='item-detail'),
    path('transactions/my_authorized', views.TransactionsAuthorizedByUser.as_view(), name='transactions_authorized_by_user'),
    path('transactions/<uuid:pk>/change_date', views.change_transaction_date, name='transaction_change_date'),

]