from django.db import models
from register.models import Client


class Cash(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField('Document Date')

    def __str__(self):
        if(self.debit == 0):
            return "credit: "+str(self.credit)
        else:
            return "debit: "+str(self.debit)


class AccountReceivable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    documentNumber = models.PositiveIntegerField()
    soldTo = models.CharField(max_length=180)
    particulars = models.CharField(max_length=500)

    def __str__(self):
        return self.particulars


class CashAdvance(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    cashVoucherNumber = models.PositiveIntegerField()
    payee = models.CharField(max_length=180)

    def __str__(self):
        return self.payee


class AccountPayable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    documentNumber = models.PositiveIntegerField()
    item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    vendor = models.CharField(max_length=200)

    def __str__(self):
        return self.item


class LoansPayable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Date Issued')
    lending_company = models.CharField('Lending Company', max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    service_fee = models.DecimalField(max_digits=12, decimal_places=2)
    payable_in = models.PositiveIntegerField('Years to be paid', default=0)
    interest = models.DecimalField(max_digits=5, decimal_places=2)

# --------------------------------------------------------------------

class AccountReceivableEntry(models.Model):
    account_receivable = models.ForeignKey(AccountReceivable, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField('Entry Date')
    # account_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        if(self.debit == 0):
            return "credit: "+str(self.credit)
        else:
            return "debit: "+str(self.debit)


class CashAdvanceEntry(models.Model):
    account_receivable = models.ForeignKey(CashAdvance, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField('Entry Date')
    # account_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        if(self.debit == 0):
            return "credit: "+str(self.credit)
        else:
            return "debit: "+str(self.debit)


class AccountPayableEntry(models.Model):
    account_receivable = models.ForeignKey(AccountPayable, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField('Entry Date')
    # account_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        if(self.debit == 0):
            return "credit: "+str(self.credit)
        else:
            return "debit: "+str(self.debit)


class LoansPayableEntry(models.Model):
    account_receivable = models.ForeignKey(LoansPayable, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField('Entry Date')
    # account_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        if(self.debit == 0):
            return "credit: "+str(self.credit)
        else:
            return "debit: "+str(self.debit)

#Create your models here.