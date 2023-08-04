from django.contrib import admin
from django.urls import path, include
from .views import api_root
from comments import views as comments_views
from posts import views as posts_views
from profiles import views as profiles_views
from likes import views as likes_views
from followers import views as followers_views


urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/posts/', posts_views.PostList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', posts_views.PostDetail.as_view(), name='post-detail'),
    path('api/comments/', comments_views.CommentList.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', comments_views.CommentDetail.as_view(), name='comment-detail'),
    path('api/profiles/', profiles_views.ProfileList.as_view(), name='profile-list'),
    path('api/profiles/<int:pk>/', profiles_views.ProfileDetail.as_view(), name='profile-detail'),
    path('api/likes/', likes_views.LikeList.as_view(), name='like-list'),
    path('api/likes/<int:pk>/', likes_views.LikeDetail.as_view(), name='like-detail'),
    path('api/followers/', followers_views.FollowerList.as_view(), name='follower-list'),
    path('api/followers/<int:pk>/', followers_views.FollowerDetail.as_view(), name='follower-detail'),
]
