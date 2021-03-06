# Generated by Django 3.2.6 on 2021-08-11 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_plan_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, help_text='email@gmail.com', max_length=200, null=True)),
                ('address', models.TextField(blank=True, help_text='address here', null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('phoneno', models.PositiveIntegerField(help_text='enter 10 digit phone number')),
                ('id_proof', models.ImageField(blank=True, null=True, upload_to='')),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('current_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.plan')),
            ],
        ),
    ]
