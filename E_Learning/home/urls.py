from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path(r'(?P<user>[\w.@+-]+)/add_notes/', views.add_notes, name="add_notes"),
    # path(r'/login', views.login, name="login"),
    # path(r'/signup', views.signup, name="signup"),
    # path(r'/logout', views.logout, name="logout"),

]
