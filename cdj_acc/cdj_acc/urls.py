from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('register.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('book/', include('book.urls')),
    path('entry/', include('entry.urls')),
    path('client/', include('client.urls')),
]
