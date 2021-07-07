from django.contrib import admin
from apps.sms_sender.models import MessageSender

admin.site.register(MessageSender)
