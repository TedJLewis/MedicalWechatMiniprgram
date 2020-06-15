from django.http import HttpResponse, Http404, FileResponse, JsonResponse
import os
import hashlib
import json
from django.contrib.auth import authenticate, login
import requests

from django.conf import settings
from patapp.models import user

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniprogram.settings')
# django.setup()


from patapp.models import image
from patapp.models import imagereal

def initinfopage(request):
    openid= request.GET.get("openid")
    user1= user.objects.filter(openid=openid)
    #user1 = user.objects.all()
    a=user1.values()
    usernew = list(a)
    print(usernew)
    response=[]
    response.append({
        'user':usernew
    })

    return JsonResponse(data=response, safe=False)



