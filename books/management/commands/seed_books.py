from django.core.management.base import BaseCommand
from datetime import date
from books.models import Book


class Command(BaseCommand):
    help = 'Seed database dengan data buku awal'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Hapus data buku yang ada sebelum seeding')

    def handle(self, *args, **options):
        if options.get('clear'):
            Book.objects.all().delete()
            self.stdout.write(self.style.WARNING('Semua data buku lama telah dihapus.'))

        books_data = [
            {
                'title': 'Django untuk Pemula',
                'author': 'Muhammad Rafi',
                'isbn': '9781234567890',
                'publisher': 'Penerbit Indonesia',
                'publication_date': date(2023, 1, 15),
                'description': 'Panduan lengkap belajar Django dari dasar hingga mahir.',
                'quantity': 5,
            },
            {
                'title': 'Python Advanced Programming',
                'author': 'John Doe',
                'isbn': '9781234567891',
                'publisher': 'Tech Press',
                'publication_date': date(2022, 6, 20),
                'description': 'Pelajari teknik programming Python tingkat lanjut.',
                'quantity': 3,
            },
            {
                'title': 'Web Development with Django',
                'author': 'Sarah Johnson',
                'isbn': '9781234567892',
                'publisher': 'Web Academy',
                'publication_date': date(2023, 3, 10),
                'description': 'Membangun aplikasi web modern dengan Django.',
                'quantity': 4,
            },
            {
                'title': 'Database Design Principles',
                'author': 'Robert Smith',
                'isbn': '9781234567893',
                'publisher': 'Data Systems Inc',
                'publication_date': date(2021, 11, 5),
                'description': 'Prinsip-prinsip desain database yang baik.',
                'quantity': 2,
            },
            {
                'title': 'RESTful API Development',
                'author': 'Emily Wilson',
                'isbn': '9781234567894',
                'publisher': 'API Press',
                'publication_date': date(2023, 8, 12),
                'description': 'Membuat API REST yang scalable dan secure.',
                'quantity': 6,
            },
            {
                'title': 'Clean Code Handbook',
                'author': 'Robert C. Martin',
                'isbn': '9781234567895',
                'publisher': 'Code Quality Press',
                'publication_date': date(2020, 9, 1),
                'description': 'Menulis kode yang clean dan maintainable.',
                'quantity': 3,
            },
            {
                'title': 'JavaScript Modern Essentials',
                'author': 'Kyle Simpson',
                'isbn': '9781234567896',
                'publisher': 'JS Academy',
                'publication_date': date(2022, 12, 15),
                'description': 'Fitur-fitur modern JavaScript ES6 dan seterusnya.',
                'quantity': 5,
            },
            {
                'title': 'Software Architecture Patterns',
                'author': 'Mark Richards',
                'isbn': '9781234567897',
                'publisher': 'Architecture Press',
                'publication_date': date(2023, 4, 22),
                'description': 'Pola-pola arsitektur software yang proven.',
                'quantity': 2,
            },
        ]

        created = 0
        for data in books_data:
            obj, created_flag = Book.objects.update_or_create(isbn=data['isbn'], defaults=data)
            if created_flag:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Berhasil membuat/menyegarkan {len(books_data)} data buku (baru: {created}).'))
