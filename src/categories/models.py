import unidecode
from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Categories(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode.unidecode(self.name))
        return super().save(*args, **kwargs)

    def applicable_attribute_category_ids(self):
        return self.get_ancestors(include_self=True).values_list('pk', flat=True)
