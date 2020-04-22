from rest_framework import serializers
from apps.models import *

class MhsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__' 