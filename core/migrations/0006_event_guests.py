# Generated by Django 5.0.7 on 2024-08-06 05:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_event_guests'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='guest_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
