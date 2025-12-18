from rest_framework import serializers
from .models import SavingPlan
from .models import Contribution
from .models import Withdrawal

class SavingPlanSerializer(serializers.ModelSerializer):
    total_saved = serializers.SerializerMethodField()
    current_balance = serializers.SerializerMethodField()
    class Meta:
        model = SavingPlan
        fields = '__all__'

    def get_total_saved(self, obj):
        return obj.total_saved()

    def get_current_balance(self, obj):
        return obj.current_balance()
class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = '__all__'

