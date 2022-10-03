from .serializers import *
from django.shortcuts import render
from .models import *


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def home(request):
    return render(request, 'home.html')

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def KrosovkaMakeAPI(request):
    korosvka  = Krosovka.objects.all()
    serializers = KrosovkaAPI(korosvka, many=True)
    return Response(serializers.data)


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializers = KrosovkaAPI(krosovka, many=False)
    return Response(serializers.data)