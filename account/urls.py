from django.contrib import admin
from django.urls import path, include
from login.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', HomeView.as_view(), name='home'), 
]
