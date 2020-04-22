from django.shortcuts import render, redirect
# from apps.forms import AdminForm
from apps.models import AmpuMatkul, Dosen, Kelas, MataKuliah, Admin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from datetime import datetime

def data_ampu(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        username = request.session.get('username')
        data = {
            'admin': Admin.objects.get(pk=username),
            'data_dosen' : Dosen.objects.all(),
            'data_matkul': MataKuliah.objects.all(),
            'data_kelas' : Kelas.objects.all(),
            'data_ampu'  : AmpuMatkul.objects.all().order_by('-created_at')
        }
        return render(request, 'admin/ampu_matkul.html', data)

def tambah_ampu(request):
    if request.method == 'POST':
        kd_ampu = request.POST['kd_ampu']
        nip = request.POST['nip']
        kd_kelas = request.POST['kd_kelas']
        kd_mk = request.POST['kd_mk']
        smstr = request.POST['semester']

        if AmpuMatkul.objects.filter(kd_ampu=kd_ampu).exists():
            return JsonResponse({'error': 1, 'message': 'Kode Ampu Sudah Ada !'})
        else:
            if len(kd_ampu) > 0 and len(kd_ampu) <= 10:
                if int(smstr) > 0 and len(smstr) == 1:
                    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    ampu = AmpuMatkul.objects.create(
                        kd_ampu=kd_ampu, nip_id=nip, kd_kelas_id=kd_kelas, kd_mk_id=kd_mk,
                        semester=smstr, created_at=date, updated_at=date)

                    return JsonResponse({'error': 0, 'message': 'Berhasil Menambahkan Dosen Pengampu'})
                else:
                    return JsonResponse({'error': 3, 'message': 'Semester Hanya Berisi 1 - 9 !'})
            else:
                return JsonResponse({'error': 2, 'message': 'Kode Ampu Harus Terdiri dari 1 - 10 Digit !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')

def ubah_ampu(request):
    if request.method == 'POST':
        kd_ampu = request.POST['kd_ampu']
        nip = request.POST['nip']
        kd_kelas = request.POST['kd_kelas']
        kd_mk = request.POST['kd_mk']
        smstr = request.POST['semester']
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if int(smstr) > 0 and len(smstr) == 1:
            getAmpu = AmpuMatkul.objects.get(pk=kd_ampu)
            getAmpu.nip_id = nip
            getAmpu.kd_kelas_id = kd_kelas
            getAmpu.kd_mk_id = kd_mk
            getAmpu.semester = smstr
            getAmpu.updated_at = date
            getAmpu.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Dosen Pengampu !'})
        else:
            return JsonResponse({'error': 1, 'message': 'Semester Hanya Berisi 1 - 9 !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')

def hapus_ampu(request):
    if request.method == 'POST':
        kd_ampu = request.POST['kd_ampu']

        getAmpu = AmpuMatkul.objects.get(pk=kd_ampu)

        try:
            getAmpu.delete()
            return JsonResponse({'error': 0, 'message': 'Berhasil Menghapus Dosen Pengampu'})
        except Exception as e:
            return JsonResponse({'error': 1, 'message': 'Gagal Menghapus Dosen Pengampu'})

    else:
        return HttpResponse('Hayo ngapain kwkw')
