from rest_framework import generics , viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    ViewSet to handle CRUD operations for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
