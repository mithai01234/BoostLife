# Generated by Django 4.2.5 on 2024-06-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='category',
            field=models.CharField(default=None, max_length=500),
        ),
    ]