# Generated by Django 2.2.28 on 2024-11-02 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20241102_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Card number must be 16 digits', regex='^\\d{16}$')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(message='CVV must be 3 or 4 digits', regex='^\\d{3,4}$')]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
