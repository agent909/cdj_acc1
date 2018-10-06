from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from entry.models import *
from register.models import Client
from datetime import datetime
from django.utils import timezone

from .forms import AccountReceivableForm, PaymentToAccountReceivableForm

#--------------------------------------------------------------------------------------
# HELPER FUNCTIONS

# ADD ALL THE DJANGO FORMS HERE
def append_forms_to_context(context):
    forms = {
        'account_receivable': AccountReceivableForm(auto_id=False),
        'sales': AccountReceivableForm(auto_id=False),
        'add_payment_to_account_receivable': PaymentToAccountReceivableForm(auto_id=False),
    }
    return {**context, **forms}


# GENERATE TEMPLATE FILENAME FROM ACCOUNT NAMES
def generate_filename(list_of_names):
    file_names =[]
    for account in list_of_names:
        file_names+=[account.name.lower().replace(" ","_")+".html"]

    return file_names
#--------------------------------------------------------------------------------------

def transact(request):
    accounts = get_list_or_404(Accounts)
    receivables = AccountReceivable.objects.all()

    context = {
        'accounts':accounts,
        'template_filenames':generate_filename(accounts),
        'receivables':receivables,
    }
        
    context = append_forms_to_context(context)
    return render(request, 'entry/transact.html', context)


def add_account_receivable(request):

    if request.method == 'POST':
        form = AccountReceivableForm(request.POST)

        if form.is_valid():
            print("FORM is VALIDATED")
            # print(request.POST['account_selector'])

            A_receivable = form.cleaned_data
            date = A_receivable.get("date")
            documentNumber = A_receivable.get("documentNumber")
            buyer = A_receivable.get("buyer")
            amount = A_receivable.get("amount")

            # GET id of selected CLIENT
            client = Client.objects.get(pk=1)

            # GET the name of the Account used
            account_name = Accounts.objects.get(name=form.__str__())

            # CREATE TRANSACTION
            transaction = Transactions(
                client=client, 
                nameOfTransaction=account_name, 
                date_entry=timezone.now()
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
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
        else:
            messages.warning(request, "INVALID FORM")

    # return render(request, 'entry/transact.html', context)
    return redirect('/entry/')


def add_sales(request):

    if request.method == 'POST':
        form = AccountReceivableForm(request.POST)

        if form.is_valid():
            print("FORM is VALIDATED")
            # print(request.POST['account_selector'])

            A_receivable = form.cleaned_data
            date = A_receivable.get("date")
            documentNumber = A_receivable.get("documentNumber")
            buyer = A_receivable.get("buyer")
            amount = A_receivable.get("amount")

            # GET id of selected CLIENT
            client = Client.objects.get(pk=1)

            # GET the name of the Account used
            account_name = Accounts.objects.get(name=form.__str__())

            # CREATE TRANSACTION
            transaction = Transactions(
                client=client, 
                nameOfTransaction=account_name, 
                date_entry=timezone.now()
                )

            transaction.save()

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
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
        else:
            messages.warning(request, "INVALID FORM")

    return redirect('/entry/')


def add_payment_to_account_receivable(request):

    if request.method == 'POST':
        form = PaymentToAccountReceivableForm(request.POST)

        if form.is_valid():
            print("FORM IS VALIDATED")

            payment_A_receivable = form.cleaned_data
            date = payment_A_receivable.get("date")
            debtor = payment_A_receivable.get("debtor")
            cash = payment_A_receivable.get("cash")

            try:
                receivable = AccountReceivable.objects.get(buyer=debtor)
            except AccountReceivable.DoesNotExist:
                messages.warning(request, "DEBTOR "+debtor+" DOES NOT EXIST")
                return redirect('/entry/')

            # GET id of selected CLIENT
            client = Client.objects.get(pk=1)

            # GET the name of the Account used
            account_name = Accounts.objects.get(name=form.__str__())

            # CREATE TRANSACTION
            transaction = Transactions(
                client=client, 
                nameOfTransaction=account_name, 
                date_entry=timezone.now()
                )

            transaction.save()

            cash_entry = CashOnHand(
                client=client,
                date=date,
                amount=cash,
                transaction_id=transaction
            )

            cash_entry.save()

            payment_to_AR = PaymentToAccountReceivable(
                client=client,
                receivable=receivable,
                date=date,
                debtor=debtor,
                cash=cash_entry,
                transaction_id=transaction,
            )

            payment_to_AR.save()

            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
        else:
            messages.warning(request, "INVALID FORM")

    return redirect('/entry/')