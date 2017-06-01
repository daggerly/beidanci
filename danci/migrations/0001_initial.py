# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-28 07:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danci',
            fields=[
                ('word', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('meaning', models.CharField(max_length=50)),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa')),
            ],
        ),
        migrations.CreateModel(
            name='MeaningmodeRecord',
            fields=[
                ('danci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='danci.Danci')),
                ('corrected', models.PositiveSmallIntegerField(default=0, verbose_name='\u6b63\u786e\u6b21\u6570')),
                ('last_dt', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u80cc')),
                ('next_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0b\u6b21\u80cc')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa')),
                ('learned', models.BooleanField(default=False, verbose_name='\u638c\u63e1\u4e86')),
            ],
            options={
                'ordering': ('-next_dt',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WordmodeRecord',
            fields=[
                ('danci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='danci.Danci')),
                ('corrected', models.PositiveSmallIntegerField(default=0, verbose_name='\u6b63\u786e\u6b21\u6570')),
                ('last_dt', models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u6b21\u80cc')),
                ('next_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0b\u6b21\u80cc')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa')),
                ('learned', models.BooleanField(default=False, verbose_name='\u638c\u63e1\u4e86')),
            ],
            options={
                'ordering': ('-next_dt',),
                'abstract': False,
            },
        ),
    ]
