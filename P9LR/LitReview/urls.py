from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('pieces/', views.pieces),
    url(r'^signup/$', views.signup, name='signup'), '''template does not exist?'''
]
