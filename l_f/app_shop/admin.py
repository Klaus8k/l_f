from django.contrib import admin
from .models import Category, Product, Tag
# Register your models here.

class TagsInline(admin.TabularInline):
    model = Product.tag.through



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'category', 'price',
                    'stock', 'available',]
    list_filter = ['available', 'category']
    list_editable = ['price', 'category', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        TagsInline,
    ]
    
    exclude = ('tag',)
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag',]

    
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
