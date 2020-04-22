from django.shortcuts import render, redirect
from apps.models import Mahasiswa, Kelas, Nilai, Admin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from datetime import datetime


def data_mahasiswa(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        username = request.session.get('username')
        data = {
            'admin': Admin.objects.get(pk=username),
            'data_mahasiswa': Mahasiswa.objects.all().order_by('-created_at'),
            'data_kelas': Kelas.objects.all()
        }
        return render(request, 'admin/mahasiswa.html', data)


def tambah_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']
        pswd = nim
        kelas = request.POST['kd_kelas']
        jurusan = request.POST['jurusan']
        prodi = request.POST['prodi']

        if Mahasiswa.objects.filter(nim=nim).exists():
            return JsonResponse({'error': 1, 'message': 'NIM Mahasiswa Sudah Ada !'})
        else:
            if int(nim) > 0 and len(nim) == 7:
                date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                mhs = Mahasiswa.objects.create(nim=nim, nama=nama, password=pswd, kd_kelas_id=kelas,
                                           jurusan=jurusan, prodi=prodi, created_at=date, updated_at=date)
                return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Mahasiswa'})
            else:
                return JsonResponse({'error': 2, 'message': 'NIM Harus Berisikan Angka dan Terdiri dari 7 Digit !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def ubah_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']
        pswd = request.POST['password']
        kelas = request.POST['kd_kelas']
        jurusan = request.POST['jurusan']
        prodi = request.POST['prodi']

        if pswd not in '':
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            getMhs = Mahasiswa.objects.get(pk=nim)
            getMhs.nama = nama
            getMhs.password = pswd
            getMhs.kd_kelas_id = kelas
            getMhs.jurusan = jurusan
            getMhs.prodi = prodi
            getMhs.updated_at = date
            getMhs.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Mahasiswa !'})
        else:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            getMhs = Mahasiswa.objects.get(pk=nim)
            getMhs.nama = nama
            getMhs.password = getMhs.password
            getMhs.kd_kelas_id = kelas
            getMhs.jurusan = jurusan
            getMhs.prodi = prodi
            getMhs.updated_at = date
            getMhs.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Mahasiswa !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')

def hapus_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST['nim']

        getMhs = Mahasiswa.objects.get(pk=nim)

        try:
            getMhs.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Mahasiswa'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Mahasiswa'})
        
    else:
        return HttpResponse('Hayo ngapain kwkw')

# data nilai
def data_nilai(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        username = request.session.get('username')
        data = {
            'admin': Admin.objects.get(pk=username),
            'data_nilai': Nilai.objects.all().order_by('-created_at')
        }
        return render(request, 'admin/nilai_mahasiswa.html', data)
