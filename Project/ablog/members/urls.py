from django.urls import path
from django.views.generic.edit import CreateView
# from . import views
from .views import UserRegisterView, UserEditView, EditProfilePageView, ShowProfilePostsView, ShowProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view()),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(),
         name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(),
         name='edit_profile_page'),
    path('create_profile/', CreateProfilePageView.as_view(),
         name='create_profile_page'),
    path('show_profile_posts/<int:id>/',
         ShowProfilePostsView, name='show_profile_posts')

]
