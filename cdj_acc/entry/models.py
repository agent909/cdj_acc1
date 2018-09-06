from django.db import models
from register.models import Client


class Entry(models.Model):
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date = models.DateTimeField('Entry Date')
    account_id = models.PositiveIntegerField(default=0)


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

#Create your models here.