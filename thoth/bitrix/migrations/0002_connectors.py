# Generated by Django 5.2 on 2025-04-24 03:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrix', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='gulin_0463ce74-39f5-49f2-803c-1c7cda67dae5', max_length=255, unique=True)),
                ('service', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(default='gulin.kz', max_length=255)),
                ('icon', models.FileField(blank=True, null=True, upload_to='connector_icons/')),
            ],
        ),
        migrations.RemoveField(
            model_name='app',
            name='connector',
        ),
        migrations.AddField(
            model_name='line',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='line',
            name='portal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='bitrix.bitrix'),
        ),
        migrations.AddField(
            model_name='app',
            name='connectors',
            field=models.ManyToManyField(blank=True, related_name='apps', to='bitrix.connector'),
        ),
        migrations.AddField(
            model_name='line',
            name='connector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='bitrix.connector'),
        ),
    ]
