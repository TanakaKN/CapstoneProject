from django.shortcuts import render
from rest_framework import viewsets
from .models import SavingPlan
from .serializers import SavingPlanSerializer

# Create your views here.
class SavingPlanViewSet(viewsets.ModelViewSet):
    queryset = SavingPlan.objects.all()
    serializer_class = SavingPlanSerializer
