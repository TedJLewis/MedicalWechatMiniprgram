from django.http import HttpResponse, Http404, FileResponse, JsonResponse
import os
import hashlib
import json
from django.contrib.auth import authenticate, login
import requests
from patapp.models import user
from django.conf import settings



def login(request):
    response = []
    code = request.GET.get("code")
    url = "https://api.weixin.qq.com/sns/jscode2session"
    appid = 'wxac2341f794fa01a0'
    secret = '5761fb4e7a19827e830017aa2ebe8da0'
    url = url + "?appid=" + appid + "&secret=" + secret + "&js_code=" + code + "&grant_type=authorization_code"
    wechatBack=requests.get(url).json()
    openid=wechatBack['openid']
    sessionkey=wechatBack['session_key']

    response.append({
        'code': code,
        'openid': openid,
        'sessionkey':sessionkey,
    })
    newuser = user.objects.filter(openid=openid)
    if newuser.exists():
        print("openid exists")
    else:
        user1 = user(openid=openid)
        user1.save()

    return JsonResponse(data=response, safe=False)



