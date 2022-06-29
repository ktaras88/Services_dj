# Generated by Django 4.0.5 on 2022-06-29 11:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('price', models.IntegerField(default=0)),
                ('worker_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.worker')),
            ],
        ),
    ]
