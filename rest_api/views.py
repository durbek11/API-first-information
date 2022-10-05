from .serializers import *
from django.shortcuts import render
from .models import *


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def home(request):
    return render(request, 'home.html')

# API to`liq chiqarish`
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def KrosovkaMakeAPI(request):
    korosvka  = Krosovka.objects.all()
    serializers = KrosovkaAPI(korosvka, many=True)
    return Response(serializers.data)

# Api ni ID orqali chiqarish(alohida alohida qilib chiqarish)
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializers = KrosovkaAPI(krosovka, many=False)
    return Response(serializers.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singlePAivewewe(request):
    cars  = Cars.objects.all()
    serializers = CarsAPI(cars, many=True)
    return Response(serializers.data)


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleApai(request, pk):
    mobile = Cars.objects.get(id=pk)
    serializers = CarsAPI(mobile, many=False)
    return Response(serializers.data)

# post joylash, (malumot joylash)
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotJoylash(request,):
    serializers = KrosovkaAPI(data=request.data)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)

# POST update, (malumot taxrirlash)
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotUpdate(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializers = KrosovkaAPI(instance=krosovka, data=request.data)
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)

# POST delete, (malumptlarni ochirish)
@api_view(["DELETE"])
@permission_classes((permissions.AllowAny, ))
def malumotDelete(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    krosovka.delete()

    return Response("malumot o`chirildi")