import os
import django
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.db import models
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniprogram.settings')
django.setup()

from patapp.models import doctor


doctor1 = doctor(doctor_id=2)
doctor1.save()