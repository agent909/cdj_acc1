from django.conf.urls import url
from django.urls import path
from . import views

app_name = "entry"

urlpatterns = [
    path('<slug:acc_name>/borrower=<slug:borrower>', views.get_borrower),
    path('<slug:acc_name>/debtor=<slug:debtor_name>', views.get_debtors),
    path('<slug:acc_name>/', views.transact, name='transaction'),
    path('forms/account_receivable/', views.add_account_receivable, name='add_account_receivable'),
    path('forms/sales/', views.add_sales, name='add_sales'),
    path('forms/payment_to_account_receivable/', views.add_payment_to_account_receivable, name='add_payment_to_account_receivable'),
    path('forms/loans_receivable/', views.add_loans_receivable, name='add_loans_receivable'),
    path('forms/loan_payment/borrower=<slug:borrower>', views.add_loan_payment, name='add_loan_payment'),
    path('forms/loan_payment/borrower=', views.get_404_1),
]