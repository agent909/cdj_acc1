from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    position = models.CharField(max_length=200)


class UserDirectory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_num = models.CharField(max_length=20)


class Client(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contactNum = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    companyName = models.CharField(max_length=500)

    def __str__(self):
        return self.lastname+" "+self.firstname