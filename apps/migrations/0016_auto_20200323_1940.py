# Generated by Django 3.0 on 2020-03-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_auto_20200323_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ampumatkul',
            name='kd_kelas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_kelas', to='apps.Kelas'),
        ),
        migrations.AlterField(
            model_name='ampumatkul',
            name='kd_mk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_matkul', to='apps.MataKuliah'),
        ),
        migrations.AlterField(
            model_name='ampumatkul',
            name='nip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_dosen', to='apps.Dosen'),
        ),
    ]
