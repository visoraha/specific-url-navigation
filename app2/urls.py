from app2.views import *
from django.urls import path
app_name='food'
urlpatterns=[
    path('chicken/',chicken,name='chicken'),
    path('muttton/',mutton,name='mutton'),
]