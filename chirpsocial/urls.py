from django.urls import path
from .views import dashboard, profile_list, profile
from django.contrib.auth import views as auth_views

app_name = "chirp"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
   # path("dashboard/", dashboard, name="dashboard"),
   path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]