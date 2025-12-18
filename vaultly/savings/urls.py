from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingPlanViewSet, ContributionViewSet

router = DefaultRouter()
router.register(r'saving-plans', SavingPlanViewSet)
router.register(r'contributions', ContributionViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]