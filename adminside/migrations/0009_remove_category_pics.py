# Generated by Django 4.2.6 on 2023-10-23 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0008_category_pics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pics',
        ),
    ]
