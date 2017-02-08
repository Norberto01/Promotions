# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20170207_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='email_document',
            field=models.ForeignKey(help_text='Only excel are allowed! xls and xlsx file extensions.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Emails file list'),
        ),
    ]
