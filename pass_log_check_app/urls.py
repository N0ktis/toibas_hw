from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check_raw_url, name='check_raw_url'),
    path('check/<str:hash_type>/<str:login>/<str:password>', views.check_hash, name='check_hash'),
]