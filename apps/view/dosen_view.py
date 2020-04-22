from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from django.urls import reverse
from apps.models import Dosen, Admin


def data_dosen(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        username = request.session.get('username')
        data = {
            'admin': Admin.objects.get(pk=username),
            'data_dosen': Dosen.objects.all().order_by('-created_at')
        }
        return render(request, 'admin/dosen.html', data)

def tambah_dosen(request):
    if request.method == 'POST':
        nip = request.POST['nip']
        nama = request.POST['nama']
        pswd = nip
        if Dosen.objects.filter(nip=nip).exists():
            return JsonResponse({'error': 1, 'message': 'NIP Sudah Ada !'})
        else:
            if int(nip) > 0 and len(nip) == 18:
                date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                dosen = Dosen.objects.create(nip=nip, nama=nama, password=pswd, created_at=date, updated_at=date)
                return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Dosen'})
            else:
                return JsonResponse({'error': 2, 'message': 'NIP Harus Berisikan Angka dan Terdiri dari 18 Digit !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')

def ubah_dosen(request):
    if request.method == 'POST':
        nip = request.POST['nip']
        pswd = request.POST['password']

        if pswd not in '':
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            getDosen = Dosen.objects.get(pk=nip)
            getDosen.nama = request.POST['nama']
            getDosen.password = pswd
            getDosen.updated_at = date
            getDosen.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Dosen'})
        else:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            getDosen = Dosen.objects.get(pk=nip)
            getDosen.nama = request.POST['nama']
            getDosen.password = getDosen.password
            getDosen.updated_at = date
            getDosen.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Dosen'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def hapus_dosen(request):
    if request.method == 'POST':
        nip = request.POST['nip']

        getDosen = Dosen.objects.get(pk=nip)

        try:
            getDosen.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Dosen'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Dosen'})

    else:
        return HttpResponse('Hayo ngapain kwkw')
