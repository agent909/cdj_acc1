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

# Create your models here.
