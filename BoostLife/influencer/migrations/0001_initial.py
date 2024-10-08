# Generated by Django 4.1.13 on 2024-08-10 15:06

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=255)),
                ('otp_value', models.CharField(blank=True, max_length=6)),
                ('passbook', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('password', models.CharField(max_length=128)),
                ('address', models.TextField()),
                ('type', models.CharField(max_length=10)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=10)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('is_influencer', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, related_name='influencer_groups', related_query_name='influencer_group', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='influencer_user_permissions', related_query_name='influencer_user_permission', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Influencer',
                'verbose_name_plural': 'Influencers',
            },
        ),
        migrations.CreateModel(
            name='InfluencerLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('influencer_code', models.CharField(max_length=20)),
                ('ip_address', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfluencerOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=6)),
                ('otp_created_at', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='influencer.influencer')),
            ],
        ),
    ]
