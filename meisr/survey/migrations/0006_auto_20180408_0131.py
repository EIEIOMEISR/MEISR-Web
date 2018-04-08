# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_remove_profile_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default='1996-08-13'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Not yet'), (2, 'Sometimes'), (3, 'Often/Beyond')], null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='starting_age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='routine',
            name='number',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
