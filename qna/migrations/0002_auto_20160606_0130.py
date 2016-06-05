# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
