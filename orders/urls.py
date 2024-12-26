from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PlatformApiCallViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)
router.register(r'platform-apicalls', PlatformApiCallViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
