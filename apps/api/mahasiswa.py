from django.shortcuts import redirect, render
from apps.models import Mahasiswa, Kelas, AmpuMatkul, Soal, DetailSoal, Nilai
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.api.serializer import MahasiswaSerializer, AmpuMatkulSerializer
from rest_framework.decorators import api_view
from apps.authentication import MahasiswaBackend
from django.forms.models import model_to_dict
from apps.api.essay_scoring import scoring
import math
from numpy import random

@csrf_exempt
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        response = {
            'statusCode': 1,
            'message': 'Method Not Allowed!'
        }

        return Response(response)
    else:
        #mhs = Kelas.objects.all()
        #s = MhsSerializer(mhs, many=True)

        mhs = MahasiswaBackend().authenticate(nim=request.POST['nim'],
                                              password=request.POST['password'])
        if mhs is not None:
            akun = Mahasiswa.objects.get(nim=mhs.nim)

            data = {
                'nim': akun.nim,
                'nama': akun.nama,
                'jurusan': akun.jurusan,
                'prodi': akun.prodi,
                'kd_kelas': akun.kd_kelas_id,
                'kelas': akun.kd_kelas.kelas
            }

            return JsonResponse({
                'statusCode': 0,
                'message': 'Login Berhasil!',
                'data': [data]
            })

        else:
            return JsonResponse({
                'statusCode': 1,
                'message': 'NIM atau Password Salah!',
                'data': []
            })


@csrf_exempt
@api_view(['GET', 'POST'])
def profile(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        try:
            akun = Mahasiswa.objects.get(nim=request.POST['nim'])

            data = {
                'nim': akun.nim,
                'nama': akun.nama,
                'jurusan': akun.jurusan,
                'prodi': akun.prodi,
                'kd_kelas': akun.kd_kelas_id,
                'kelas': akun.kd_kelas.kelas
            }
            return JsonResponse({
                'statusCode': 0,
                'message': 'Success!',
                'data': [data]
            })
        except Exception as e:
            return JsonResponse({
                'statusCode': 1,
                'message': 'Failed!',
                'data': []
            })


@csrf_exempt
@api_view(['GET', 'POST'])
def matkul(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        # data = [model_to_dict(instance)
        #         for instance in AmpuMatkul.objects.filter(kd_kelas=request.POST['kd_kelas']).order_by('-created_at')]

        data = AmpuMatkul.objects.filter(
            kd_kelas=request.POST['kd_kelas']).order_by('-created_at')

        ampu_dict = {}
        ampu_record = []

        for ampu in data:
            record = {
                "kd_ampu": ampu.kd_ampu,
                "nip": ampu.nip.nip,
                "nama_dosen": ampu.nip.nama,
                "kd_mk": ampu.kd_mk.kd_mk,
                "matkul": ampu.kd_mk.mata_kuliah,
                "kd_kelas": ampu.kd_kelas.kd_kelas,
                "kelas": ampu.kd_kelas.kelas,
                "sks": ampu.kd_mk.sks,
                "semester": ampu.semester

            }
            ampu_record.append(record)

        ampu_dict["statusCode"] = 0
        ampu_dict["message"] = 'Success!'
        ampu_dict["data"] = ampu_record

        return JsonResponse(ampu_dict)


@csrf_exempt
@api_view(['GET', 'POST'])
def soal(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        data = Soal.objects.filter(
            kd_ampu__kd_kelas=request.POST['kd_kelas']).order_by('-created_at')

        soal_dict = {}
        soal_record = []

        for soal in data:
            record = {
                'kd_soal': soal.kd_soal,
                'judul_soal': soal.judul_soal,
                'kd_ampu': soal.kd_ampu.kd_ampu,
                'nip': soal.kd_ampu.nip.nip,
                'nama_dosen': soal.kd_ampu.nip.nama,
                'kd_mk': soal.kd_ampu.kd_mk.kd_mk,
                'matkul': soal.kd_ampu.kd_mk.mata_kuliah,
                'kelas': soal.kd_ampu.kd_kelas.kelas,
                'sks': soal.kd_ampu.kd_mk.sks,
                'semester': soal.kd_ampu.semester
            }
            soal_record.append(record)

        soal_dict['statusCode'] = 0
        soal_dict['message'] = 'Success!'
        soal_dict['data'] = soal_record

        return JsonResponse(soal_dict)


@csrf_exempt
@api_view(['GET', 'POST'])
def detail_soal(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        data = DetailSoal.objects.filter(
            kd_soal=request.POST['kd_soal']).order_by('-created_at')

        if(len(data) == 0):
            soal_dict = {}

            data = Soal.objects.filter(kd_soal=request.POST['kd_soal']).order_by('-created_at')
            
            data_dict = {
                'kd_soal': data[0].kd_soal,
                'judul_soal': data[0].judul_soal,
                'kd_ampu': data[0].kd_ampu.kd_ampu,
                'nip': data[0].kd_ampu.nip.nip,
                'nama_dosen': data[0].kd_ampu.nip.nama,
                'kd_mk': data[0].kd_ampu.kd_mk.kd_mk,
                'matkul': data[0].kd_ampu.kd_mk.mata_kuliah,
                'kelas': data[0].kd_ampu.kd_kelas.kelas,
                'sks': data[0].kd_ampu.kd_mk.sks,
                'semester': data[0].kd_ampu.semester
            }

            soal_dict['statusCode'] = 0
            soal_dict['message'] = 'Success!'
            soal_dict['data'] = [data_dict]
            soal_dict['data_soal'] = []

            return JsonResponse(soal_dict)
        else:
            soal_dict = {}
            soal_record = []

            data_dict = {
                'kd_soal': data[0].kd_soal.kd_soal,
                'judul_soal': data[0].kd_soal.judul_soal,
                'kd_ampu': data[0].kd_soal.kd_ampu.kd_ampu,
                'nip': data[0].kd_soal.kd_ampu.nip.nip,
                'nama_dosen': data[0].kd_soal.kd_ampu.nip.nama,
                'kd_mk': data[0].kd_soal.kd_ampu.kd_mk.kd_mk,
                'matkul': data[0].kd_soal.kd_ampu.kd_mk.mata_kuliah,
                'kelas': data[0].kd_soal.kd_ampu.kd_kelas.kelas,
                'sks': data[0].kd_soal.kd_ampu.kd_mk.sks,
                'semester': data[0].kd_soal.kd_ampu.semester
            }

            for detail_soal in data:
                record = {
                    'nomer': detail_soal.id,
                    'soal': detail_soal.soal,
                }
                soal_record.append(record)

            soal_dict['statusCode'] = 0
            soal_dict['message'] = 'Success!'
            soal_dict['data'] = [data_dict]
            soal_dict['data_soal'] = soal_record

            return JsonResponse(soal_dict)
        



@csrf_exempt
@api_view(['GET', 'POST'])
def soal_proccess(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        nomer = request.POST.getlist('nomer[]')
        jawaban = request.POST.getlist('jawaban[]')
        kd_soal = request.POST['kd_soal']
        nim = request.POST['nim']

        j = 0
        nilai = 0
        data_dict = {}

        data_record = []
        data_score = []

        for i in nomer:
            getKey = DetailSoal.objects.filter(id=int(i))
            key1 = getKey[0].jawaban1
            key2 = getKey[0].jawaban2
            key3 = getKey[0].jawaban3

            result1 = scoring([key1], [jawaban[j]])
            result2 = scoring([key2], [jawaban[j]])
            result3 = scoring([key3], [jawaban[j]])

            allResult = [result1, result2, result3]
            maxResult = max(allResult)

            keys = {
                'no': int(i),
                'key1': getKey[0].jawaban1,
                'key2': getKey[0].jawaban2,
                'key3': getKey[0].jawaban3,
                'answer': jawaban[j],
                'result1': result1,
                'result2': result2,
                'result3': result3,
                'score_final': math.ceil(maxResult)
            }

            j += 1
            data_record.append(keys)
            data_score.append(math.ceil(maxResult))

        ifExist, final, index = insert_score(kd_soal, nim, data_score)

        if(ifExist):
            data_dict['statusCode'] = 0
            data_dict['message'] = 'Success!'
            #data_dict['data'] = data_record
            data_dict['data'] = [{'score': final, 'index': index}]

            return JsonResponse(data_dict)
        else:
            data_dict['statusCode'] = 1
            data_dict['message'] = 'Anda Sudah Mengerjakan soal ini!'
            #data_dict['data'] = data_record
            data_dict['data'] = []

            return JsonResponse(data_dict)


def insert_score(kd_soal, nim, data_score):
    score = 0
    for i in range(len(data_score)):
        score += data_score[i]

    final = math.ceil(score/len(data_score))

    index = ''
    if final >= 50 and final < 60:
        index = 'C'
    elif final >= 60 and final < 70:
        index = 'BC'
    elif final >= 70 and final < 80:
        index = 'B'
    elif final >= 80 and final < 90:
        index = 'AB'
    elif final >= 90 and final <= 100:
        index = 'A'
    elif final > 100:
        index = 'A'
    else:
        index = 'E'

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    ran = random.randint(999999)
    twoDigits = nim[5:]
    kd_nilai = 'N' + str(ran) + '-' + twoDigits

    cekIfExist = Nilai.objects.filter(nim=nim).filter(kd_soal=kd_soal).count()
    if cekIfExist == 0:
        Nilai.objects.create(kd_nilai=kd_nilai, kd_soal_id=kd_soal, nim_id=nim,
                             nilai=final, index=index, created_at=date, updated_at=date)
        return True, final, index
    else:
        return False, final, index


@csrf_exempt
@api_view(['GET', 'POST'])
def ranking(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        kd_soal = request.POST['kd_soal']
        data = Nilai.objects.filter(kd_soal=kd_soal).order_by('-nilai')

        nilai_dict = {}
        nilai_record = []

        for nilai in data:
            record = {
                'nim': nilai.nim.nim,
                'nama': nilai.nim.nama,
                'nilai': nilai.nilai,
                'index': nilai.index,
                'tgl_selesai': nilai.created_at
            }

            nilai_record.append(record)

        nilai_dict['statusCode'] = 0
        nilai_dict['message'] = 'Success!'
        nilai_dict['data'] = nilai_record

        return JsonResponse(nilai_dict)


@csrf_exempt
@api_view(['GET', 'POST'])
def nilai(request):
    if request.method == 'GET':
        return JsonResponse({
            'statusCode': 1,
            'message': 'Method Not Allowed!',
        })
    else:
        nim = request.POST['nim']
        data = Nilai.objects.filter(nim=nim).order_by('-created_at')

        nilai_dict = {}
        nilai_record = []

        for nilai in data:
            record = {
                'kd_nilai': nilai.kd_nilai,
                'kd_soal': nilai.kd_soal.kd_soal,
                'judul_soal': nilai.kd_soal.judul_soal,
                'kd_ampu': nilai.kd_soal.kd_ampu.kd_ampu,
                'nip': nilai.kd_soal.kd_ampu.nip.nip,
                'nama_dosen': nilai.kd_soal.kd_ampu.nip.nama,
                'kd_mk': nilai.kd_soal.kd_ampu.kd_mk.kd_mk,
                'matkul': nilai.kd_soal.kd_ampu.kd_mk.mata_kuliah,
                'kelas': nilai.kd_soal.kd_ampu.kd_kelas.kelas,
                'sks': nilai.kd_soal.kd_ampu.kd_mk.sks,
                'semester': nilai.kd_soal.kd_ampu.semester,
                'nilai': nilai.nilai,
                'index': nilai.index
            }

            nilai_record.append(record)

        nilai_dict['statusCode'] = 0
        nilai_dict['message'] = 'Success!'
        nilai_dict['data'] = nilai_record

        return JsonResponse(nilai_dict)
