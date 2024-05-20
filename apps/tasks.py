import time

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from apps.models import User


@shared_task
def send_to_user_email(email: str, message: str):
    print(email, message)
    send_mail('Tema', message, settings.EMAIL_HOST_USER, [email])
    return f'{email} ga yuborildi'