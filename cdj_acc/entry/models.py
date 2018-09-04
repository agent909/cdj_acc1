from django.db import models


class Entry(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    date = models.DateTimeField('Entry date')


class AccountReceivable(models.Model):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    documentNumber = models.PositiveIntegerField()
    soldTo = models.CharField(max_length=180)
    particulars = models.CharField(max_length=500)
    cash = models.DecimalField(decimal_places=5)


class CashAdvance(models.Model):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
    date = models.DateTimeField('Document Date')
    cashVoucherNumber = models.PositiveIntegerField()
    payee = models.CharField(max_length=180)
    cash = models.DecimalField(decimal_places=5)


class AccountPayable(models.Model):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
    date = models.DateTimeField('Dacument Date')
    documentNumber = models.PositiveIntegerField()
    item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=5)
    totalAmount = models.DecimalField(decimal_places=5)


# Create your models here.
