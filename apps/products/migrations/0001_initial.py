# Generated by Django 3.2.4 on 2021-06-07 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена:')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество:')),
                ('is_stock', models.BooleanField(db_index=True, default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='categories.category')),
            ],
        ),
    ]
