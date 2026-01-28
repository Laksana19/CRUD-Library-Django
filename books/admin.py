from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publisher', 'quantity', 'created_at')
    list_filter = ('author', 'publisher', 'created_at')
    search_fields = ('title', 'author', 'isbn')
    ordering = ('-created_at',)
