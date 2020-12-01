from django.urls import path

from . import views

urlpatterns = [
     path('new_post/', views.NewPost.as_view(), name='new_post'),
     path('<str:username>/', views.profile.as_view(), name='profile'),
     path('<str:username>/follow/', views.profile_follow.as_view(),
          name='profile_follow'),
     path('<str:username>/unfollow/',
          views.profile_unfollow.as_view(), name='profile_unfollow'),
     path('news/', views.news.as_view(), name='news'),
     path('login/', views.login.as_view(), name='login'),
     path('logout/', views.login.as_view(), name='logout')
]
