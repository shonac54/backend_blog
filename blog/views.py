from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from blog.serializer import RegisterSerializer,BlogSerializer
from blog.models import BlogModel
from django.db.models import Q

# Create your views here.
@csrf_exempt
def userRegister(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serialized_data = RegisterSerializer(data =recieved_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
        
@csrf_exempt
def userBlog(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serializer_check = BlogSerializer(data = recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))

@csrf_exempt
def viewBlog(request):
    if request.method == "POST":
            blogList=BlogModel.objects.all()
            serialize_data=BlogSerializer(blogList,many=True)
            
            return HttpResponse(json.dumps(serialize_data.data))

