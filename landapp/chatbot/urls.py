from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chatbot_index'),
    path('ask/', views.ask, name='chatbot_ask'),
]
