# Generated by Django 3.0 on 2020-08-13 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nilai',
            name='skor',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)]),
            preserve_default=False,
        ),
    ]