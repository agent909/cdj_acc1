from django.conf.urls import url
from django.urls import path
from . import views

app_name = "entry"

urlpatterns = [
    path('<slug:acc_name>/debtor=<slug:debtor_name>', views.get_debtors),
    path('<slug:acc_name>/', views.transact, name='transaction'),
    # path('<int:account_id>', views.transact, name='transaction'),
    path('', views.transact, name='transaction'),
    path('forms/account_receivable/', views.add_account_receivable, name='add_account_receivable'),
    path('forms/sales/', views.add_sales, name='add_sales'),
    path('forms/payment_to_account_receivable/', views.add_payment_to_account_receivable, name='add_payment_to_account_receivable'),
]