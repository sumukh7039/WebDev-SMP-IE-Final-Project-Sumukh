
from django.urls import path
from django.views.generic.list import ListView
# from . import views
from .views import AddPostView, LikeView, UpdatePostView, HomeView, ArticleDetailView, UserPostView, DeletePostView, DislikeView


urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/delete',
         DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('dislike/<int:pk>', DislikeView, name='dislike_post'),
    path('user_profile/', UserPostView.as_view(), name='user_post'),

]
