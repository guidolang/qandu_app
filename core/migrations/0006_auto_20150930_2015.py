# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150930_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='visibility',
        ),
        migrations.RemoveField(
            model_name='question',
            name='visibility',
        ),
    ]
