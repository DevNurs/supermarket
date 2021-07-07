from django.views.generic import CreateView
from apps.sms_sender.models import MessageSender
from apps.sms_sender.forms import MessageSenderForm
from apps.sms_sender.tasks import send_message_to_email


class MessageSenderCreateView(CreateView):
    model = MessageSender
    form_class = MessageSenderForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        send_message_to_email.delay(form.instance.email)
        return super().form_valid(form)



