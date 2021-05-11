from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexview, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]