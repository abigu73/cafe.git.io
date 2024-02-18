# Generated by Django 5.0.1 on 2024-02-18 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_description_product_volume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='volume',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]