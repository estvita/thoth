# Generated by Django 5.2.1 on 2025-05-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_articlepage_canonical_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='menu_title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='menu_title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='tariffpage',
            name='menu_title',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
