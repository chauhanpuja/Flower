# Generated by Django 3.2.5 on 2021-12-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_order_payment_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(default='', max_length=200),
        ),
    ]
