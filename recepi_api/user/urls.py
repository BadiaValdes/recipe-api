from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name="user"),
    re_path('user/change_password/(?P<pk>[0-9a-f]{32})', views.UserChangePassword.as_view(), name="change_password"),
    re_path('user/change_avatar/(?P<pk>[0-9a-f]{32})', views.UserChangeAvatar.as_view(), name="change_avatar"),
    re_path('user/change_background/(?P<pk>[0-9a-f]{32})', views.UserChangeBackground.as_view(), name="change_background"),
    re_path('users/(?P<pk>[0-9a-f]{32})/', views.UserDetail.as_view(), name="user_details"), ]
    
