from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from entry.models import *
from register.models import Client
from datetime import datetime
from django.utils import timezone
from timeit import default_timer
from itertools import chain

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

# GENERATE EACH BUYER'S TRANSACTIONS
def generate_Btransactions(receivables):
    buyers = receivables.values('buyer').distinct()
    buyer_t=[]
    buyer_transactions=[]

    for buyer in buyers:
        # get list of payment of specific debtor
        buyer_payables = receivables.filter(buyer=buyer.get('buyer'))
        # get list of receivable of specific buyer
        buyer_payments = PaymentToAccountReceivable.objects.filter(
            receivable__client_id=1, receivable__buyer=buyer.get('buyer'))
        buyer_t += [sorted(chain(buyer_payables, buyer_payments), key=lambda instance: instance.date)]

    for t in buyer_t:
        balance=0
        temp=[]
        for transact in t:
            if(transact.__class__.__name__=='AccountReceivable'):
                balance+=transact.cash
                temp+=[[transact.date, transact.cash,' ', balance]]
            else:
                balance-=transact.cash
                temp+=[[transact.date, ' ', transact.cash, balance]]
        buyer_transactions+=[temp]

    return buyer_transactions
    
#--------------------------------------------------------------------------------------

def transact(request, account_id):
    start = default_timer()
    accounts = get_list_or_404(Accounts)

    #get all receivables of current client
    my_client = Client.objects.get(pk=1)
    receivables = AccountReceivable.objects.filter(client=my_client.id)
    list_test= [1,2]
    # #get all payment
    # PaymentToAccountReceivable.objects.filter(receivable__client_id=1, receivable_id=ARobject.id)

    context = {
        'mlist':list_test,
        'accounts':accounts,
        'template_filenames':generate_filename(accounts),
        'receivables':receivables,
        'my_client':my_client,
        'accountId':account_id,
        'buyer_transactions':generate_Btransactions(receivables),
    }
        
    context = append_forms_to_context(context)
    print(default_timer()-start)
    return render(request, 'entry/transact.html', context)


def add_account_receivable(request):
    start = default_timer()
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
                transaction=transaction,
            )

            AR.save()

            Sale = Sales(
                client=client,
                date=date,
                documentNumber=documentNumber,
                buyer=buyer,
                amount=amount,
                transaction=transaction
            )
            Sale.save()
            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
        else:
            messages.warning(request, "INVALID FORM")
    print(default_timer()-start)
    # return render(request, 'entry/transact.html', context)
    return redirect('/entry/1')


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
                transaction=transaction
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
            # try:
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
                transaction=transaction
            )

            cash_entry.save()

            payment_to_AR = PaymentToAccountReceivable(
                receivable=receivable,
                date=date,
                cash=cash_entry.amount,
                transaction=transaction,
            )

            payment_to_AR.save()

            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
            # except:
            #     transaction.delete()
            #     print("ERROR WHILE POSTING TO DATABASE")
            #     messages.success(request, "ERROR WHILE POSTING TO DATABASE")
        else:
            messages.warning(request, "INVALID FORM")

    return redirect('/entry/')