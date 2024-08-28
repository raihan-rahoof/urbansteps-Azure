# Generated by Django 4.2.6 on 2023-11-25 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0012_onlinepayment_order_alter_order_payment_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("code", models.CharField(max_length=50)),
                ("discount", models.PositiveIntegerField()),
                ("min_amount", models.IntegerField()),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="CouponUsage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=50)),
                ("total_amount", models.BigIntegerField()),
                ("disount_amount", models.BigIntegerField()),
                ("used", models.BooleanField()),
                ("valid_from", models.DateField(null=True)),
                ("valid_to", models.DateField(null=True)),
                ("usage_time", models.DateField(auto_now=True)),
                (
                    "coupon",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.coupons",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
