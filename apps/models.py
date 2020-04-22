from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Admin(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    nama = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class Dosen(models.Model):
    nip = models.CharField(max_length=18, primary_key=True)
    nama = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)

class MataKuliah(models.Model):
    kd_mk = models.CharField(max_length=10, primary_key=True)
    mata_kuliah = models.CharField(max_length=50)
    sks = models.PositiveIntegerField(validators=[MaxValueValidator(2)])
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)


class Kelas(models.Model):
    kd_kelas = models.CharField(max_length=10, primary_key=True)
    kelas = models.CharField(max_length=60)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)


class AmpuMatkul(models.Model):
    kd_ampu = models.CharField(max_length=10, primary_key=True)
    nip = models.ForeignKey(Dosen, on_delete=models.PROTECT)
    kd_mk = models.ForeignKey(MataKuliah, on_delete=models.PROTECT)
    kd_kelas = models.ForeignKey(Kelas, on_delete=models.PROTECT)
    semester = models.PositiveIntegerField(validators=[MaxValueValidator(2)])
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)
    
class Mahasiswa(models.Model):
    nim = models.CharField(max_length=10, primary_key=True)
    nama = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    kd_kelas = models.ForeignKey(Kelas, on_delete=models.PROTECT)
    jurusan = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)


class Soal(models.Model):
    kd_soal = models.CharField(max_length=10, primary_key=True)
    kd_ampu = models.ForeignKey(AmpuMatkul, on_delete=models.PROTECT)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)

class DetailSoal(models.Model):
    id = models.AutoField(primary_key=True)
    kd_soal = models.ForeignKey(Soal, on_delete=models.PROTECT)
    soal = models.TextField()
    jawaban = models.TextField()
    bobot = models.PositiveIntegerField(validators=[MaxValueValidator(3)])
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)


class Nilai(models.Model):
    kd_nilai = models.CharField(max_length=10, primary_key=True)
    kd_soal = models.ForeignKey(Soal, on_delete=models.PROTECT)
    nim = models.ForeignKey(Mahasiswa, on_delete=models.PROTECT)
    nilai = models.PositiveIntegerField(validators=[MaxValueValidator(3)])
    index = models.CharField(max_length=2)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)
