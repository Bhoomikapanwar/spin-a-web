# Generated by Django 2.0.2 on 2018-02-02 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('b_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=100)),
                ('b_ifsc', models.CharField(max_length=11)),
                ('b_address', models.TextField()),
                ('b_email', models.EmailField(max_length=254)),
                ('b_phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
