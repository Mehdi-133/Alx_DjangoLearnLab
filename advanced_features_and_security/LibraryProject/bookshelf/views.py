from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

# View to create a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        Book.objects.create(title=title, author=author, description=description)
        return render(request, 'book_created.html')
    return render(request, 'create_book.html')

# View to edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return render(request, 'book_edited.html')
    return render(request, 'edit_book.html', {'book': book})

# View to view a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'view_book.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return render(request, 'book_deleted.html')


# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required

# List all books - requiring permission to view
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})


# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def book_search(request):
    search_query = request.GET.get('q', '')  # Safe way to get user input
    books = Book.objects.filter(title__icontains=search_query)  # Django ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})


# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm
from .models import Book

def book_search(request):
    form = ExampleForm(request.GET)
    books = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        books = Book.objects.filter(title__icontains=search_query)

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
