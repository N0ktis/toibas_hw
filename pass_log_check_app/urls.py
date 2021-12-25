from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check/<str:hash_type>/<str:login>/<str:password>', views.check_hash, name='check_hash'),
]