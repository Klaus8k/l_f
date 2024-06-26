import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'l_f.settings')

app = Celery('l_f')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


