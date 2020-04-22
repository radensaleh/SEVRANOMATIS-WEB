from django.contrib import admin
from django.urls import path, include
from apps.view import admin_view, dosen_view, kelas_view, ampumatkul_view, matkul_view, mahasiswa_view

urlpatterns = [
    #tampil data
    path('', admin_view.login, name='login'),
    path('logout', admin_view.logout, name='logout'),
    path('dashboard', admin_view.dashboard, name='dashboard'),
    path('data-dosen', dosen_view.data_dosen, name='data-dosen'),
    path('data-ampu', ampumatkul_view.data_ampu, name='data-ampu'),
    path('data-kelas', kelas_view.data_kelas, name='data-kelas'),
    path('data-matkul', matkul_view.data_matkul, name='data-matkul'),
    path('data-mahasiswa', mahasiswa_view.data_mahasiswa, name='data-mahasiswa'),
    path('data-nilai', mahasiswa_view.data_nilai, name='data-nilai'),
    
    path('pengaturan', admin_view.pengaturan, name='pengaturan'),

    #Kelas
    path('tambah-kelas', kelas_view.tambah_kelas, name='tambah-kelas'),
    path('ubah-kelas', kelas_view.ubah_kelas, name='ubah-kelas'),
    path('hapus-kelas', kelas_view.hapus_kelas, name='hapus-kelas'),

    #Matkul
    path('tambah-matkul', matkul_view.tambah_matkul, name='tambah-matkul'),
    path('ubah-matkul', matkul_view.ubah_matkul, name='ubah-matkul'),
    path('hapus-matkul', matkul_view.hapus_matkul, name='hapus-matkul'),

    #Dosen
    path('tambah-dosen', dosen_view.tambah_dosen, name='tambah-dosen'),
    path('ubah-dosen', dosen_view.ubah_dosen, name='ubah-dosen'),
    path('hapus-dosen', dosen_view.hapus_dosen, name='hapus-dosen'),

    #Mahasiswa
    path('tambah-mahasiswa', mahasiswa_view.tambah_mahasiswa, name='tambah-mahasiswa'),
    path('ubah-mahasiswa', mahasiswa_view.ubah_mahasiswa, name='ubah-mahasiswa'),
    path('hapus-mahasiswa', mahasiswa_view.hapus_mahasiswa, name='hapus-mahasiswa'),

    #Dosen Pengampu Matkul
    path('tambah-ampu', ampumatkul_view.tambah_ampu,name='tambah-ampu'),
    path('ubah-ampu', ampumatkul_view.ubah_ampu, name='ubah-ampu'),
    path('hapus-ampu', ampumatkul_view.hapus_ampu, name='hapus-ampu'),
]
