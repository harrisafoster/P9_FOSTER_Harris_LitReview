from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile),
    path('flux/', views.flux, name='flux'),
    url(r'^signup/$', views.signup, name='signup'),
]
