from .views import ProductView, BrandView, CategoryView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "ecommerceshop"

router = DefaultRouter()
router.register(r"api/brands", BrandView, basename="brand")
router.register(r"api/categories", CategoryView, basename="category")
# router.register(r"api/porducts", ProductView, basename="ecommerceshop")
router.register(
    r"api/porducts/(?P<name>[^/.]+)", ProductView, basename="ecommerceshop_detail"
)
# router.register(r"api/porducts/", ProductView, basename="ecommerceshop")
# urlpatterns = router.urls


urlpatterns = [
    path("", include(router.urls)),
]
