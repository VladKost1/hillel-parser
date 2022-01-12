import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
import django
import logging


logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heaven_site.settings')

django.setup()

app = Celery('heaven_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=20, minute=20), clean_logs.s(), name="clean logs")


@app.task
def clean_logs():
    from middleware.models import Logger
    old_logs = Logger.objects.filter(created__lte=timezone.now() - timedelta(days=7))
    old_logs.delete()


@app.task
def send_email_task(subject, message, sender, recipient):
    logger.info(message)
    send_mail(subject, message, sender, recipient)
