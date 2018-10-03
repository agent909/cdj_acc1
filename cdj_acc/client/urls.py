from django.conf.urls import url
from django.urls import path
from . import views

app_name = "client"

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^client$', views.register_client, name='register client'),
    # url(r'^registerUser$', views.register_user, name='register_user')
    path('select_client/', views.select_client, name='select_client'),
]