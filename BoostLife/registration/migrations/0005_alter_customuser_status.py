# Generated by Django 4.2.5 on 2024-05-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_customuser_activity_level_alter_customuser_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
