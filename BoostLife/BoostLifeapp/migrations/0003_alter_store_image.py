# Generated by Django 4.1.13 on 2024-08-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoostLifeapp', '0002_alter_store_address_alter_store_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.FileField(upload_to='store_name/'),
        ),
    ]