from django.db import models


class MessageSender(models.Model):
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} -- {self.email}"
