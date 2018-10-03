from django.shortcuts import render, get_object_or_404, get_list_or_404
from register.models import Client


def select_client(request):
    clients = get_list_or_404(Client)
    context = {
        'clients':clients,
        }
    return render(request, 'client/select_client.html', context)