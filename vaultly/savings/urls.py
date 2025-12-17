from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingPlanViewSet

router = DefaultRouter()
router.register(r'saving-plans', SavingPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]