# Generated by Django 5.2.1 on 2025-06-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrix', '0008_alter_bitrix_domain_alter_bitrix_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitrix',
            name='license_expired',
            field=models.BooleanField(default=False),
        ),
    ]
