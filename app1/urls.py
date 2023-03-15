from app1.views import *
from django.urls import path
app_name='fruits'
urlpatterns=[
    path('tomato/',tomato,name='tomato'),
    path('banana/',banana,name='banana'),
]