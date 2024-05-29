from django.urls import path
from products.views import ProductListCreateView, ProductDetailUpdateDeleteView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product_list_create"),
    path(
        "products/<int:id>/",
        ProductDetailUpdateDeleteView.as_view(),
        name="product_detail_update_delete",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
