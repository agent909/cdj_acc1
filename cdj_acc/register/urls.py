from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^client$', views.register_client, name='client register'),
    url(r'^user$',views.register_user, name='add user')
]