from django.forms import ModelForm, Form
from django import forms
from .models import Order, OrderItem

class OrderCreateForm(ModelForm):
    user_name = forms.CharField(required=False)
    telegram = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.CharField(required=False)
    
    class Meta:
        model = Order
        fields = ('user_name', 'phone_number', 'email', 'address',
                  'telegram')
        

class FastOrderCreateForm(ModelForm):
    user_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    address = forms.CharField(required=False)
    telegram = forms.CharField(required=False)
    
    
    class Meta:
        model = Order
        fields = ('phone_number',)
