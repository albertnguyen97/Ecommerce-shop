# Generated by Django 4.2.7 on 2023-12-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='category-icon', max_length=50),
        ),
    ]
