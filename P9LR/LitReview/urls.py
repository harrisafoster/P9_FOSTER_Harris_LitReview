from django.urls import path
from . import views
from .views import PostListView, PersonalPostListView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('flux/', PostListView.as_view(), name='flux'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('create_review/', views.create_review, name='create_review'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('posts/', PersonalPostListView.as_view(), name='posts'),
    path('review/edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('review/remove/<int:pk>/', views.delete_review, name='delete_review'),
    path('ticket/edit/<int:pk>/', UpdatePostView.as_view(), name='edit_ticket'),
    path('ticket/<int:pk>/remove/', DeletePostView.as_view(), name='delete_ticket'),
    path('ticket/respond/<int:pk>/', views.create_response, name='create_response'),
]
