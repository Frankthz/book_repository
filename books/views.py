from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView

from .filters import BookFilter
from .forms import BookForm, AuthorForm
from .models import Book, Author


class BookListView(FilterView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    filterset_class = BookFilter

    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True).order_by('-publish_date')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('book_list')


def page_not_found(request, exception):
    return render(request, 'Error404.html', status=404)


def error_500(request):
    return render(request, 'Error500.html', status=500)
