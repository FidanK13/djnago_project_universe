# Generated by Django 3.2.6 on 2021-09-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0007_navbarmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='workmodel',
            name='work_head_image',
            field=models.ImageField(blank=True, null=True, upload_to='work_image'),
        ),
    ]
