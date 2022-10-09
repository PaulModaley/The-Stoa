from django.contrib import admin
from django.urls import path, include
from stoicblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stoicblog.urls')),
    path('accounts/', include('allauth.urls')),
]
