from django.urls import path,include
from Blog.views import index 
urlpatterns = [
    path('',index),
]