from django.conf.urls import url
from django.urls import path
from . import views

app_name = "entry"

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^client$', views.register_client, name='register client'),
    # url(r'^registerUser$', views.register_user, name='register_user')
    path('', views.transact, name='transaction'),
    path('account_receivable/', views.add_account_receivable, name='add_account_receivable'),
    path('sales/', views.add_sales, name='add_sales'),
]