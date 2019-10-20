from django.urls import path, re_path
from . import views

app_name = "home"

urlpatterns = [
    path(r'add_notes/', views.add_notes, name="add_notes"),

    path(r'view_notes/', views.view_notes, name="view_notes"),

    # path(r'/login', views.login, name="login"),

    # path(r'/signup', views.signup, name="signup"),
    # path(r'/logout', views.logout, name="logout"),
    path('addBook/',views.addbook,name='addbook'),
   #path('searchbooks/',views.searchbooks,name='search')
   #path('listbooks/',views.listbooks,name='postsearch')
    #path('deletebooks/')
    path('addcourse/',views.addcourse,name='addcourse'),
    path('course_list/',views.course_list,name='course_list'),
    path('addextcourse/',views.addexternalcourse,name='addextcourse'),
    path('extcourse_list/',views.external_course_list,name='extcourse_list'),
    re_path(r'(?P<coursename>[\w.@+-]+)/(?P<videoname>[\w.@+-]+)/',views.viewcourse)

]


