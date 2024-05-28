import requests
from products.models import ProductModel

def data_loader():
    response = requests.get("https://fakestoreapi.com/products")
    data = response.json()

    for product_data in data:
        product, created = ProductModel.objects.get_or_create(
            title=product_data['title'],
            price=product_data["price"],
            defaults={
                'description': product_data["description"],
                'category': product_data["category"],
                'image': product_data["image"],
                'rating_rate': product_data["rating"]["rate"],
                'rating_count': product_data["rating"]["count"],
            }
        )
        if not created:
            product.title = product_data["title"]
            product.price = product_data["price"]
            product.description = product_data["description"]
            product.category = product_data["category"]
            product.image = product_data["image"]
            product.rating_rate = product_data["rating"]["rate"]
            product.rating_count = product_data["rating"]["count"]
            product.save()
