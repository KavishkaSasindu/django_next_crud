# Generated by Django 5.0 on 2023-12-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='age',
            field=models.CharField(max_length=10),
        ),
    ]
