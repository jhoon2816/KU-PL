# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0005_auto_20160629_0554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='downvote',
            new_name='vote',
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvote',
        ),
    ]
