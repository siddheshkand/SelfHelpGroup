from django.db import models

from Collection.models import User


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    granter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='granter')
    amount = models.PositiveIntegerField()
    repay_amount = models.PositiveIntegerField()
    interest_rate = models.PositiveIntegerField()
    remaining_principal = models.PositiveIntegerField()
    remaining_interest = models.PositiveIntegerField()
    remaining_fine = models.PositiveIntegerField()
