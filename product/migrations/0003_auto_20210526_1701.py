# Generated by Django 3.1.7 on 2021-05-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210526_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
