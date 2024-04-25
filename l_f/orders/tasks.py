from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from l_f.config import get_config

auth_password = get_config().conf_dict


@shared_task
def order_created(order_id):
    
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Спасибо {order.user_name} за заказ № {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          '',
                          [order.email])
    return mail_sent

# Отправка почты
# https://stackoverflow.com/questions/49697705/issues-printing-django-email-to-console