# Generated by Django 2.2.5 on 2020-02-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_session_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='round',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='session',
            name='time',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]