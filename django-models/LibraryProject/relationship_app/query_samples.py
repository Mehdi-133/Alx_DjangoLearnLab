from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"


def list_all_books_in_library(library_name):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"


def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian of a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian found for the library {library_name}"


# Example usage
if __name__ == "__main__":
    # Replace these with actual values in your database
    print(query_all_books_by_author("J.K. Rowling"))
    print(list_all_books_in_library("Central Library"))
    print(retrieve_librarian_for_library("Central Library"))
