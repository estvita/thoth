# Generated by Django 5.2.1 on 2025-05-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='olxuser',
            name='attempts',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='olxuser',
            name='status',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
