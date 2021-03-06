# Generated by Django 3.2.6 on 2021-08-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('Duration', models.TextField(choices=[('ONE MONTH', 'ONE MONTH'), ('SIX MONTH', 'SIX MONTH'), ('TWELVE MONTH', 'TWELVE MONTH')], default='')),
                ('cost', models.PositiveIntegerField()),
            ],
        ),
    ]
