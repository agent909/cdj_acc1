from django.shortcuts import render
# Create your views here.

def transact(request):
    return render(request, 'entry/transact.html')


