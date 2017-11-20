# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_auto_20171103_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
        migrations.RemoveField(
            model_name='tripmember',
            name='email',
        ),
    ]