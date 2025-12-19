from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import SavingPlan, Contribution, SavingPlan
from .serializers import SavingPlanSerializer, ContributionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import SavingPlan, Withdrawal
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def plans_list(request):
    plans = SavingPlan.objects.filter(user=request.user)
    return render(request, 'savings/plans.html', {'plans': plans})

@login_required
def plan_detail(request, plan_id):
    plan = SavingPlan.objects.get(id=plan_id, user=request.user)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        Contribution.objects.create(
            saving_plan=plan,
            amount=amount
        )
        return redirect('plan_detail', plan_id=plan.id)

    return render(request, 'savings/plan_detail.html', {'plan': plan})

@login_required
def create_plan(request):
    if request.method == 'POST':
        SavingPlan.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            target_amount=request.POST.get('target_amount'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            frequency=request.POST.get('frequency'),
            target_per_period=request.POST.get('target_per_period'),
        )
        return redirect('plans')

    return render(request, 'savings/create_plan.html')

@login_required
def plans_list(request):
    plans = SavingPlan.objects.filter(user=request.user)
    return render(request, 'savings/plans.html', {'plans': plans})


@login_required
def plan_detail(request, plan_id):
    plan = get_object_or_404(SavingPlan, id=plan_id, user=request.user)

    if request.method == 'POST':
        if 'amount' in request.POST:
            Contribution.objects.create(
            saving_plan=plan,
            amount=request.POST.get('amount')
        )

            return redirect('plan_detail', plan_id=plan.id)
       
        plan.name = request.POST.get('name', plan.name)
        plan.target_amount = request.POST.get('target_amount', plan.target_amount)
        plan.save()

    contributions = Contribution.objects.filter(saving_plan=plan)

    return render(request, 'savings/plan_detail.html', {
        'plan': plan,
        'contributions': contributions
    })


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


