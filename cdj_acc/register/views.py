# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('register/index.html')
    return HttpResponse(template.render({}, request))


def register_client(request):
    return HttpResponse('<h1>Hello This is for Client Registration</h1>')


def register_user(request):
    return HttpResponse('<h1>Hello This is for USER registration</h1>')