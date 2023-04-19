from rest_framework.viewsets import ModelViewSet
from .serializers import *

def ensure_Marketer_pk(kwargs, key, value):
    if kwargs.get(key) is not None and kwargs[key] == 'me':
        kwargs[key] = value


# --------------------------------------------------------------------------

class MarketerProductViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GetSmallProductSerializer

    def get_queryset(self):
        return Product.objects.filter(marketers__user__id=self.kwargs['marketer_pk']) \
            
class MarketerViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GetMarketerSerializer

    queryset = Marketer.objects \
                .select_related('user') \
                .prefetch_related('products') \

# --------------------------------------------------------------------------

class ProductMarketerViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GetSmallMarketerSerializer

    def get_queryset(self):
        return Marketer.objects \
            .filter(products__id=self.kwargs['product_pk']) \
            .select_related('user') \


class ProductViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GetProductSerializer

    queryset = Product.objects \
                .prefetch_related('marketers') \
                .prefetch_related('marketers__user') \
                
