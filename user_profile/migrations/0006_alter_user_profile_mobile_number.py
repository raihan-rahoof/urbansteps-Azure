# Generated by Django 4.2.6 on 2023-11-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_user_profile_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='mobile_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
