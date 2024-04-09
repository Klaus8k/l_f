from django.forms import ModelForm

from .models import Order, OrderItem

class OrderCreateForm(ModelForm):
    
    class Meta:
        model = Order
        fields = ('user_name', 'phone_number', 'email', 'address',
                  'telegram')
        
    