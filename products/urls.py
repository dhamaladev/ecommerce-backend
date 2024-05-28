from django.urls import path
from products.views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductTitleSearchView,
    ProductCategoryFilterView,
    ProductCreateView,
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='all_products'),
    path('products/create', ProductCreateView.as_view(), name='create_product'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/search/<str:title>/', ProductTitleSearchView.as_view(), name='product_search'),
    path('products/category/<str:category>/', ProductCategoryFilterView.as_view(), name='product_category_filter'),
]
