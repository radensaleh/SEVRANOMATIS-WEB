from apps.models import Admin, Dosen, Mahasiswa
from django.contrib.auth.models import User


class AdminBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            admin = Admin.objects.get(username=username)
            if Admin.objects.get(password=password):
                return admin
            return None
        except Admin.DoesNotExist:
            return None

    def get_admin(self, username):
        try:
            return Admin.objects.get(pk=username)
        except Admin.DoesNotExist:
            return None

class DosenBackend(object):
    def authenticate(self, nip=None, password=None):
        try:
            dosen = Dosen.objects.get(nip=nip)
            if Dosen.objects.get(password=password):
                return dosen
            return None
        except Dosen.DoesNotExist:
            return None
    
    def get_dosen(self, nip):
        try:
            return Dosen.objects.get(pk=nip)
        except Dosen.DoesNotExist:
            return None


class MahasiswaBackend(object):
    def authenticate(self, nim=None, password=None):
        try:
            mhs = Mahasiswa.objects.get(nim=nim)
            if Mahasiswa.objects.get(password=password):
                return mhs
            return None
        except Mahasiswa.DoesNotExist:
            return None

    def get_mhs(self, nim):
        try:
            return Mahasiswa.objects.get(pk=nim)
        except Mahasiswa.DoesNotExist:
            return None
