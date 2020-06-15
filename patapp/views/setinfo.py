from django.http import HttpResponse, Http404, FileResponse, JsonResponse
import os
import hashlib
import json
from django.contrib.auth import authenticate, login
import requests

from django.conf import settings
from patapp.models import user

def setinfo(request):
    openid = request.GET.get("openid")
    gender = request.GET.get("gender")
    mobile = request.GET.get("mobile")
    age = request.GET.get("age")
    first= request.GET.get("first")
    name = request.GET.get("name")
    avatar = request.GET.get("avatar")

    # print(gender)
    # print(mobile)
    # print(age)
    # print(first)
    user1 = user(openid=openid, gender=gender, mobile=mobile, age=age,first_date=first, name= name, avatarimg=avatar, )
    # print(openid)
    # user1 = user(openid=openid)
    # user1.save()
    # print(img.img)
    # if not gender.strip()=='':
    #     user1 = user(openid=openid, gender=gender, )
    #
    # if not mobile.strip()=='':
    #     user1 = user(openid=openid, mobile=mobile, )
    #
    # if not age.strip()=='':
    #     user1 = user(openid=openid, age=age, )
    #
    # if not first.strip()=='':
    #     user1 = user(openid=openid, first_date=first, )


    user1.save()


    response=[]
    response.append({
        'message': "setinfo success!",

    })

    # return HttpResponse('OK')
    return JsonResponse(data=response, safe=False)
