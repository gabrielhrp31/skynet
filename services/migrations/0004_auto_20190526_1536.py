# Generated by Django 2.2 on 2019-05-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_contract_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
