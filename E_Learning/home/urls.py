from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

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

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


