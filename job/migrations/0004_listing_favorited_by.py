# Generated by Django 3.2.5 on 2021-07-15 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0003_alter_listing_compensation'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorited_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
