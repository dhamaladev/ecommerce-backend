from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, URLValidator

# product model
class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    description = models.TextField()
    category = models.CharField(max_length=255)
    image = models.URLField(validators=[URLValidator()])
    rating_rate = models.FloatField()
    rating_count = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'products'
