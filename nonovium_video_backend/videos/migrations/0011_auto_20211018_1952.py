# Generated by Django 3.1.13 on 2021-10-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0010_video_uploaded_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
