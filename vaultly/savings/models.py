from django.db import models
from django.contrib.auth.models import User

class SavingPlan(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saving_plans')
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    target_per_period = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


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



