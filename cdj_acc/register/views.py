# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def index(request):
    template = loader.get_template('register/index.html')
    return HttpResponse(template.render({}, request))


def register_client(request):
    return HttpResponse('<h1>Hello This is for Client Registration</h1>')


def register_user(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)

        if(form.is_valid()):
            print("Valid")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            print("failed post")
            return redirect('index')
    else:
        form  = UserCreationForm()

    # template = loader.get_template('register/register_user.html')
    context = {"form": form}
    return render(request, 'registration/register_user.html', context)