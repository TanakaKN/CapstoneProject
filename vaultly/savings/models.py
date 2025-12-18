from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone


class SavingPlan(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saving_plans')
    name_of_plan = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    target_per_period = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def total_saved(self):
        total = self.contributions.aggregate(
            total=Sum('amount')
        )['total']
        return total or 0
    

    def can_withdraw(self):
        return timezone.now().date() >= self.end_date
   

    def total_withdrawn(self):
        total = self.withdrawals.aggregate(
            total=Sum('amount')
             )['total']
        return total or 0
    
    def current_balance(self):
        return self.total_saved() - self.total_withdrawn()


    def __str__(self):
        return self.name_of_plan


class Contribution(models.Model):
    saving_plan = models.ForeignKey(
        SavingPlan,
        on_delete=models.CASCADE,
        related_name='contributions'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} contribution"

class Withdrawal(models.Model):
    saving_plan = models.ForeignKey(
        SavingPlan,
        on_delete=models.CASCADE,
        related_name='withdrawals'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Withdrawal {self.amount}"



