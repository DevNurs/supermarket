from supermarket.celery import app
from django.core.mail import send_mail
from apps.sms_sender.models import MessageSender


@app.task
def send_message_to_email(email):
    send_mail(
        'Hello, I am ГАИ',
        "You must pay 1000$ for my Steam Account, if you don't pay I'm gonna kill you",
        'nursultandev@gmail.com',
        [email],
        fail_silently=False,
    )


@app.task
def spam_email():
    for email in MessageSender.objects.all():
        send_mail(
            'Hello, I am ГАИ',
            "You must pay 1000$ for my Steam Account, if you don't pay I'm gonna kill you",
            'nursultandev@gmail.com',
            [email.email],
            fail_silently=False,
        )

