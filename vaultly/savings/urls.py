from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingPlanViewSet, ContributionViewSet

from .views import withdraw


router = DefaultRouter()
router.register(r'saving-plans', SavingPlanViewSet)
router.register(r'contributions', ContributionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('saving-plans/<int:plan_id>/withdraw/', withdraw),
]