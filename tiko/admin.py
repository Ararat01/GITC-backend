from django.contrib import admin

from .models import Product, Users

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    pass

