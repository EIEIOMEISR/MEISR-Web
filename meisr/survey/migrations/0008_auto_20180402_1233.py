# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 12:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0007_auto_20180331_0645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['starting_age', 'question_text']},
        ),
        migrations.AddField(
            model_name='answer',
            name='routine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.Routine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='routine',
            name='choice',
            field=models.IntegerField(choices=[(1, 'Waking Up'), (2, 'Meal Times'), (3, 'Getting Dressed'), (4, 'Toileting/Diaper'), (5, 'Outings (Going Out)'), (6, 'Play Time With Others'), (7, 'Play Time by Him or Herself'), (8, 'Nap Time'), (9, 'Bath Time'), (10, 'Hanging Out Time (including TV & Books)'), (11, 'Grocery Shopping'), (12, 'Outside Time'), (13, 'Bedtime'), (14, 'Transition Time')]),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('question', 'routine', 'user')]),
        ),
    ]
