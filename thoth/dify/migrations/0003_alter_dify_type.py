# Generated by Django 5.2 on 2025-05-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dify', '0002_alter_dify_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dify',
            name='type',
            field=models.CharField(choices=[('chatflow', 'Chatflow'), ('workflow', 'Workflow')], default='chatflow', max_length=10),
        ),
    ]
