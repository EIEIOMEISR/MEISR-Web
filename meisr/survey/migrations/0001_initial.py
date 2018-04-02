# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 13:52
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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Not yet'), (2, 'Sometimes'), (3, 'Often'), (4, 'Beyond This')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DevelopmentalDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('A', 'A = adaptive'), ('CG', 'CG = cognitive'), ('CM', 'CM = communication'), ('M', 'M = motor'), ('S', 'S = social')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='FunctionalDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('E', 'E = engagement'), ('I', 'I = independence'), ('S', 'S = social relationships')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('S', 'S = positive social relations'), ('K', 'K = acquiring and using knowledge and skills'), ('A', 'A = taking action to meet needs')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, unique=True)),
                ('starting_age', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['starting_age', 'question_text'],
            },
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dev', models.DecimalField(decimal_places=2, max_digits=4)),
                ('func', models.DecimalField(decimal_places=2, max_digits=4)),
                ('out', models.DecimalField(decimal_places=2, max_digits=4)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Routine'),
        ),
        migrations.AddField(
            model_name='outcome',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out', to='survey.Question'),
        ),
        migrations.AddField(
            model_name='functionaldomain',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='func', to='survey.Question'),
        ),
        migrations.AddField(
            model_name='developmentaldomain',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev', to='survey.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='outcome',
            unique_together=set([('question', 'choice')]),
        ),
        migrations.AlterUniqueTogether(
            name='functionaldomain',
            unique_together=set([('question', 'choice')]),
        ),
        migrations.AlterUniqueTogether(
            name='developmentaldomain',
            unique_together=set([('question', 'choice')]),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('question', 'user')]),
        ),
    ]
