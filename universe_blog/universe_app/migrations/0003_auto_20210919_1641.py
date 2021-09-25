# Generated by Django 3.2.6 on 2021-09-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0002_footer_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='blog_subtitle',
            new_name='blog_subtitle_f',
        ),
        migrations.AddField(
            model_name='settings',
            name='blog_subtitle_s',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='blog_subtitle_t',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]