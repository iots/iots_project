# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iots_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='notes',
            field=models.CharField(max_length=50),
        ),
    ]
