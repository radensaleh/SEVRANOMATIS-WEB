# Generated by Django 3.0 on 2020-03-23 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_auto_20200323_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ampumatkul',
            name='nipnya',
        ),
        migrations.AddField(
            model_name='ampumatkul',
            name='nipnya',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.Dosen'),
        ),
    ]
