# LibraryProject/bookshelf/forms.py
from django import forms

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=255)


from django import forms

class ExampleForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=True, label="Search Query")