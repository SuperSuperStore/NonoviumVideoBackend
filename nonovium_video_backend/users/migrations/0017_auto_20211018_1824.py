# Generated by Django 3.1.13 on 2021-10-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_auto_20211018_1635"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_image",
            field=models.CharField(
                default="https://avatars.dicebear.com/api/avataaars/58430.svg?size=150",
                max_length=250,
                verbose_name="Profile Image URL",
            ),
        ),
    ]
