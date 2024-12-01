from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('album/', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/new/', views.album_create, name='album_create'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes Django auth URLs
]
