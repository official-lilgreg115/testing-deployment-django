from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from.serializer import DataSerializer

# Create your views here.

@api_view(['GET'])
def get_users(resquest):
    users = Data.objects.all()
    serializer = DataSerializer(users)
    return Response(serializer.data)