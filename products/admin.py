from django.contrib import admin
from products.models import ProductModel

# registering product in admin panel
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = (
        "id",
        "title",
        "price",
        "category",
        "image",
        "rating_rate",
        "rating_count",
    )
    list_filter = ["category", "rating_rate", "price"]
    ordering = ("-price",)
    search_fields = ("name", "category")


admin.site.register(ProductModel, ProductAdmin)
