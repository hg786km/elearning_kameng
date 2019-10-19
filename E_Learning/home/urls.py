from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path(r'add_notes/', views.add_notes, name="add_notes"),
    path(r'view_notes/', views.view_notes, name="view_notes"),
    # path(r'/signup', views.signup, name="signup"),
    # path(r'/logout', views.logout, name="logout"),

]


