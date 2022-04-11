
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path(r'books', views.books, name='books'),
]
