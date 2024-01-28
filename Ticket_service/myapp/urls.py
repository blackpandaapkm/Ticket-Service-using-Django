from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='home'),
    path('',topics_detail,name='topics_detail'),
    path('',topics_listing,name='topics_listing'),
    path('',contact,name='contact')

]