from django.db import models
from register.models import Client


class Accounts(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    nameOfTransaction = models.ForeignKey(Accounts, on_delete=models.PROTECT)
    date_entry = models.DateTimeField('Entry Date')

    def __str__(self):
        return str(self.id)+". "+self.nameOfTransaction.name


class AccountReceivable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField('Document Date')
    documentNumber = models.PositiveIntegerField()
    buyer = models.CharField(max_length=180)
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction.id)+". "+self.buyer+" "+str(self.cash)


class PaymentToAccountReceivable(models.Model):
    receivable = models.ForeignKey(AccountReceivable, on_delete=models.PROTECT)
    documentNumber = models.PositiveIntegerField()
    date = models.DateField('Document Date')
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE) 

    def __str__(self):
        return self.receivable.buyer+" cash: "+str(self.cash)


class Sales(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField('Document Date')
    documentNumber = models.PositiveIntegerField()
    buyer = models.CharField(max_length=180)
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction.id)+". "+self.buyer+" "+str(self.cash)


class CashOnHand(models.Model): 
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField('Document Date')
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cash)


class CashInBank(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField("Document Date")
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cash)


class LoansReceivable(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField("Document Date")
    documentNumber = models.PositiveIntegerField()
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    amountApplied = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    loanType = models.CharField(max_length=20)
    modeOfPayment = models.CharField(max_length=15)
    termsOfPaymentYear = models.PositiveIntegerField(default=0)
    termsOfPaymentMonth = models.PositiveIntegerField(default=0)
    termsOfPaymentDay = models.PositiveIntegerField(default=0)
    interestRate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    methodOfInterest = models.CharField(max_length=10)
    serviceFee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    penaltyRate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname+", "+self.firstname+" "+str(self.amountApplied)


class ServiceFee(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField("Document Date")
    cash = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return self.cash


class LoanPayment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    loan = models.ForeignKey(LoansReceivable, on_delete=models.CASCADE)
    date = models.DateField("Document Date")
    documentNumber = models.PositiveIntegerField()
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    paymentAmount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname+", "+self.firstname+" "+str(self.paymentAmount)
