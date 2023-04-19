from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()

router.register(
    'marketers',
    MarketerViewSet,
    basename='marketers'
)
router.register(
    'products',
    ProductViewSet,
    basename='products'
)

# --------------------------------------------------------------------------

marketer_router = routers.NestedDefaultRouter(
    router,
    'marketers',
    lookup='marketer'
)

marketer_router.register(
    'products',
    MarketerProductViewSet,
    basename='marketer-products'
)

# --------------------------------------------------------------------------

product_router = routers.NestedDefaultRouter(
    router,
    'products',
    lookup='product'
)

product_router.register(
    'marketers',
    ProductMarketerViewSet,
    basename='product-marketers'
)

# --------------------------------------------------------------------------

urlpatterns = router.urls + marketer_router.urls + product_router.urls
