# Generated by Django 3.0 on 2020-08-13 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20200813_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='lognilai',
            name='skor_akhir',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)]),
            preserve_default=False,
        ),
    ]
