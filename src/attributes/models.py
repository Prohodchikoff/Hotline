from django.core.exceptions import ValidationError
from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        'categories.Categories',
        on_delete=models.CASCADE,
        related_name='attributes',
    )

    class Meta:
        unique_together = [['category', 'name']]
        verbose_name_plural = 'attributes'

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name='values',
    )
    value = models.CharField(max_length=50)

    class Meta:
        unique_together = [['attribute', 'value']]
        verbose_name_plural = 'attribute values'

    def __str__(self):
        return self.value


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='product_attributes',
    )
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['product', 'attribute']]

    def clean(self):
        if self.value.attribute_id != self.attribute_id:
            raise ValidationError('Value does not belong to this attribute.')
        if self.attribute.category_id not in self.product.category.applicable_attribute_category_ids():
            raise ValidationError('Attribute does not belong to product category.')
