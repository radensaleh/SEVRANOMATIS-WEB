# Generated by Django 3.0 on 2020-08-13 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_nilai_skor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lognilai',
            old_name='skor_akhir',
            new_name='status',
        ),
    ]
