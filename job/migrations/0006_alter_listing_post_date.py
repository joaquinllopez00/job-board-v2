# Generated by Django 3.2.5 on 2021-07-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20210719_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='post_date',
            field=models.DateField(default='2021-07-20'),
        ),
    ]
