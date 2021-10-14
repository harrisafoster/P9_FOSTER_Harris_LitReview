from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('flux/', views.flux, name='flux'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('create_response/', views.create_response, name='create_response'),
    path('create_review/', views.create_review, name='create_review'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('posts/', views.posts, name='posts'),
    path('edit_ticket/', views.edit_ticket, name='edit_ticket'),
    path('edit_review/', views.edit_review, name='edit_review'),
]
