# Generated by Django 5.0.4 on 2024-07-01 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('PLZ', models.IntegerField(null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
