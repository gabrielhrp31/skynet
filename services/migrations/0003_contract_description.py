# Generated by Django 2.2 on 2019-05-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_contract_daily_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
