from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.sign_up, name='signup'),
    path('logout', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('qr/', views.qr, name='qr'),
]
