from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingPlanViewSet, ContributionViewSet

from .views import home, plans_list, plan_detail, withdraw, create_plan


router = DefaultRouter()
router.register(r'saving-plans', SavingPlanViewSet)
router.register(r'contributions', ContributionViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
    path('plans/', plans_list, name='plans'),
    path('plans/<int:plan_id>/', plan_detail, name='plan_detail'),
    path('plans/create/', create_plan, name='create_plan'),

]

urlpatterns += [
    path('saving-plans/<int:plan_id>/withdraw/', withdraw),
]