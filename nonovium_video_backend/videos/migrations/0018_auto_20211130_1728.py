# Generated by Django 3.1.13 on 2021-11-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0017_auto_20211118_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='266512d1-b0a6-42de-a590-f579f9889f76', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='slug',
            field=models.CharField(blank=True, editable=False, max_length=255, unique=True),
        ),
    ]
