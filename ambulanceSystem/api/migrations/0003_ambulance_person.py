# Generated by Django 3.2 on 2021-05-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210501_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='person',
            field=models.IntegerField(null=True),
        ),
    ]
