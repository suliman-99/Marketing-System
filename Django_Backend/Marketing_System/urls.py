from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(
    'product',
    ProductViewSet,
    basename='product'
)
router.register(
    'marketer',
    MarketerViewSet,
    basename='marketer'
)

urlpatterns = router.urls
