# Generated by Django 3.1.13 on 2021-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0016_auto_20211118_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='$a276b9b8-043a-4ec8-be21-5b424c1e0bf9', editable=False, max_length=256),
        ),
    ]
