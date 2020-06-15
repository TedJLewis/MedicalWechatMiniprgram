import os
import django
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.db import models
from django.core import serializers
from patapp.models import user
from patapp.models import image
from patapp.models import imagereal
import requests

def reply(request):
    #image1=image.objects.all()
   # print(image1)
   # image1 = image.objects.values()

   # print(image1.get(id=1))

  #  data = serializers.serialize("json", image1)
    id = request.GET.get("id")

    image1 = image.objects.filter(upload_key=id)
    # user1 = user.objects.all()
    a = image1.values()
    usernew = list(a)
    print(usernew)
    response = []
    response.append({
        'user': usernew
    })

    return JsonResponse(data=response, safe=False)
