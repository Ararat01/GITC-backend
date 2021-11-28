from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    product_info = models.TextField()
    product_price =  models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'