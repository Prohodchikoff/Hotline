from django.db import models

def product_image_path(instance, filename):
    return 'images/products/p_{0}/{1}'.format(instance.product.name, filename)

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField()
    origin_country = models.ForeignKey(
        'cities_light.Country',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    create_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class ProductImages(models.Model):
    path = models.ImageField(upload_to=product_image_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    class Meta:
        db_table = 'product_images'
        verbose_name_plural = "product images"
 