# Generated by Django 3.0 on 2020-07-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0024_auto_20200724_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='soal',
            name='judul_soal',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
