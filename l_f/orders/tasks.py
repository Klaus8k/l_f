from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Спасибо {order.user_name} за заказ № {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'tipkor@mail.ru',
                          [order.email])
    return mail_sent