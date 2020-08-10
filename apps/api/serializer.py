from rest_framework import serializers
from apps.models import *

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = '__all__' 


class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'


class MataKuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataKuliah
        fields = '__all__'


class DosenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosen
        fields = '__all__'

class AmpuMatkulSerializer(serializers.ModelSerializer):
    kelas = KelasSerializer(read_only=True,many=True)
    class Meta:
        model = AmpuMatkul
        fields = '__all__'
