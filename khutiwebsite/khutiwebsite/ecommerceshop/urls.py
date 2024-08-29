from .views import (
    ProductView,
    BrandView,
    CategoryView,
    ProductCategoryViewSet,
    ProductByCategoryViewSet,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "ecommerceshop"

router = DefaultRouter()
router.register(r"api/brands", BrandView, basename="brand")
router.register(r"api/categories", CategoryView, basename="category")
router.register(r"api/porducts", ProductView, basename="ecommerceshop")
# router.register(
#     r"api/porduct_by_category",
#     ProductByCategoryViewSet,
#     basename="ecommerceshop_category",
# )
router.register(
    r"api/porduct_by_category",
    ProductByCategoryViewSet,
    basename="product_by_category",
)
router.register(
    r"api/porduct/categories",
    ProductCategoryViewSet,
    basename="ecommerceshop-categories",
)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api/product_by_category/<str:category>/",
        ProductByCategoryViewSet.as_view({"get": "retrieve"}),
        name="product-by-category",
    ),
]
