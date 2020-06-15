from django.contrib import admin
from .models import user
from .models import image
from .models import imagereal
# Register your models here.

admin.site.register(user)
admin.site.register(image)
admin.site.register(imagereal)