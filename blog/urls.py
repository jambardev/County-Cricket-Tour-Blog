from . import views
from django.urls import path
from .views import about_view

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', about_view, name='about'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]