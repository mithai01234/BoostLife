# Generated by Django 4.2.5 on 2024-06-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0006_alter_workoutbanner_workout_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
