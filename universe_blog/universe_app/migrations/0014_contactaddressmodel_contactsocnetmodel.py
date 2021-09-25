# Generated by Django 3.2.6 on 2021-09-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0013_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSocNetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]