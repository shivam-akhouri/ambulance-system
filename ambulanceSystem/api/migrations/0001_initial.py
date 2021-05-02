# Generated by Django 3.2 on 2021-05-01 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('driverName', models.CharField(max_length=30)),
                ('healthWorker', models.IntegerField()),
                ('oxyCylinderMeter', models.FloatField()),
                ('severity', models.IntegerField()),
                ('posLatitude', models.FloatField()),
                ('posLongtude', models.FloatField()),
                ('phoneno', models.IntegerField()),
                ('hospitalName', models.CharField(max_length=30)),
                ('ambulanceGmeet', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
