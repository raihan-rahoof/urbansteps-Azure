# Generated by Django 4.2.6 on 2023-11-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
    ]
