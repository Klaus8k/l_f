from django.contrib import admin
from .models import Category, Product, Tag
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'category', 'tag', 'price',
                    'stock', 'available',]
    list_filter = ['available', 'tag', 'category']
    list_editable = ['price', 'category','tag', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
