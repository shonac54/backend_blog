from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from blog.serializer import RegisterSerializer

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

