from django.contrib import admin
from django.urls import path

from pages import views

urlpatterns = [
    path('', views.home),
    path('healthz', views.healthz),
    path('admin/', admin.site.urls),
]
