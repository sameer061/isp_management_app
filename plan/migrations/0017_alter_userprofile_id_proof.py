# Generated by Django 3.2.6 on 2021-08-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0016_alter_userprofile_id_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id_proof',
            field=models.FileField(blank=True, null=True, upload_to='id_proof'),
        ),
    ]
