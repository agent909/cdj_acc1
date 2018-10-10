from django.conf.urls import url
from django.urls import path
from . import views

app_name = "entry"

urlpatterns = [
    path('<int:account_id>', views.transact, name='transaction'),
    path('', views.transact, name='transaction'),
    path('account_receivable/', views.add_account_receivable, name='add_account_receivable'),
    path('sales/', views.add_sales, name='add_sales'),
    path('payment_to_account_receivable/', views.add_payment_to_account_receivable, name='add_payment_to_account_receivable'),
]