# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150116_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expiration_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]