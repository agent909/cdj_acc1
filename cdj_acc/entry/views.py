from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from entry.models import *
from register.models import Client
from datetime import datetime, timedelta
from django.utils import timezone
from timeit import default_timer
from itertools import chain
from decimal import Decimal

from .forms import AccountReceivableForm, PaymentToAccountReceivableForm, LoansReceivableForm, LoanPaymentForm

#--------------------------------------------------------------------------------------
# HELPER FUNCTIONS

# ADD ALL THE DJANGO FORMS HERE
def append_forms_to_context(context):
    forms = {
        'account_receivable': AccountReceivableForm(auto_id=False),
        'sales': AccountReceivableForm(auto_id=False),
        'payment_to_account_receivable': PaymentToAccountReceivableForm(auto_id=False),
        'loans_receivable': LoansReceivableForm(auto_id=False),
        'loan_payment': LoanPaymentForm(auto_id=False),
    }
    return {**context, **forms}


# GENERATE TEMPLATE FILENAME FROM ACCOUNT NAMES
def generate_filename(list_of_names):
    file_names =[]
    for account in list_of_names:
        file_names+=[account.name.lower().replace(" ","_")+".html"]

    return file_names

# GENERATE DEBTOR TRANSACTIONS
def generate_Btransaction(receivables, buyer_name):
    buyer_payables = receivables.filter(buyer=buyer_name)
    buyer_payments = PaymentToAccountReceivable.objects.filter(
        receivable__client=receivables[0].client, receivable__buyer=buyer_name)
    transactions = sorted(chain(buyer_payables, buyer_payments), key=lambda instance: instance.date)
    transactions2 = []

    balance=0
    for item in transactions:
        temp=[]
        if(item.__class__.__name__=='AccountReceivable'):
            balance+=item.cash
            temp+=[item.date, item.documentNumber, item.cash,'', balance]
        else:
            balance-=item.cash
            temp+=[item.date, item.documentNumber,'', item.cash, balance]
        transactions2+=[temp]
    return transactions2


# GENERATE DEBTOR BALANCE
def get_receivables_balances(receivables):
    debtors = receivables.values('buyer').distinct()
    balances=[]
    for debtor in debtors:
        payables = AccountReceivable.objects.filter(buyer=debtor.get('buyer'))
        payments = PaymentToAccountReceivable.objects.filter(receivable__buyer=debtor.get('buyer'))
        
        debtor_balance=0
        for item in payables:
            debtor_balance+=item.cash
        for item in payments:
            debtor_balance-=item.cash
        balances+=[[debtor.get('buyer'),debtor_balance]]
    return balances

# GET BORROWERS OR LOANEES
def get_loan_borrowers():
    loans = LoansReceivable.objects.all().order_by('lastname').values('firstname','middlename','lastname','loanType').distinct()
    temp = []
    for x in loans:
        x=list(x.values())
        temp+=[[x[0],x[1],x[2],x[3]]]
    return temp


def get_loan_transactions(request, borrower):
    borrower = borrower.split('_')
    # try:
    lr = LoansReceivable.objects.filter(firstname=borrower[0], middlename=borrower[1], lastname=borrower[2], loanType=borrower[3])
    # except(IndexError):
        # messages.warning(request, "BORROWER "+debtor+" DOES NOT EXIST")
        # return redirect('/entry/loan_payment/')        

    lp = LoanPayment.objects.filter(loan=lr[0])

    transactions = sorted( chain(lr,lp), key=lambda instance:instance.date) 

    current_loan=""
    paymentTerms_days=0
    payment_mode=0
    balance=0
    regular_interest_payment=0
    lr_ledger=[]
    dueDate=0
    regular_payment=0
    daily_interest=0
    previous_paymentDate = ""

    for entry in transactions:        
        if(entry.__class__.__name__=='LoansReceivable'):
            current_loan = entry
            balance = entry.amountApplied
            previous_paymentDate = ""
            lr_ledger += [  [ entry.date, entry.amountApplied, 0, entry.amountApplied, 0, 0]  ]
            paymentTerms_days = (entry.termsOfPaymentYear*12*30)+(entry.termsOfPaymentMonth*30)+entry.termsOfPaymentDay
            if(entry.modeOfPayment=="monthly"):
                payment_mode=30
            elif(entry.modeOfPayment=="semi-monthly"):
                payment_mode=15
            elif(entry.modeOfPayment=="weekly"):
                payment_mode=7
            else:
                payment_mode=1

            dueDate = entry.date+timedelta(days=payment_mode)

            regular_payment = (entry.amountApplied/paymentTerms_days)*payment_mode
            regular_interest_payment = entry.amountApplied*(entry.interestRate/100)*Decimal(payment_mode/360)
            # regular_interest_payment =( (entry.amountApplied*(entry.interestRate/100))/paymentTerms_days )*payment_mode
            daily_interest = entry.amountApplied*(entry.interestRate/100)*Decimal(1/360)
        else:

            day_advance = (dueDate-entry.date).days
            if(day_advance<0):
                payment_lapsed = 1+int(day_advance/payment_mode)*-1
                
                penalty = (payment_lapsed*regular_payment*(current_loan.penaltyRate/100))
                interest = (-day_advance)*daily_interest+(regular_interest_payment*payment_lapsed)
            else:
                penalty = 0
                payment_lapsed = 0
                interest = (payment_mode-day_advance)*daily_interest+(regular_interest_payment*payment_lapsed)


            #Very advanced payment
            if(interest<0):
                interest = 0

            deduction_to_principal = entry.paymentAmount-interest-penalty-(regular_interest_payment*payment_lapsed)
            if(round(deduction_to_principal,2)==0):
                deduction_to_principal=0
            balance -= deduction_to_principal
            dueDate+=timedelta(days=payment_mode+payment_mode*payment_lapsed)

            lr_ledger += [  [entry.date, "", round(deduction_to_principal, 2), round(balance, 2), round(interest,2), round(penalty, 2)]  ]
            print(entry.date, "", round(deduction_to_principal, 2), round(balance, 2), round(interest,2), round(penalty, 2))
            print(dueDate)

    return lr_ledger
#--------------------------------------------------------------------------------------

def transact(request, acc_name):
    start = default_timer()
    accounts = get_list_or_404(Accounts)
    my_client = Client.objects.get(pk=1)
    receivables = AccountReceivable.objects.filter(client_id=my_client.id)

    context={
        'acc_name':acc_name,
        'accounts':accounts,
        'template_filenames':generate_filename(accounts),
        'buyer_transactions':[],
        'my_client':my_client,
        'debtor_balances':get_receivables_balances(receivables),
        'loans_list':get_loan_borrowers(),
    }

    context = append_forms_to_context(context)
    print(default_timer()-start)
    return render(request, 'entry/transact.html', context)


def get_borrower(request, acc_name, borrower):
    start = default_timer()
    accounts = get_list_or_404(Accounts)
    my_client = Client.objects.get(pk=1)
    borrower2 = borrower.split("_")
    lr = LoansReceivable.objects.filter(firstname=borrower2[0], middlename=borrower2[1], lastname=borrower2[2], loanType=borrower2[3]).order_by('date')

    context={
        'acc_name':acc_name,
        'accounts':accounts,
        'template_filenames':generate_filename(accounts),
        'loan_transactions':get_loan_transactions(request, borrower),
        'my_client':my_client,
        'loans_list':get_loan_borrowers(),
        'loan': lr[len(lr)-1],
        'borrower':borrower,
    }

    context = append_forms_to_context(context)
    print(default_timer()-start)
    return render(request, 'entry/transact.html', context)


def get_debtors(request, acc_name, debtor_name):
    start = default_timer()
    accounts = get_list_or_404(Accounts)
    my_client = Client.objects.get(pk=1)
    receivables = AccountReceivable.objects.filter(client_id=my_client.id)
    try:
        receivable = AccountReceivable.objects.filter(buyer=debtor_name.replace('_',' '))[0]
    except(AccountReceivable.DoesNotExist, IndexError) as error:
        messages.warning(request, "DEBTOR "+debtor+" DOES NOT EXIST")
        return redirect('/entry/payment_to_account_receivable/')

    context={
        'debtor_name':debtor_name,
        'acc_name':acc_name,
        'accounts':accounts,
        'template_filenames':generate_filename(accounts),
        'buyer_transactions':generate_Btransaction(receivables, debtor_name.replace("_"," ")),
        'my_client':my_client,
        'debtor_balances':get_receivables_balances(receivables),
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
            buyer = A_receivable.get("buyer").upper()
            cash = A_receivable.get("cash")

            # GET id of selected CLIENT
            client = Client.objects.get(pk=1)

            # GET the name of the Account used
            account_name = Accounts.objects.get(name=form.__str__())

            # CREATE TRANSACTION
            transaction = Transactions(
                client=client, 
                nameOfTransaction=account_name, 
                date_entry=timezone.now(),
                )

            transaction.save()
            
            AR = AccountReceivable(
                client=client,
                date=date,
                documentNumber=documentNumber,
                buyer=buyer,
                cash=cash,
                transaction=transaction,
            )

            AR.save()

            Sale = Sales(
                client=client,
                date=date,
                documentNumber=documentNumber,
                buyer=buyer,
                cash=cash,
                transaction=transaction
            )
            Sale.save()

            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
        else:
            messages.warning(request, "INVALID FORM")
    print(default_timer()-start)
    # return render(request, 'entry/transact.html', context)
    return redirect('/entry/account_receivable/')


def add_sales(request):

    if request.method == 'POST':
        form = AccountReceivableForm(request.POST)

        if form.is_valid():
            print("FORM is VALIDATED")
            # print(request.POST['account_selector'])

            A_receivable = form.cleaned_data
            date = A_receivable.get("date")
            documentNumber = A_receivable.get("documentNumber")
            buyer = A_receivable.get("buyer").upper()
            cash = A_receivable.get("cash")

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
                cash=cash,
                transaction=transaction
            )
            Sale.save()
            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
        else:
            messages.warning(request, "INVALID FORM")

    return redirect('/entry/sales/')


def add_payment_to_account_receivable(request):

    if request.method == 'POST':
        form = PaymentToAccountReceivableForm(request.POST)

        if form.is_valid():
            print("FORM IS VALIDATED")

            payment_A_receivable = form.cleaned_data
            date = payment_A_receivable.get("date")
            documentNumber = payment_A_receivable.get("documentNumber")
            debtor = payment_A_receivable.get("debtor").upper()
            cash = payment_A_receivable.get("cash")

            try:
                receivable = AccountReceivable.objects.filter(buyer=debtor)[0]
            except(AccountReceivable.DoesNotExist, IndexError) as error:
                messages.warning(request, "DEBTOR "+debtor+" DOES NOT EXIST")
                return redirect('/entry/payment_to_account_receivable/')

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
                cash=cash,
                transaction=transaction
            )

            cash_entry.save()

            payment_to_AR = PaymentToAccountReceivable(
                receivable=receivable,
                documentNumber=documentNumber,
                date=date,
                cash=cash_entry.cash,
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

    return redirect('/entry/payment_to_account_receivable/')


def add_loans_receivable(request):

    if request.method == 'POST':
        form = LoansReceivableForm(request.POST)

        if form.is_valid():
            print("FORM IS VALIDATED")

            loans_receivable = form.cleaned_data
            date = loans_receivable.get("date")
            documentNumber = loans_receivable.get("documentNumber")
            firstname = loans_receivable.get("firstname").upper()
            middlename = loans_receivable.get("middlename").upper()
            lastname = loans_receivable.get("lastname").upper()
            amountApplied = loans_receivable.get("amountApplied")
            loanType = loans_receivable.get("loanType")
            modeOfPayment = loans_receivable.get("modeOfPayment")
            termsOfPaymentYear = loans_receivable.get("termsOfPaymentYear")
            termsOfPaymentMonth = loans_receivable.get("termsOfPaymentMonth")
            termsOfPaymentDay = loans_receivable.get("termsOfPaymentDay")
            interestRate = loans_receivable.get("interestRate")
            methodOfInterest = loans_receivable.get("methodOfInterest")
            serviceFee = loans_receivable.get("serviceFee")
            penaltyRate = loans_receivable.get("penaltyRate")

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

            S_fee = ServiceFee(
                client=client,
                date=date,
                cash=amountApplied*(serviceFee/100),
                transaction=transaction
            )

            S_fee.save()

            cash_entry = CashOnHand(
                client=client,
                date=date,
                cash=(amountApplied-amountApplied*(serviceFee/100))*-1,
                transaction=transaction
            )

            cash_entry.save()

            loans_R = LoansReceivable(
                client=client,
                date=date,
                documentNumber=documentNumber,
                firstname=firstname,
                middlename=middlename,
                lastname=lastname,
                amountApplied=amountApplied,
                loanType=loanType,
                modeOfPayment=modeOfPayment,
                termsOfPaymentYear=termsOfPaymentYear,
                termsOfPaymentMonth=termsOfPaymentMonth,
                termsOfPaymentDay=termsOfPaymentDay,
                interestRate=interestRate,
                methodOfInterest=methodOfInterest,
                serviceFee=amountApplied*(serviceFee/100),
                penaltyRate=penaltyRate,
                transaction=transaction,
            )

            loans_R.save()

            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")
            # except:
            #     transaction.delete()
            #     print("ERROR WHILE POSTING TO DATABASE")
            #     messages.success(request, "ERROR WHILE POSTING TO DATABASE")
        else:
            messages.warning(request, "INVALID FORM")
        borrower=firstname+'_'+middlename+'_'+lastname+'_'+loanType
    return redirect('/entry/loans_receivable/borrower='+borrower)


def add_loan_payment(request, borrower):
    if request.method== 'POST' :
        form = LoanPaymentForm(request.POST)
        if form.is_valid():
            print("FORM VALIDATED")
            borrower = borrower.split("_")
            lpayment_form = form.cleaned_data
            date = lpayment_form.get("date")
            documentNumber = lpayment_form.get("documentNumber")
            firstname = borrower[0]
            middlename = borrower[1]
            lastname = borrower[2]
            paymentAmount = lpayment_form.get("paymentAmount")
            loanType = borrower[3]

            try:
                loan = LoansReceivable.objects.filter(
                    firstname=firstname,
                    middlename=middlename,
                    lastname=lastname,
                    loanType=loanType
                    )[0]
            except(LoansReceivable.DoesNotExist, IndexError):
                messages.warning(request, "BORROWER "+lastname+", "+firstname+" with "+loanType+" loan DOES NOT EXIST")
                return redirect('/entry/loan_payment/') 

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
                cash=paymentAmount,
                transaction=transaction
            )

            cash_entry.save()

            loan_payment = LoanPayment(
                client=client,
                loan=loan,
                date=date,
                documentNumber=documentNumber,
                firstname=firstname,
                middlename=middlename,
                lastname=lastname,
                paymentAmount=paymentAmount,
                transaction=transaction,
            )

            loan_payment.save()

            print("SUCCESSfully posted to database")
            messages.success(request, "SUCCESSFULLY POSTED ENTRY")

        else:
            messages.warning(request, "INVALID FORM")
        borrower=firstname+'_'+middlename+'_'+lastname+'_'+loanType
    return redirect('/entry/loan_payment/borrower='+borrower)
