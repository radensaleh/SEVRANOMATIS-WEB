from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from django.urls import reverse
from apps.models import Dosen, Admin, AmpuMatkul, MataKuliah, Kelas, Soal, DetailSoal, Nilai
from apps.authentication import DosenBackend
from numpy import random


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
                dosen = Dosen.objects.create(
                    nip=nip, nama=nama, password=pswd, created_at=date, updated_at=date)
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

############################ PAGE DOSEN ###################################


def dashboard_dosen(request):
    if 'nip' not in request.session:
        return HttpResponseRedirect(reverse('login-dosen'))
    else:
        nip = request.session.get('nip')

        data = {
            'dosen': Dosen.objects.get(pk=nip),
            'ampu_matkul': AmpuMatkul.objects.filter(nip=nip).count(),
            'soal': Soal.objects.filter(kd_ampu__nip=nip).count()
        }
        return render(request, 'dosen/base_dosen.html', data)


def login_dosen(request):
    if request.method == 'POST':
        dosen = DosenBackend().authenticate(nip=request.POST['nip'],
                                            password=request.POST['password'])
        if dosen is not None:
            akun = Dosen.objects.get(nip=dosen.nip)
            request.session['nip'] = request.POST['nip']
            return HttpResponseRedirect('dashboard')
        else:
            return render(request, 'dosen/login_dosen.html', {'data': 'login failed'})
    else:
        if 'nip' not in request.session:
            return render(request, 'dosen/login_dosen.html')
        else:
            return HttpResponseRedirect(reverse('dashboard-dosen'))


def logout_dosen(request):
    del request.session['nip']
    return HttpResponseRedirect(reverse('login-dosen'))


def pengaturan_dosen(request):
    if request.method == 'POST':
        nip = request.POST['nip']
        nama = request.POST['nama']
        pswd = request.POST['password']

        if pswd not in '':
            getDsn = Dosen.objects.get(pk=nip)
            getDsn.nama = nama
            getDsn.password = pswd
            getDsn.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Data !'})
        else:
            getDsn = Dosen.objects.get(pk=nip)
            getDsn.nama = nama
            getDsn.password = getDsn.password
            getDsn.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Data !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def ampu_dosen(request):
    if 'nip' not in request.session:
        return HttpResponseRedirect(reverse('login-dosen'))
    else:
        nip = request.session.get('nip')
        data = {
            'dosen': Dosen.objects.get(pk=nip),
            'data_ampu': AmpuMatkul.objects.filter(nip=nip).all().order_by('-created_at')
        }
        return render(request, 'dosen/ampu_matkul.html', data)


def soal_dosen(request):
    if 'nip' not in request.session:
        return HttpResponseRedirect(reverse('login-dosen'))
    else:
        nip = request.session.get('nip')
        data = {
            'dosen': Dosen.objects.get(pk=nip),
            'data_soal': Soal.objects.filter(kd_ampu__nip=nip).all().order_by('-created_at'),
            'ampu_matkul': AmpuMatkul.objects.filter(nip=nip).all()
        }
        return render(request, 'dosen/soal.html', data)


def tambah_soal_dosen(request):
    if request.method == 'POST':
        ampu = request.POST['kd_ampu']
        judul = request.POST['judul_soal']

        ran = random.randint(99)
        dm = datetime.now().strftime("%d%m")
        y = datetime.now().strftime("%Y")
        #kd_soal = 'S' + dm + y[:2] + '-' + str(ran)
        kd_soal = 'S' + ampu + '-' + str(ran)

        if Soal.objects.filter(kd_soal=kd_soal).exists():
            return JsonResponse({'error': 1, 'message': 'Soal Sudah Ada !'})
        else:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            soal = Soal.objects.create(
                kd_soal=kd_soal,judul_soal=judul, kd_ampu_id=ampu, created_at=date, updated_at=date)
            return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Soal'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def hapus_soal_dosen(request):
    if request.method == 'POST':
        kd = request.POST['kd_soal']

        getSoal = Soal.objects.get(pk=kd)

        try:
            getSoal.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Soal'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Soal'})

    else:
        return HttpResponse('Hayo ngapain kwkw')


def detail_soal_dosen(request, kd_soal):
    if 'nip' not in request.session:
        return HttpResponseRedirect(reverse('login-dosen'))
    else:
        nip = request.session.get('nip')

        data = {
            'dosen': Dosen.objects.get(pk=nip),
            'kd_soal': kd_soal,
            'detail_soal': DetailSoal.objects.filter(kd_soal=kd_soal).all()
        }
        return render(request, 'dosen/detail_soal.html', data)


def tambah_detailsoal_dosen(request, kd_soal):
    if request.method == 'POST':
        soal = request.POST['soal']
        jawaban1 = request.POST['jawaban1']
        jawaban2 = request.POST['jawaban2']
        jawaban3 = request.POST['jawaban3']
        #bobot = request.POST['bobot']

        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        detailsoal = DetailSoal.objects.create(
            soal=soal, jawaban1=jawaban1, jawaban2=jawaban2, jawaban3=jawaban3, created_at=date, updated_at=date, kd_soal_id=kd_soal)
        return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Soal'})

        # if int(bobot) <= 0 or int(bobot) > 100:
        #     return JsonResponse({'error': 1, 'message': 'Bobot tidak boleh 0, minus atau lebih dari 100'})
        # else:
        #     date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        #     detailsoal = DetailSoal.objects.create(
        #         soal=soal, jawaban=jawaban, bobot=bobot, created_at=date, updated_at=date, kd_soal_id=kd_soal)
        #     return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Soal'})
    else:
        return HttpResponse('Hayo ngapain kwkw')


def hapus_detailsoal_dosen(request, kd_soal):
    if request.method == 'POST':
        kd = request.POST['id']
        print(kd)
        getSoal = DetailSoal.objects.get(pk=kd)

        try:
            getSoal.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Soal'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Soal'})

    else:
        return HttpResponse('Hayo ngapain kwkw')


def nilai_mahasiswa(request):
    if 'nip' not in request.session:
        return HttpResponseRedirect(reverse('login-dosen'))
    else:
        nip = request.session.get('nip')

        data = {
            'dosen': Dosen.objects.get(pk=nip),
            'data_nilai': Nilai.objects.all().order_by('-created_at')
        }
        return render(request, 'dosen/nilai_mahasiswa.html', data)
