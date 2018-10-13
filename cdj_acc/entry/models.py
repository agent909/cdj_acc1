from django.db import models
from register.models import Client

# class Cash(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     date = models.DateTimeField('Document Date')

#     def __str__(self):
#         if(self.debit == 0):
#             return "credit: "+str(self.credit)
#         else:
#             return "debit: "+str(self.debit)


class Accounts(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    nameOfTransaction = models.ForeignKey(Accounts, on_delete=models.PROTECT)
    date_entry = models.DateTimeField('Entry Date')
    # add user attribute for LOGS

    def __str__(self):
        return str(self.id)+". "+self.nameOfTransaction.name


class AccountReceivable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField('Document Date')
    documentNumber = models.PositiveIntegerField()
    buyer = models.CharField(max_length=180)
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE, default=-1)

    def __str__(self):
        return str(self.transaction.id)+". "+self.buyer+" "+str(self.cash)


class PaymentToAccountReceivable(models.Model):
    receivable = models.ForeignKey(AccountReceivable, on_delete=models.PROTECT)
    documentNumber = models.PositiveIntegerField()
    date = models.DateField('Document Date')
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE, default=-1) 

    def __str__(self):
        return self.receivable.buyer+" cash: "+str(self.cash)


class Sales(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField('Document Date')
    documentNumber = models.PositiveIntegerField()
    buyer = models.CharField(max_length=180)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction.id)+". "+self.buyer+" "+str(self.amount)


class CashOnHand(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField('Document Date')
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)


class CashInBank(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField("Document Date")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)
