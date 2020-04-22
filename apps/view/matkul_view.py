from django.shortcuts import render, redirect
from apps.models import MataKuliah, Admin
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from datetime import datetime


def data_matkul(request):
    if 'username' not in request.session:
        return render(request, 'admin/login.html')
    else:
        username = request.session.get('username')
        data = {
            'admin': Admin.objects.get(pk=username),
            'data_matkul': MataKuliah.objects.all().order_by('-created_at')
        }
        return render(request, 'admin/matkul.html', data)


def tambah_matkul(request):
    if request.method == 'POST':
        kd = request.POST['kd_mk']
        mk = request.POST['matkul']
        sks = request.POST['sks']
        if MataKuliah.objects.filter(kd_mk=kd).exists():
            return JsonResponse({'error': 1, 'message': 'Kode Mata Kuliah Sudah Ada !'})
        else:
            if int(sks) > 0 and int(sks) <= 10:
                date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                matkul = MataKuliah.objects.create(
                kd_mk=kd, mata_kuliah=mk, sks=sks, created_at=date, updated_at=date)
                return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Mata Kuliah'})
            else:
                return JsonResponse({'error': 2, 'message': 'SKS Tidak Boleh Kurang Dari 0 atau Lebih Dari 10'})
            
    else:
        return HttpResponse('Hayo ngapain kwkw')


def ubah_matkul(request):
    if request.method == 'POST':
        kd = request.POST['kd_mk']
        mk = request.POST['matkul']
        sks = request.POST['sks']

        if int(sks) > 0 and int(sks) <= 10:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            getMk = MataKuliah.objects.get(pk=kd)
            getMk.mata_kuliah = mk
            getMk.sks = sks
            getMk.updated_at = date
            getMk.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Mata Kuliah'})
        else:
            return JsonResponse({'error': 1, 'message': 'SKS Tidak Boleh Kurang Dari 0 atau Lebih Dari 10'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def hapus_matkul(request):
    if request.method == 'POST':
        kd = request.POST['kd_mk']

        getMk = MataKuliah.objects.get(kd_mk=kd)
        
        try:
            getMk.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Mata Kuliah'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Mata Kuliah'})

    else:
        return HttpResponse('Hayo ngapain kwkw')
