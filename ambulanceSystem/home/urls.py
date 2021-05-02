from django.contrib import admin
from django.urls import path
from . import views
from api.views import getMessages, getAmbulances

urlpatterns = [
    path('', views.homepage),
    path('index/', views.homepage),
    path('signUp/', views.signUp),
    path('signIn/', views.signIn),
    path('contact/', views.contactUs),
    path('ambulanceRegister/', views.ambulanceRegister),
    path('search/', views.searchPage),
    path('joinMeeting/', views.joinMeeting),
    path('sendMessage/', views.sendMessage),
    path('logout/', views.signOut),
    path('location/', views.location),
    path('patientUpdate/', views.patientUpdate),
    path('messages/', getMessages),
    path('showAmbulances/', views.showAmbulances),
    path('hospitalAmbulances/', getAmbulances),
    path('doctorSide/', views.doctorSide),
    path('todelete/', views.todelete)
]
