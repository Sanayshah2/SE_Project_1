from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('test', views.test, name='test'),
  path('home', views.home, name='home'),
  path('login', views.login, name='login'),
  path('signup', views.signup, name='signup'),
  path('find_roommate', views.find_roommates, name='find_roommate')
]