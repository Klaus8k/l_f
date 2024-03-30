from decimal import Decimal
from django.conf import settings
from app_shop.models import Product

class Cart(object):
    def __init__(self, request):
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[session.CART_SESSION_ID] = {}
            
        self.cart = cart
        
        # https://pocoz.gitbooks.io/django-v-primerah/content/glava-7-sozdanie-internet-magazina/sozdanie-korzini/hranenie-korzini-pokupok-v-sessiyah.html