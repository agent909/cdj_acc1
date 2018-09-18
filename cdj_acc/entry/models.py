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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nameOfTransaction = models.ForeignKey(Accounts)
    date_entry = models.DateTimeField('Entry Date')
    # add user attribute for LOGS

    def __str__(self):
        return self.nameOfTransaction+" "+str(self.date_entry)


class AccountReceivable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    documentNumber = models.PositiveIntegerField()
    buyer = models.CharField(max_length=180)
    # account_receivable = models.ForeignKey(AccountReceivable, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction_id = models.ForeignKey(Transactions)
    # cash = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.particulars


class Sales(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    documentNumber = models.PositiveIntegerField()
    buyer = models.CharField(max_length=180)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    item = models.CharField(max_length=500)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.buyer+" "+str(self.cash)



# class CashAdvance(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date = models.DateTimeField('Document Date')
#     cashVoucherNumber = models.PositiveIntegerField()
#     payee = models.CharField(max_length=180)

#     def __str__(self):
#         return self.payee


# class AccountPayable(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date = models.DateTimeField('Document Date')
#     documentNumber = models.PositiveIntegerField()
#     item = models.CharField(max_length=200)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     vendor = models.CharField(max_length=200)

#     def __str__(self):
#         return self.item


# class LoansPayable(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date = models.DateTimeField('Date Issued')
#     lending_company = models.CharField('Lending Company', max_length=200)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     service_fee = models.DecimalField(max_digits=12, decimal_places=2)
#     payable_in = models.PositiveIntegerField('Years to be paid', default=0)
#     interest = models.DecimalField(max_digits=5, decimal_places=2)

# --------------------------------------------------------------------

# class AccountReceivableEntry(models.Model):
#     # This CLASS could be WRONG!
#     account_receivable = models.ForeignKey(AccountReceivable, on_delete=models.CASCADE)
#     debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     date = models.DateTimeField('Entry Date')
#     transaction_id = models.PositiveIntegerField()
#     # account_id = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         if(self.debit == 0):
#             return "credit: "+str(self.credit)
#         else:
#             return "debit: "+str(self.debit)


# class CashAdvanceEntry(models.Model):
#     account_receivable = models.ForeignKey(CashAdvance, on_delete=models.CASCADE)
#     debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     date = models.DateTimeField('Entry Date')
#     # account_id = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         if(self.debit == 0):
#             return "credit: "+str(self.credit)
#         else:
#             return "debit: "+str(self.debit)


# class AccountPayableEntry(models.Model):
#     account_receivable = models.ForeignKey(AccountPayable, on_delete=models.CASCADE)
#     debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     date = models.DateTimeField('Entry Date')
#     # account_id = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         if(self.debit == 0):
#             return "credit: "+str(self.credit)
#         else:
#             return "debit: "+str(self.debit)


# class LoansPayableEntry(models.Model):
#     account_receivable = models.ForeignKey(LoansPayable, on_delete=models.CASCADE)
#     debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     date = models.DateTimeField('Entry Date')
#     # account_id = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         if(self.debit == 0):
#             return "credit: "+str(self.credit)
#         else:
#             return "debit: "+str(self.debit)

#Create your models here.