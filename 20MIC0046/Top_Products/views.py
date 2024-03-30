from rest_framework import generics, pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Product
from .serializers import ProductSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['rating', 'price', 'company', 'discount']
    ordering = ['-rating'] # Default ordering

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Product.objects.filter(category=category_name)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'