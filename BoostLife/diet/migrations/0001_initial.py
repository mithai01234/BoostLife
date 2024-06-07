# Generated by Django 4.1.13 on 2024-06-05 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('carbs', models.BooleanField(default=False)),
                ('protein', models.BooleanField(default=False)),
                ('fat', models.BooleanField(default=False)),
                ('number_of_intake', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='diet_images/')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DietVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('preptime', models.CharField(max_length=50)),
                ('carbs', models.CharField(max_length=50)),
                ('fat', models.CharField(max_length=50)),
                ('protein', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='diet_videos/')),
                ('precautions', models.CharField(max_length=1000)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TimeofFood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='timeoffood_images/')),
                ('number_of_cup', models.CharField(max_length=50)),
                ('number_of_gram', models.CharField(max_length=50)),
                ('calories', models.CharField(max_length=50)),
                ('diet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.diet')),
            ],
        ),
    ]
