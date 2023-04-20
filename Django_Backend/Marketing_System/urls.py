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


urlpatterns = router.urls + marketer_router.urls 
