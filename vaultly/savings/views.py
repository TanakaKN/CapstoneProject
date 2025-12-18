from django.shortcuts import render
from rest_framework import viewsets
from .models import SavingPlan, Contribution
from .serializers import SavingPlanSerializer, ContributionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import SavingPlan, Withdrawal


# Create your views here.
class SavingPlanViewSet(viewsets.ModelViewSet):
    queryset = SavingPlan.objects.all()
    serializer_class = SavingPlanSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

    
@api_view(['POST'])
def withdraw(request, plan_id):
    plan = get_object_or_404(SavingPlan, id=plan_id)

    if not plan.can_withdraw():
        return Response(
            {"error": "Withdrawal not allowed before end date."},
            status=status.HTTP_400_BAD_REQUEST
        )

    amount = plan.total_saved()

    Withdrawal.objects.create(
        saving_plan=plan,
        amount=amount
    )

    return Response(
        {
            "message": "Withdrawal successful",
            "amount": amount
        },
        status=status.HTTP_200_OK
    )


