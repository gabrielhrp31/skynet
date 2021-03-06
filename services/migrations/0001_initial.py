# Generated by Django 2.2 on 2019-05-22 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0009_auto_20190522_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_price', models.FloatField(default=0.0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('avg_time', models.FloatField(blank=True, default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('employees_available', models.IntegerField(default=0)),
                ('contracts', models.ManyToManyField(through='services.Contract', to='clientes.Client')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.Service'),
        ),
    ]
