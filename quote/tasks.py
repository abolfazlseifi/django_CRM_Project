from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def send_email_task():
    send_mail(
        'Celery Task ',
        'seifi.eng@gmail.com',
        [
            'seifi.eng@gmail.com',
        ])

    return None
