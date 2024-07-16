from . import views
from django.urls import path
from .views import about_view, delete_post
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', about_view, name='about'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/delete_post/', delete_post, name='delete_post'),
    #path('your-posts/', views.your_posts, name='your_posts'),
]