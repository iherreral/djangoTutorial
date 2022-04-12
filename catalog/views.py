from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'my_book_list'  # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='a')[:5]  # Get 5 books containing the title voces
    queryset = Book.objects.all()
    template_name = 'books/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


""" Equivalente if not use generic.DetailView.
def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
"""


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5
    context_object_name = 'my_author_list'  # your own name for the list as a template variable
    queryset = Author.objects.all()
    template_name = 'authors/author_list.html'  # Specify your own template name/location


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html'