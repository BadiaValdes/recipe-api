from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name="user"),
    path('user/create', views.CreateUser.as_view(), name="user_create"),
    re_path('user/change_password/(?P<pk>[0-9a-f]{32})', views.UserChangePassword.as_view(), name="change_password"),
    re_path('user/change_avatar/(?P<pk>[0-9a-f]{32})', views.UserChangeAvatar.as_view(), name="change_avatar"),
    re_path('user/change_background/(?P<pk>[0-9a-f]{32})', views.UserChangeBackground.as_view(),
            name="change_background"),
    re_path('user/admin_info/(?P<pk>[0-9a-f]{32})', views.UserDatailAdmin.as_view(),
            name="change_admin_info"),
    # path('user/', views.UserDetail.as_view(), name="user_details2"),
    # path('users/<username>/', views.UserDetail.as_view(), name="user_details"),
    re_path('users/(?P<pk>[0-9a-f]{32})/', views.UserDetail.as_view(), name="user_details"),
    path('user/<username>/', views.UserDetailByUsername.as_view(), name="user_details_by_name"),
]
