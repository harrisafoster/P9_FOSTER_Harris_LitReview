from django.urls import path
from . import views
from .views import PostListView, PersonalPostListView


urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('flux/', PostListView.as_view(), name='flux'),
    path('my_posts/', PersonalPostListView.as_view(), name='my_posts'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('create_review/', views.create_review, name='create_review'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('ticket/respond/<int:pk>/', views.create_response, name='create_response'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('delete/<int:pk>/delete_ticket/', views.delete_ticket, name='delete_ticket'),
    path('delete/<int:pk>/delete_review/', views.delete_review, name='delete_review'),
    path('delete/<int:pk>/delete_review_and_ticket/', views.delete_review_and_ticket, name='delete_review_and_ticket'),
    # Delete and remake below
]
