from django.shortcuts import render, redirect
from apps.forms import AdminForm
from apps.models import Admin, Dosen, Mahasiswa, Kelas, MataKuliah
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from apps.authentication import AdminBackend
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        admin = AdminBackend().authenticate(username=request.POST['username'],
                                            password=request.POST['password'])
        if admin is not None:
            akun = Admin.objects.get(username=admin.username)
            request.session['username'] = request.POST['username']
            return HttpResponseRedirect('dashboard')
        else:
            return render(request, 'admin/login_admin.html', {'data':'login failed'})
    else:
        if 'username' not in request.session:
            return render(request, 'admin/login_admin.html')
        else:
            return HttpResponseRedirect(reverse('dashboard'))

def dashboard(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        username = request.session.get('username')  
        
        data = {
            'admin': Admin.objects.get(pk=username),
            'mahasiswa': Mahasiswa.objects.all().count(),
            'dosen': Dosen.objects.all().count(),
            'kelas': Kelas.objects.all().count(),
            'matkul': MataKuliah.objects.all().count()
        }
        return render(request, 'admin/base_admin.html', data)

def pengaturan(request):
    if request.method == 'POST':
        username = request.POST['username']
        nama = request.POST['nama']
        pswd = request.POST['password']

        if pswd not in '':
            getAdm = Admin.objects.get(pk=username)
            getAdm.nama = nama
            getAdm.password = pswd
            getAdm.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Data !'})
        else:
            getAdm = Admin.objects.get(pk=username)
            getAdm.nama = nama
            getAdm.password = getAdm.password
            getAdm.save()
            return JsonResponse({'error': 0, 'message': 'Berhasil Mengubah Data !'})
    else:
        return HttpResponse('Hayo ngapain kwkw')

def logout(request):
    del request.session['username']
    return HttpResponseRedirect(reverse('login'))
