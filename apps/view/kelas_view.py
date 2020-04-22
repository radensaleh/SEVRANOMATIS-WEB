from django.shortcuts import render, redirect
from apps.models import Kelas, Admin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.urls import reverse

def data_kelas(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        username = request.session.get('username')
        data = {
            'admin': Admin.objects.get(pk=username),
            'data_kelas': Kelas.objects.all().order_by('-created_at')
        }
        return render(request, 'admin/kelas.html', data)


def tambah_kelas(request):
    if request.method == 'POST':
        kd = request.POST['kd_kelas']
        kelas = request.POST['kelas']
        
        if Kelas.objects.filter(kd_kelas=kd).exists():
            return JsonResponse({'error': 1, 'message': 'Kode Kelas Sudah Ada !'})
        else:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            kelas = Kelas.objects.create(
                kd_kelas=kd, kelas=kelas, created_at=date, updated_at=date)
            return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Kelas'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def ubah_kelas(request):
    if request.method == 'POST':
        kd = request.POST['kd_kelas']
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        getKelas = Kelas.objects.get(pk=kd)
        getKelas.kelas = request.POST['kelas']
        getKelas.updated_at = date
        getKelas.save()
        return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Kelas'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def hapus_kelas(request):
    if request.method == 'POST':
        kd = request.POST['kd_kelas']

        getKelas = Kelas.objects.get(pk=kd)

        try:
            getKelas.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Kelas'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Kelas'})

    else:
        return HttpResponse('Hayo ngapain kwkw')
