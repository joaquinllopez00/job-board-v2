# Generated by Django 3.2.5 on 2021-07-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210715_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
