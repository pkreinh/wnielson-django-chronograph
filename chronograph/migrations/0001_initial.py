# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 09:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('frequency', models.CharField(choices=[(b'YEARLY', 'Yearly'), (b'MONTHLY', 'Monthly'), (b'WEEKLY', 'Weekly'), (b'DAILY', 'Daily'), (b'HOURLY', 'Hourly'), (b'MINUTELY', 'Minutely'), (b'SECONDLY', 'Secondly')], max_length=10, verbose_name='frequency')),
                ('params', models.TextField(blank=True, help_text='Comma-separated list of <a href="http://labix.org/python-dateutil" target="_blank">rrule parameters</a>. e.g: interval:15', null=True, verbose_name='params')),
                ('command', models.CharField(blank=True, help_text='A valid django-admin command to run.', max_length=200, verbose_name='command')),
                ('args', models.CharField(blank=True, help_text='Space separated list; e.g: arg1 option1=True', max_length=200, verbose_name='args')),
                ('disabled', models.BooleanField(default=False, help_text='If checked this job will never run.')),
                ('next_run', models.DateTimeField(blank=True, help_text="If you don't set this it will be determined automatically", null=True, verbose_name='next run')),
                ('last_run', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='last run')),
                ('is_running', models.BooleanField(default=False, editable=False)),
                ('last_run_successful', models.BooleanField(default=True, editable=False)),
                ('lock_file', models.CharField(blank=True, editable=False, max_length=255)),
                ('force_run', models.BooleanField(default=False)),
                ('subscribers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('disabled', 'next_run'),
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_date', models.DateTimeField(auto_now_add=True)),
                ('stdout', models.TextField(blank=True)),
                ('stderr', models.TextField(blank=True)),
                ('success', models.BooleanField(default=True, editable=False)),
                ('duration', models.FloatField(editable=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronograph.Job')),
            ],
            options={
                'ordering': ('-run_date',),
            },
        ),
    ]
