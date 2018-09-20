from django.shortcuts import render, get_object_or_404, get_list_or_404
from entry.models import *
from register.models import Client
# Create your views here.

def transact(request):
    accounts = get_list_or_404(Accounts)
    context = {'accounts':accounts}
    return render(request, 'entry/transact.html', context)

