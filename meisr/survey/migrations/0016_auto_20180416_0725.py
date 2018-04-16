# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0015_archive'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='archive',
            unique_together=set([('user', 'question', 'submit_count')]),
        ),
    ]