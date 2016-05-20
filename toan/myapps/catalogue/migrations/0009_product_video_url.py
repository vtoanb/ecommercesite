# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20160304_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_url',
            field=models.URLField(default='www.youtube.com'),
            preserve_default=False,
        ),
    ]
