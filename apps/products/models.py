from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    price = models.PositiveIntegerField(verbose_name='Цена:')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество:')
    is_stock = models.BooleanField(default=False, db_index=True)
    category = models.ForeignKey(
        Category,
        related_name='product_category',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.title} -- {self.is_stock}"


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product',
        verbose_name='Картинки',
        blank=True, null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_image'
    )

    def __str__(self):
        return f"{self.product.title} -- {self.product.id}"
