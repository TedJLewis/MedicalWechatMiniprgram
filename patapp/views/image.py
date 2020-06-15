from django.http import HttpResponse, Http404, FileResponse, JsonResponse
import os
import hashlib
from patapp.models import user
from patapp.models import image
from patapp.models import imagereal
from django.utils import timezone

def getImage(request):

   if request.method=='POST':
       image=request.FILES['image']
       print(image)
       open_id=request.POST.get('openid')
     #  md5=request.GET.get('md5')
       basedir= 'D:\workspace\PythonProject\djangotest'
       path= 'D:\\workspace\\PythonProject\\miniprogram\\static\\userimg'
       if not os.path.exists(path+open_id+'.jpg'):
           with open(path+open_id+'.jpg','wb') as f:
               f.write(image.read())
               f.close()

def getMultImage(request):
    files = request.FILES
    response = []
    text = request.POST.get("text")
    print("text: " + text)
   # print(files)


    for key, value in files.items():
        content = value.read()
        md5 = hashlib.md5(content).hexdigest()
       # text = request.body.test
        openid = request.POST.get("openid")
        print("openid: " + openid)



        linuxpath = '/home/djangotest/static/userimg/'
        winpath='D:\\workspace\\PythonProject\\miniprogram\\static\\userimg\\'
        path= os.path.join(winpath, md5 + ".jpg")
        with open(winpath+ md5+ '.jpg', 'wb') as f:
            f.write(content)
        picpath= winpath+ md5+ '.jpg'

       # response = self.wrap_json_response(data=response, code=ReturnCode.SUCCESS, message=message)
        response.append({
            'name': key,
            'md5': md5,
          #  'text': text
        })
        message = 'POST method success.'
        create_time = timezone.now()
        d1 = create_time.strftime("%Y-%m-%d %H:%M")
        pk = create_time.strftime("%Y%m%d%H%M%S")
        user1 = user.objects.get(openid=openid)
        image1 = image(upload_key=pk, text=text, user=user1, upload_time=d1)
        image1.save()
        imagereal1 =imagereal(image=image1, img=request.FILES.get("image"))
        imagereal1.save()


       # response = self.wrap_json_response(data=response, code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)


