# Generated by Django 4.1.5 on 2023-04-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0003_product_colors_product_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tarih - Saat'),
        ),
    ]