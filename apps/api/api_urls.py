from django.contrib import admin
from django.urls import path, include
from apps.api import mahasiswa

urlpatterns = [
    #mahasiswa
    path('login', mahasiswa.login, name='api-login'),
    path('profile', mahasiswa.profile, name='api-profile'),
    path('matkul', mahasiswa.matkul, name='api-matkul'),
    path('soal', mahasiswa.soal, name='api-soal'),
    path('detail-soal', mahasiswa.detail_soal, name='api-detail-soal'),
    path('soal-proccess', mahasiswa.soal_proccess, name='api-soal-proccess'),
    path('ranking', mahasiswa.ranking, name='api-ranking'),
    path('nilai', mahasiswa.nilai, name='api-nilai'),
]

