from .serializers import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.
@api_view(['GET'])
def getall(request):
    bmdata=book_model.objects.all()
    serial=bookmodelSerializer(bmdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        bmid=book_model.objects.get(id=id)
    except book_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookmodelSerializer(bmid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        bmid=book_model.objects.get(id=id)
    except book_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookmodelSerializer(bmid)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        book_model.delete(bmid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(ststua=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=bookmodelSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        bmid=book_model.objects.get(id=id)
    except book_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookmodelSerializer(bmid)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        serial=bookmodelSerializer(data=request.data,instance=bmid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

def index(request):
    url="http://127.0.0.1:8000/getall/?format=json"
    req=requests.get(url)
    data=req.json()
    print(data)
    return render(request,'index.html',{'data':data}) 