# 📚 Sistem Perpustakaan CRUD Django

Aplikasi web sederhana untuk manajemen perpustakaan dengan fitur Create, Read, Update, dan Delete (CRUD) menggunakan Django.

## 🚀 Fitur Utama

- ✅ **Daftar Buku**: Tampilkan semua buku dalam perpustakaan
- ✅ **Tambah Buku**: Tambahkan buku baru ke perpustakaan
- ✅ **Lihat Detail**: Lihat informasi lengkap tentang setiap buku
- ✅ **Edit Buku**: Ubah informasi buku yang sudah ada
- ✅ **Hapus Buku**: Hapus buku dari perpustakaan
- ✅ **Pencarian**: Cari buku berdasarkan judul atau pengarang
- ✅ **Django Admin**: Kelola buku melalui admin panel Django
- ✅ **UI Responsif**: Antarmuka yang indah menggunakan Bootstrap 5

## 📋 Persyaratan

- Python 3.8+
- Django 4.2.7
- Virtual Environment (venv)

## 🔧 Setup & Instalasi

### 1. Clone atau ekstrak project
```bash
cd c:\PROJECT
```

### 2. Aktifkan Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies (jika belum)
```bash
pip install Django==4.2.7
```

### 4. Jalankan Development Server
```bash
python manage.py runserver
```

Server akan berjalan di `http://127.0.0.1:8000/`

## 📖 Penggunaan

### Aplikasi Web
1. Buka browser dan akses: http://127.0.0.1:8000/
2. Klik "Tambah Buku" untuk menambah buku baru
3. Cari buku menggunakan fitur pencarian
4. Klik "Lihat Detail" untuk melihat informasi lengkap
5. Klik "Edit" untuk mengubah data buku
6. Klik "Hapus" untuk menghapus buku

### Django Admin Panel
1. Akses: http://127.0.0.1:8000/admin/
2. Username: `admin`
3. Password: `admin123`
4. Kelola buku dari admin interface

## 📁 Struktur Project

```
PROJECT/
├── library_project/        # Konfigurasi project
│   ├── __init__.py
│   ├── settings.py         # Pengaturan Django
│   ├── urls.py             # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── books/                  # Aplikasi books
│   ├── migrations/         # Database migrations
│   ├── templates/books/    # Template HTML
│   │   ├── base.html
│   │   ├── book_list.html
│   │   ├── book_detail.html
│   │   ├── book_form.html
│   │   └── book_confirm_delete.html
│   ├── models.py           # Model Book
│   ├── views.py            # Views CRUD
│   ├── forms.py            # Django Forms
│   ├── urls.py             # URL routing app
│   ├── admin.py            # Admin configuration
│   └── apps.py
├── manage.py               # Django management command
├── db.sqlite3              # Database SQLite
├── README.md               # File ini
└── .gitignore              # Git ignore file
```

## 🗄️ Model Database

### Book Model
```python
- title (CharField): Judul buku
- author (CharField): Pengarang
- isbn (CharField): Nomor ISBN (unik)
- publisher (CharField): Nama penerbit
- publication_date (DateField): Tanggal publikasi
- description (TextField): Deskripsi buku
- quantity (IntegerField): Jumlah stok
- created_at (DateTimeField): Tanggal dibuat
- updated_at (DateTimeField): Tanggal diperbarui
```

## 🔗 URL Routes

| URL | Deskripsi |
|-----|-----------|
| `/` | Halaman daftar buku |
| `/book/<id>/` | Halaman detail buku |
| `/book/create/` | Form tambah buku |
| `/book/<id>/update/` | Form edit buku |
| `/book/<id>/delete/` | Konfirmasi hapus buku |
| `/admin/` | Django admin panel |

## 📝 Contoh Data

Anda dapat menambahkan data buku seperti:

| Judul | Pengarang | ISBN | Penerbit |
|-------|-----------|------|----------|
| Harry Potter and the Philosopher's Stone | J.K. Rowling | 9780747532699 | Bloomsbury |
| The Great Gatsby | F. Scott Fitzgerald | 9780743273565 | Scribner |
| To Kill a Mockingbird | Harper Lee | 9780061120084 | HarperCollins |

## 🐛 Troubleshooting

### Migration Error
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files Error
```bash
python manage.py collectstatic
```

### Port sudah digunakan
```bash
python manage.py runserver 8001
```

## 📚 Referensi Dokumentasi

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/4.2/topics/http/views/)
- [Django Forms](https://docs.djangoproject.com/en/4.2/topics/forms/)
- [Bootstrap 5](https://getbootstrap.com/)

## 📄 Lisensi

Project ini bebas digunakan untuk keperluan pembelajaran dan pengembangan.

## 👨‍💻 Author

Dibuat dengan Django oleh GitHub Copilot

---

**Selamat menggunakan Sistem Perpustakaan CRUD Django! 📚✨**
