# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_auto_20160625_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
