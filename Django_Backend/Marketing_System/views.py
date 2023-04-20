from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import permissions
from .serializers import *

def ensure_Marketer_pk(kwargs, key, value):
    if kwargs[key] == 'me':
        kwargs[key] = value


# --------------------------------------------------------------------------

class MarketerProductViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GetSmallProductSerializer

    def get_permissions(self):
        if self.kwargs['marketer_pk'] != 'me' and self.request.user.id != int(self.kwargs['marketer_pk']):
            return [permissions.IsAdminUser()]
        else:
            return super().get_permissions()

    def get_queryset(self):
        ensure_Marketer_pk(self.kwargs, 'marketer_pk', self.request.user.id)
        return Product.objects \
            .filter(marketers__user__id=self.kwargs['marketer_pk'])  \
            
class MarketerViewSet(RetrieveModelMixin, GenericViewSet):
    http_method_names = ['get']
    serializer_class = GetMarketerSerializer

    def get_permissions(self):
        if self.kwargs['pk'] != 'me' and self.request.user.id != int(self.kwargs['pk']):
            return [permissions.IsAdminUser()]
        else:
            return super().get_permissions()

    def get_queryset(self):
        ensure_Marketer_pk(self.kwargs, 'pk', self.request.user.id)
        return Marketer.objects \
            .select_related('user') \
            .prefetch_related('products') \

# --------------------------------------------------------------------------

class ProductViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GetProductSerializer

    queryset = Product.objects \
                .prefetch_related('marketers') \
                .prefetch_related('marketers__user') \
                
