# Generated by Django 4.2.5 on 2024-05-22 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item_old_price', models.FloatField()),
                ('discount', models.IntegerField()),
                ('item_new_price', models.FloatField()),
                ('most_popular', models.BooleanField()),
                ('recommended', models.BooleanField()),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.catagory')),
            ],
        ),
    ]