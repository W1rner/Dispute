from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.user_page),
    path('edit_profile/', views.user_edit_profile_page, name='edit_profile'),
    path('premium/', views.premium_page, name='premium'),
]
