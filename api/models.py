from datetime import datetime
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Categories(MPTTModel):
    parent = TreeForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
    
    


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        Categories, blank=True, null=True,  on_delete=models.CASCADE, related_name="data")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Products(models.Model):
    parent = models.ForeignKey(
        SubCategory, blank=True, null=True,  on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    images = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])
