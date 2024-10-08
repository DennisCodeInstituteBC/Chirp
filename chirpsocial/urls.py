from django.urls import path
from .views import dashboard

app_name = "chirp"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]