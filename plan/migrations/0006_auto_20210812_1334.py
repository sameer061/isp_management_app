# Generated by Django 3.2.6 on 2021-08-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_auto_20210812_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
