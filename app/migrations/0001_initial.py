# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('asset', models.CharField(max_length=200, unique=True)),
                ('dhash', models.CharField(max_length=1024, unique=True)),
                ('uuid', models.CharField(max_length=8, unique=True)),
            ],
        ),
    ]
