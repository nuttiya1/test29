from django.urls import path

from quiz import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('vote/', views.vote, name='vote'),
]
