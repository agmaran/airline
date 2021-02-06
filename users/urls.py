from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # To display information about the currently logged user
    path("login", views.login_view, name="login"), # For logging someone in
    path("logout", views.logout_view, name="logout") # For logging someone out
]