# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(default='temporary', max_length=100)),
                ('image', models.FileField(default='pic_folder/None/no-img.jpg', upload_to='images/')),
            ],
        ),
    ]