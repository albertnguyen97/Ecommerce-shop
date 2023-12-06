# Generated by Django 4.2.7 on 2023-11-26 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_product',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
