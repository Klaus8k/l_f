from django.db import models
from app_shop.models import Product


class Order(models.Model):

    user_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ: {self.id}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, related_name='items' ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items' ,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
    
    def __str__(self):
        return f'{self.id}'
    
    def get_cost(self):
        return self.price * self.quantity
    