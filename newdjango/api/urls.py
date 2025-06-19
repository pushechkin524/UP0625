from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'posorders', PosOrderViewSet)
router.register(r'faqs', FaqViewSet)
router.register(r'seasons', SeasonViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = router.urls
