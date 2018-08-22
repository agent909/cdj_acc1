from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    # password = 


class UserDirectory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_num = models.CharField(max_length=20)


# class Client(models.Model):
