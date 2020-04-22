from django import forms
from .models import Admin, Dosen, MataKuliah, Kelas, AmpuMatkul, \
    Soal, DetailSoal, Nilai


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('username', 'password')
        label = {
            'username': 'Username',
            'password': 'Password'
        }


class DosenForm(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = ('nip', 'nama', 'password')
        labels = {
            'nip': 'NIP',
            'nama': 'Nama Lengkap',
            'password': 'Password'
        }
