# Generated by Django 4.2.6 on 2023-10-21 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_auth', '0002_customer_is_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_blocked',
        ),
    ]
