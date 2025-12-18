from django.shortcuts import render
from rest_framework import viewsets
from .models import SavingPlan, Contribution
from .serializers import SavingPlanSerializer, ContributionSerializer

# Create your views here.
class SavingPlanViewSet(viewsets.ModelViewSet):
    queryset = SavingPlan.objects.all()
    serializer_class = SavingPlanSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
