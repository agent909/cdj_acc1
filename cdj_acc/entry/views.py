from django.shortcuts import render, get_object_or_404, get_list_or_404
from entry.models import *
from register.models import Client
# Create your views here.

def transact(request):
    accounts = get_list_or_404(Accounts)
    try:
        printit=""
        # myarray = request.POST['items']
        # for x in myarray:
        #     printit+=x 
        context = {
            'accounts':accounts, 'myarray':request.POST['items[0]'],
        }

        print(request.POST['items'])

        return render(request, 'entry/transact.html', context)
    except:
        pass

    context = {
        'accounts':accounts,
    }

    return render(request, 'entry/transact.html', context)

        # # GET id of selected CLIENT
        # client = Client.objects.get(pk=1)

        # # GET the name of the Account used
        # account_name = Accounts.objects.get(name=request.POST['account_selector'])

        # # CREATE TRANSACTION
        # transaction = Transactions(client=client, nameOfTransaction=account_name, date_entry=timezone.localtime(timezone.now()))
        # transaction.save()

        # #GET TRANSACTION ID 
        # transaction_id = transaction.id

        # # GET DETAILS ON THE TEMPLATE FORM then create A/R
        # account_receivable_entry = AccountReceivable(
        #     client=client, 
        #     date=request.POST['date'], 
        #     documentNumber=request.POST['document_number'], 
        #     buyer=request.POST['debtor'],
        #     # cash=
        #     )

        # context = {
        #     'accounts':accounts,
        #     'message':'Successfully added entry',
        #   }
        # #   DO!  TRIGGER function ON template side to prompt success or failure of transaction.
        # return render(request, 'entry/transact.html', context)
