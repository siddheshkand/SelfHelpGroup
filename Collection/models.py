from django.db import models


# Create your models here.

class WorkingMonth(models.Model):
    month = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


class Bank(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


class Role(models.Model):
    role_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class User(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class UserCollection(models.Model):
    year = models.IntegerField()
    month = models.ForeignKey(WorkingMonth, on_delete=models.CASCADE)
    paid = models.BooleanField(default=True)


class UserPaymentDetails(models.Model):
    user_collection = models.ForeignKey(UserCollection, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class BankTransaction(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)  # Credit or Debit
    amount = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=100)


class Balance(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    current = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
