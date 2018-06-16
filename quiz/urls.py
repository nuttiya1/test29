from django.urls import path
from django.contrib import admin

from quiz import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('vote', views.vote, name='vote'),
    path('admin/', admin.site.urls),
]
