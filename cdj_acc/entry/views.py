from django.shortcuts import render
# Create your views here.

def transact(request):
    return render(request, 'transact.html')


    