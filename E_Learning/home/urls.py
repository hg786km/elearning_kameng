
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from django.views.generic import TemplateView
app_name = "home"

urlpatterns = [
    path(r'add_notes/', views.add_notes, name="add_notes"),
    path(r'view_notes/', views.view_notes, name="view_notes"),
    path(r'add_club/', views.add_club, name="add_club"),
    path('display_clubs/', views.display_clubs, name='display_clubs'),
    path('addbook/',views.addbook,name='addbook'),
    path('displaybook/',views.displaybook,name='displaybook'),
    path('(?P<username>[\w.@+-]+)/(?P<book_title>[\w.@+-]+)/requestbook/',views.requestbook, name='requestbook'),
    path('viewrequests/',views.viewrequests, name='viewrequests'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('course_list/',views.course_list,name='course_list'),
    path('addextcourse/',views.addexternalcourse,name='addextcourse'),
    path('extcourse_list/',views.external_course_list,name='extcourse_list'),
    re_path(r'(?P<coursename>[\w.@+-]+)/(?P<videoname>[\w.@+-]+)/',views.viewcourse),
    path('courses/',TemplateView.as_view(template_name='home/courses.html')),
    path('books/',TemplateView.as_view(template_name='home/books.html')),
    path('notes/',TemplateView.as_view(template_name='home/notes.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




