# Generated by Django 2.2 on 2019-06-12 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20190612_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='renewed',
        ),
    ]
