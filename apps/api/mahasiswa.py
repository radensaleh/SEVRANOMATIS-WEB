from django.shortcuts import redirect, render
from apps.models import Mahasiswa, Kelas
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.api.serializer import MhsSerializer
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        mhs = Kelas.objects.all()
        s = MhsSerializer(mhs, many=True)

        response = {
            'data': s.data,
            'code': 0,
        }

        return Response(response)
    else:
        mhs = Kelas.objects.all()
        s = MhsSerializer(mhs, many=True)

        response = {
            'data': s.data,
            'statusCode': 1,
            'message' : 'Yeay'
        }

        return Response(response)

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         mhs = Mahasiswa.objects.all()

#         return JsonResponse({
#             'statusCode' : 0,
#             'message' : 'Success',
#             'data' : mhs
#         })
#     else:
#         mhs = serializers.serialize("json", Kelas.objects.all())
#         aa = Kelas.objects.all()

#         # nim = aa.kd_kelas
#         # nama = aa.kelas
#         # jurusan = aa.created_at

#         data = {}
#         # data['nim'] = nim
#         # data['nama'] = nama
#         # data['jurusan'] = jurusan

#         # response_data = {}
#         # response_data['statusCode'] = 1
#         # response_data['message'] = nim

#         return JsonResponse({
#             'statusCode': 0,
#             'message': 'Success',
#             'data': mhs
#         })
#         #return HttpResponse(response_data)
#         #return HttpResponse(json.dumps(response_data), content_type="application/json")
