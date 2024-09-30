# blog/urls.py
from django.urls import path
from . import views
from .views import contact_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('writing/', views.writing, name='writing'),  # หน้าเขียนบล็อก
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', contact_view, name='contact'),
    path('pythonnew/', views.pythonnew, name='pythonnew'),
    path('e34/', views.e34, name='e34'),
    path('nodenew/', views.node, name='nodenew'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('setting/', views.setting, name='setting'),
    path('', views.none_login, name='noneloginhome'),
    path('write/', views.write_blog, name='write_blog'),
    path('bloglist/', views.blog_list, name='bloglist'),
    path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),




]
