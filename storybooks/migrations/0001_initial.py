# Generated by Django 4.0.2 on 2022-02-22 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('title', models.CharField(default='Untitled Audio', max_length=255)),
                ('description', models.CharField(default='Empty', max_length=2048)),
                ('archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audio_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'audio file',
                'verbose_name_plural': 'audio files',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('spaced', models.BooleanField()),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Storybook', max_length=255)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storybooks.audio')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translation_author', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translation_language', to='storybooks.language')),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'translation',
                'verbose_name_plural': 'translations',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('index', models.IntegerField()),
                ('timestamp', models.IntegerField(null=True)),
                ('translation', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='storybooks.translation')),
            ],
            options={
                'verbose_name': 'story',
                'verbose_name_plural': 'stories',
            },
        ),
    ]