from django.urls import path
from . import views

urlpatterns = [
    # all blogs
    path('', views.index, name='index'),
    # searched blogs
    path('bloggers/', views.blogSearch, name='blog-search'),
    # user related blogs
    path('bloggers/dashboard', views.dashboard, name='dashboard'),
    # creating blogs
    path('bloggers/create', views.blogCreate, name='blog-create'),
    # blog Detail
    path('bloggers/<slug:slug>', views.blogDetail, name='blog-detail')
]
