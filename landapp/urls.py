from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('landapp.chatbot.urls')),
    path('account/', include('landapp.accounts.urls')),
]
