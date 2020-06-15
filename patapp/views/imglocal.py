import os
import django
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.db import models
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniprogram.settings')
django.setup()

from patapp.models import user
from patapp.models import image
from patapp.models import imagereal

def localImg():

    image_list = imagereal.objects.all()
    id = 13
    for h in image_list:
        img1=h.img
        img2=str(img1)
        imglocal='file:///D:/workspace/PythonProject/miniprogram/miniprogram-1/'+img2

        image1 = imagereal(id=id,imglocal=imglocal)
        image1.save()
        id=id+1

        # img = imagereal.objects.filter(image_id=pk)
        # pkimg = []
        # for i in img:
        #     strimg = str(i.img)
        #     pkimg.append(strimg)





if __name__=='__main__':
    localImg()