from django.contrib import admin
from django.urls import path
from fileupload import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name ='index'),
    path('thank',views.thank,name ='thank'),
    path('back',views.index,name ='index'),
    path('check',views.check,name ='check'),
]