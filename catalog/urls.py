
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path(r'books/', views.BookListView.as_view(), name='books'),
    path(r'book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path(r'authors/', views.AuthorListView.as_view(), name='authors'),
    path(r'author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
