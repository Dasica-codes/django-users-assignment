from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('new_user/', views.new_user, name='new_user'),
    path('<int:id>/', views.user_detail, name='user_detail'),
    path('', views.users_list, name='users_list'),
]