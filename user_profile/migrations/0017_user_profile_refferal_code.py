# Generated by Django 4.2.6 on 2023-12-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0016_wishlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_profile",
            name="refferal_code",
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
