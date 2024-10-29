from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, TypeViewSet, PriceViewSet

router = DefaultRouter()
router.register(r'types', TypeViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/decrease_quantity/', ProductViewSet.as_view({'post': 'decrease_quantity'}), name='decrease_quantity'),
]