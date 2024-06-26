from django.conf import settings
from app_shop.models import Product


class Cart:
    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product: Product, quаntity=1, update_quantity=False):
        """Добавить продукт в корзину (с количеством) рили обновить его количество

        Args:
            product (_type_): _description_
            quantity (int, optional): _description_. Defaults to 1.
            update_quantity (bool, optional): _description_. Defaults to False.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quаntity

        else:
            self.cart[product_id]['quantity'] += quаntity
        self.save()

    def save(self):
        """Обновить сессию корзины"""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product: Product):
        """Удалить продукт из корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор всех продуктов в корзине"""

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Подсчет всех товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Подсчет общей стоимости товаров
        """

        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """clear cart"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True