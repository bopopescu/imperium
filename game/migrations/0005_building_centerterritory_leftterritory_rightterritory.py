# Generated by Django 2.2.5 on 2020-02-24 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0004_auto_20200218_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, default='Поле', max_length=20)),
                ('corn', models.IntegerField(blank=True, default=1)),
                ('subordinate', models.IntegerField(blank=True, default=1)),
                ('warrior', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RightTerritory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(default='Поле', max_length=20)),
                ('corn', models.IntegerField(blank=True, default=0)),
                ('subordinate', models.IntegerField(blank=True, default=0)),
                ('warrior', models.IntegerField(blank=True, default=0)),
                ('lastBuild', models.CharField(blank=True, default='Поле', max_length=20)),
                ('flagConstruct', models.BooleanField(blank=True, default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeftTerritory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(default='Поле', max_length=20)),
                ('corn', models.IntegerField(blank=True, default=0)),
                ('subordinate', models.IntegerField(blank=True, default=0)),
                ('warrior', models.IntegerField(blank=True, default=0)),
                ('lastBuild', models.CharField(blank=True, default='Поле', max_length=20)),
                ('flagConstruct', models.BooleanField(blank=True, default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CenterTerritory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(default='Поле', max_length=20)),
                ('corn', models.IntegerField(blank=True, default=0)),
                ('subordinate', models.IntegerField(blank=True, default=0)),
                ('warrior', models.IntegerField(blank=True, default=0)),
                ('lastBuild', models.CharField(blank=True, default='Поле', max_length=20)),
                ('flagConstruct', models.BooleanField(blank=True, default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
