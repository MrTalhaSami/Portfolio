from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
   
    path('members/', views.members, name="members"),
    path('members/details/<int:id>', views.details, name='details'),
    path('form/', views.form, name='form'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    

]