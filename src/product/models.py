from django.apps import apps
from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import TreeForeignKey


def product_image_path(instance, filename):
    return 'images/products/p_{0}/{1}'.format(instance.product.name, filename)


def get_default_category():
    Categories = apps.get_model('categories', 'Categories')
    category, _ = Categories.objects.get_or_create(name='Other')
    return category.pk


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

    category = TreeForeignKey(
        'categories.Categories',
        on_delete=models.PROTECT,
        default=get_default_category,
        verbose_name='category',
    )

    def __str__(self):
        return f"{self.name}"

    def clean(self):
        if self.category and self.category.level != 2 and self.category.name != 'Other':
            raise ValidationError({'category': 'Products can only be assigned to level-2 categories.'})
        return super().clean()


class ProductImages(models.Model):
    path = models.ImageField(upload_to=product_image_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'product_images'
        verbose_name_plural = "product images"
