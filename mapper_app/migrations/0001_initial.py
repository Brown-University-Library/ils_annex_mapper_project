# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationMapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='Set automatically on save.')),
                ('modify_date', models.DateTimeField(auto_now=True, help_text='Set automatically on save.')),
                ('ils_code', models.CharField(help_text='This is the Josiah `Location` code.', max_length=50)),
                ('las_code', models.CharField(help_text='This the the LAS `Customer Code` code.', max_length=50)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PickupAtMapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='Set automatically on save.')),
                ('modify_date', models.DateTimeField(auto_now=True, help_text='Set automatically on save.')),
                ('ils_code', models.CharField(help_text='This is the Josiah `Pickup At` code.', max_length=50)),
                ('las_code', models.CharField(help_text='This the the LAS `Customer Code` code.', max_length=50)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
