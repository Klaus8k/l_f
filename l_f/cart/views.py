from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app_shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# https://pocoz.gitbooks.io/django-v-primerah/content/glava-7-sozdanie-internet-magazina/sozdanie-korzini/sozdanie-predstavlenii-korzini-pokupok/dobavlenie-elementov-v-korzinu.html