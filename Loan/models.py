from django.db import models

from Collection.models import User, Bank, WorkingMonth


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    granter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='granter')
    amount = models.PositiveIntegerField()
    repay_amount = models.PositiveIntegerField()
    interest_rate = models.PositiveIntegerField()
    remaining_principal = models.PositiveIntegerField()
    remaining_interest = models.PositiveIntegerField()
    remaining_fine = models.PositiveIntegerField()
    granted_date = models.DateField()
    duration_months = models.PositiveIntegerField()


class LoanDetails(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class LoanRepay(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    month = models.ForeignKey(WorkingMonth, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    amount_paid = models.PositiveIntegerField()
