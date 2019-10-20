from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path(r'add_notes/', views.add_notes, name="add_notes"),
    # path(r'/login', views.login, name="login"),
    # path(r'/signup', views.signup, name="signup"),
    # path(r'/logout', views.logout, name="logout"),
    path('addBook/',views.addbook,name='addbook'),
   #path('searchbooks/',views.searchbooks,name='search')
   #path('listbooks/',views.listbooks,name='postsearch')
    #path('deletebooks/')
]
