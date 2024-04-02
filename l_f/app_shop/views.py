"""
This module provides the views for the product app.
"""
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    """
    Renders the product list view. 

    Args:
        request (HttpRequest): The current request.
        category_slug (str, optional): The slug of the selected category.

    Returns:
        HttpResponse: The rendered product list view.
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'app_shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    """
    Renders the product detail view.

    Args:
        request (HttpRequest): The current request.
        id (int): The ID of the product.
        slug (str): The slug of the product.

    Returns:
        HttpResponse: The rendered product detail view.
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'app_shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


