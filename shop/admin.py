from django.contrib import admin
from .models import Category, Product, Comment, Rating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'slug', 'quantity_product', 'price', 'image',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'total_likes']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'body', 'created',
                    'updated', 'active']
    list_filter = ['user', 'created', 'active']
    list_editable = ['body']


@admin.register(Rating)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'product', 'created']
    list_filter = ['user', 'rating', 'created']
    list_editable = ['rating']
