from django.shortcuts import render, get_object_or_404, get_list_or_404
from entry.models import *
from register.models import Client
from datetime import datetime

from .forms import AccountReceivableForm


def transact(request):
    accounts = get_list_or_404(Accounts)
    myform = AccountReceivableForm(auto_id=False)

    message = 'initial message'

    if request.method == 'POST':
        message = "POSTED REQUEST"
        form = AccountReceivableForm(request.POST)

        if form.is_valid():
            print("FORM is VALIDATED")
            message = "VALID"

            print(request.POST['account_selector'])

            A_receivable = form.cleaned_data
            date = A_receivable.get("date")
            documentNumber = A_receivable.get("documentNumber")
            buyer = A_receivable.get("buyer")
            amount = A_receivable.get("amount")

            # GET id of selected CLIENT
            client = Client.objects.get(pk=1)

            # GET the name of the Account used
            account_name = Accounts.objects.get(name=request.POST['account_selector'])

            # CREATE TRANSACTION
            transaction = Transactions(
                client=client, 
                nameOfTransaction=account_name, 
                date_entry=datetime.today()
                )

            transaction.save()
            
            AR = AccountReceivable(
                client=client,
                date=date,
                documentNumber=documentNumber,
                buyer=buyer,
                cash=amount,
                transaction_id=transaction,
            )

            AR.save()

            Sale = Sales(
                client=client,
                date=date,
                documentNumber=documentNumber,
                buyer=buyer,
                amount=amount,
                transaction_id=transaction
            )

            Sale.save()

            print("SUCCESSfully posted to database")
            message = "SUCCESSfully posted to database"

        else:
            message = "INVALID form"

    context = {
        'accounts':accounts, 'form':myform, 'message':message,
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
