# Generated by Django 3.2 on 2021-05-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210501_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='ctv',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='oxygenPatient',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
