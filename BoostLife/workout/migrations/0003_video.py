# Generated by Django 4.2.5 on 2024-06-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_workout_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('time', models.CharField(max_length=50)),
                ('repetition_time', models.CharField(max_length=50)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.workout')),
            ],
        ),
    ]
