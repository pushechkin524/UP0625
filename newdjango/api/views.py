from rest_framework import viewsets, permissions, filters
from .models import *
from .serializers import *


# Пример только чтения
class ReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [filters.SearchFilter]
    pagination_class = None  # отключим локально если нужно

# Полный доступ, но с правами из админки
class FullAccessViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]

# Чтение, но не изменять
class ProductViewSet(ReadOnlyViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']

class CategoryViewSet(ReadOnlyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']

class BrandViewSet(ReadOnlyViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    search_fields = ['name']

class ReviewViewSet(FullAccessViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    search_fields = ['comment']

class OrderViewSet(FullAccessViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    search_fields = ['buyer_name']

class PosOrderViewSet(ReadOnlyViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
    search_fields = ['product__name']

class FaqViewSet(ReadOnlyViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    search_fields = ['question']

class SeasonViewSet(ReadOnlyViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    search_fields = ['name']

class FavoriteViewSet(FullAccessViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    search_fields = ['product__name']
