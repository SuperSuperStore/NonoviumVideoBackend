# Generated by Django 3.1.14 on 2022-01-23 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nonovium_video_backend.pipelines.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=nonovium_video_backend.pipelines.models.user_directory_path)),
                ('video_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('width', models.PositiveIntegerField(editable=False, null=True)),
                ('height', models.PositiveIntegerField(editable=False, null=True)),
                ('size', models.PositiveIntegerField(editable=False, null=True)),
                ('duration', models.FloatField(editable=False, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
