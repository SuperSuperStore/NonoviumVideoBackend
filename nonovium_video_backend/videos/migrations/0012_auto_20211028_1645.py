# Generated by Django 3.1.13 on 2021-10-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_auto_20211028_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='$22659f4c-8ee8-402f-b69b-0c216ed2b30f', editable=False, max_length=256),
        ),
    ]
