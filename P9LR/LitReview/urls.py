from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('flux/', views.flux, name='flux'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
