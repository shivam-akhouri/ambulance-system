# Generated by Django 3.2 on 2021-05-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_messages_ambulancename'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='ctv',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='disease',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='messages',
            name='oxygenPatient',
            field=models.IntegerField(null=True),
        ),
    ]
