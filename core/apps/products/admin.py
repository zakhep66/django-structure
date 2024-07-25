from django.contrib import admin

from core.apps.products import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
        'is_visible',
        'created_at',
        'updated_at',
    )
