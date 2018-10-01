from django.utils import timezone
from entry.models import Accounts, Sales, Transactions, AccountReceivable
from register.models import Client

# The code should go like this BRO


# GET id of selected CLIENT
client = Client.objects.get(pk=1)

# GET the name of the Account used
account_name = Accounts.objects.get(name=request.POST['account_selector'])

# CREATE TRANSACTION
transaction = Transactions(client=client, nameOfTransaction=account_name, date_entry=timezone.localtime(timezone.now()))
transaction.save()

#GET TRANSACTION ID 
transaction_id = transaction.id


# GET DETAILS ON THE TEMPLATE FORM then create A/R
AR = AccountReceivable(
    client=client,
    date=date,
    documentNumber=documentNumber,
    buyer=buyer,
    cash=amount,
    transaction_id=transaction.id,
)

# GET ITEMS ON and Add it to Sales.
    # iterate through the list of items listed in the Table (provided by the user).