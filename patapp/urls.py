from django.urls import path
from .views import image
urlpatterns=[
    path('', image.getMultImage)
]
