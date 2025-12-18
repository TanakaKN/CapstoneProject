from rest_framework import serializers
from .models import SavingPlan

class SavingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingPlan
        fields = '__all__'


from .models import Contribution

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

