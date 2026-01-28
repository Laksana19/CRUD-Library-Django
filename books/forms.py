from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publisher', 'publication_date', 'description', 'quantity']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Judul Buku'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pengarang'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Penerbit'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Deskripsi Buku'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Jumlah', 'min': '1'}),
        }
