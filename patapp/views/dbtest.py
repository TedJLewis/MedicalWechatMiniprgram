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

def downloadImage(self):
    #image1=image.objects.all()
   # print(image1)
   # image1 = image.objects.values()

   # print(image1.get(id=1))

  #  data = serializers.serialize("json", image1)

    image_list = image.objects.all()
    image1 = image_list.values()
    imagenew1=list(image1)
  #  print(imagenew1)
   # print(image_list)
    pk=[]
    ppk=[]
    j=0

    for h in image_list:
            pk = h.upload_key
            #print(pk)
            img = imagereal.objects.filter(image_id=pk)
            pkimg = []
            for i in img:
                strimg = str(i.img)
                pkimg.append(strimg)
            #print(pkimg)
            imagenew1[j]['img']=pkimg
            j = j + 1
  #  print(imagenew1)
       # print(item)


    #ppkstr = str(ppk)
   # print(ppkstr)




    response=[]
    response.append({
        'image': imagenew1,

    })
    return JsonResponse(data=response, safe=False)

if __name__=='__main__':
    downloadImage()