# Generated by Django 2.2 on 2019-05-08 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190505_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=60)),
                ('district', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=2)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='photo',
        ),
        migrations.AddField(
            model_name='client',
            name='occupation',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='clientes.Address'),
        ),
    ]
