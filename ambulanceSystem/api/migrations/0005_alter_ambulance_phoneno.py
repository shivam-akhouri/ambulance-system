# Generated by Django 3.2 on 2021-05-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210501_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='phoneno',
            field=models.BigIntegerField(null=True),
        ),
    ]
