# Generated by Django 5.2 on 2025-04-21 10:08

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bitrix', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OlxApp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('client_domain', models.CharField(choices=[('olx.kz', 'olx.kz'), ('olx.bg', 'olx.bg'), ('olx.ro', 'olx.ro'), ('olx.ua', 'olx.ua'), ('olx.pt', 'olx.pt'), ('olx.pl', 'olx.pl')], max_length=10)),
                ('client_id', models.CharField(max_length=255)),
                ('client_secret', models.CharField(max_length=255)),
                ('authorization_link', models.URLField(blank=True, editable=False, max_length=500, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olx_apps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OlxUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodicity', models.PositiveIntegerField(default=10, help_text='Frequency of OLX server polling in minutes.')),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('olx_id', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('access_token', models.CharField(blank=True, max_length=255, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=255, null=True)),
                ('line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olx_users', to='bitrix.line')),
                ('olxapp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='olx_users', to='olx.olxapp')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='olx_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
