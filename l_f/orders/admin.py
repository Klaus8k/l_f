from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'email', 'address',
                    'telegram', 'created_at', 'updated_at', 'paid')
    list_filter = ('created_at', 'updated_at', 'paid')
    inlines = [OrderItemAdmin]
    
admin.site.register(Order, OrderAdmin)