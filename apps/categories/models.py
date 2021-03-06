from django.db import models
from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True, blank=True
    )
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"{self.title} -- {self.slug}"


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Category)

