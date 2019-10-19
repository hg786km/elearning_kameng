from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path(r'', views.dashboard, name="dashboard"),
    path(r'/login', views.login, name="login"),
    path(r'/signup', views.signup, name="signup"),
    path(r'/logout', views.logout, name="logout"),

]
