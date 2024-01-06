from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, AuthorCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('author/create/', AuthorCreateView.as_view(), name='create_author'),

]

