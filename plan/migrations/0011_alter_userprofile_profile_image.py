# Generated by Django 3.2.6 on 2021-08-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_auto_20210812_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/demo.jpg', null=True, upload_to='imgaes/profiles'),
        ),
    ]
