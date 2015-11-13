# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_picture_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='dhash',
            field=models.CharField(unique=True, default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='asset',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
