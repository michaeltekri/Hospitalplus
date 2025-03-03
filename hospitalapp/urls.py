
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('service/',views.services,name='service' ),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.service,name='services'),
    path('doctors/', views.doctor,name='doctors'),
    path('services/', views.service,name='services'),
    path('department/', views.dep,name='department'),
    path('appointment/', views.appoints,name='appointment'),
    path('contact/', views.con,name='contact'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),

]
