# Generated by Django 3.0 on 2020-03-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0018_auto_20200323_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ampumatkul',
            name='kd_ampu',
            field=models.CharField(max_length=18, primary_key=True, serialize=False),
        ),
    ]
