from rest_framework import serializers
from .models import SavingPlan

class SavingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingPlan
        fields = '__all__'
