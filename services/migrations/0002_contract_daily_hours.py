# Generated by Django 2.2 on 2019-05-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='daily_hours',
            field=models.FloatField(default=0.0),
        ),
    ]
