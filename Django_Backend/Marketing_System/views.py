from rest_framework.viewsets import ModelViewSet
from .serializers import *

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MarketerViewSet(ModelViewSet):
    queryset = Marketer.objects.all()
    serializer_class = MarketerSerializer
