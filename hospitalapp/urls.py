
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('service/',views.services,name='services' ),
    path('starter/', views.starter,name='starter'),
]
