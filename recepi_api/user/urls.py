from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name="user"),
    re_path('users/(?P<pk>[0-9a-f]{10})/', views.UserDetail.as_view(), name="user_details"), ]
