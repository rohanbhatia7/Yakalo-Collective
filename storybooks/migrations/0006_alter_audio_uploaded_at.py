# Generated by Django 4.0.3 on 2022-04-19 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storybooks', '0005_alter_audio_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 4, 31, 8, 771241)),
        ),
    ]
