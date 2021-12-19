from django.db import models
from django.contrib.auth.models import AbstractUser

def product_image_directory(instance, filename):
    return f'products/{instance.name}-{filename}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    product_info = models.TextField()
    product_price =  models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=product_image_directory)
    updated_at = models.DateTimeField(auto_now=True)

    def creat_equal_update(self):
        attrs = ('day', 'year', 'month', 'hour', 'minute', 'second')
        for attr in attrs:
            if getattr(self.created_at, attr) != getattr(self.updated_at, attr):
                return False

        return True
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Users(AbstractUser):
    class Meta:
        abstract = False