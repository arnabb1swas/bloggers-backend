from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_, name='register'),
    path('login', views.login_, name='login'),
    path('logout', views.logout_, name='logout'),

]
