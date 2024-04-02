from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app_shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd['quantity'])
        cart.add(product=product,
                 quаntity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product_id = int(product_id)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart_detail.html', context)


# https://pocoz.gitbooks.io/django-v-primerah/content/glava-7-sozdanie-internet-magazina/sozdanie-korzini/sozdanie-predstavlenii-korzini-pokupok/dobavlenie-elementov-v-korzinu.html