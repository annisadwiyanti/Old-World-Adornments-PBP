# Old-World Adornments

### Akses aplikasi pada:
[Old-World Adornments Website](http://annisa-dwiyanti-oldworldadornmentspbp.pbp.cs.ui.ac.id/)

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. **Setup Environment:**
   - Menginstalasi Python dan Django.
   - Menginisiasi Django.
   - Melakukan set up pengaktifan virtual environment.
   - Menambah serta menginstal requirements dan dependencies yang diperlukan dengan `pip install -r requirements.txt`.

2. **Membuat Django Project:**
   - Membuat project baru dengan perintah`django-admin startproject <nama project>`.
   - Membuat Aplikasi: Tambahkan aplikasi dengan perintah `python manage.py startapp main`, yang akan menjadi bagian utama dari proyek

3. **Menyusun Model untuk Aplikasi:**
   - Mendefinisikan `models.py` untuk kebutuhan aplikasi.
     ```
        from django.db import models

        class AdornmentsEntry(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        size = models.CharField(max_length=100)
        color = models.CharField(max_length=100)
        quantity = models.IntegerField()

        @property
        def low_stock(self):
            return self.quantity < 5
     ```
   - Jalankan perintah migrasi agar perubahan masuk ke local database, dengan menggunakan perintah `python manage.py makemigrations` dan `python manage.py migrate`

4. **Membuat Views dan Templates:**
   - Membuat fungsi pada `views.py` untuk menampilkan data.
   - Membuat template pada `main.html` untuk merender tampilan dari aplikasi Django. Template HTML ini digunakan untuk menyajikan data kepada user.

5. **Melakukan konfigurasi URLs:**
   - Menambahkan routing di `urls.py` aplikasi main untuk menghubungkan `view` dengan URL.
     ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
     ```

6. **Deployment:**
   - Menjalankan project Django dengan perintah `python manage.py runserver`
   - Melakukan deployment ke platform Pacil Web Service.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas HTML.

![Bagan Request-Response](bagan.jpeg)

**Penjelasan:**
- **Client Request:** Client menggunakan browser untuk mengirimkan permintaan ke server.
- **urls.py:** File `urls.py` menangani permintaan dengan mencocokkan URL yang diminta dan mengarahkan permintaan tersebut ke view yang sesuai.
- **views.py:** View yang ditunjuk memproses permintaan, mengakses model untuk mendapatkan data bila diperlukan, dan kemudian menyiapkan respons.
- **models.py:** Model mengelola komunikasi dengan database, baik untuk mengambil data yang diperlukan atau menyimpan data baru.
- **HTML Template:** View merender template HTML dengan data yang diperoleh dari model, dan hasilnya dikirim kembali sebagai respons ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git merupakan alat kontrol versi yang digunakan untuk memantau perubahan pada kode sumber selama proses pengembangan perangkat lunak, membuat pengembangan perangkat lunak menjadi lebih terorganisir, efisien, dan kolaboratif
- **Version Control:** Memungkinkan pengembang untuk melacak perubahan dalam kode sumber. Setiap perubahan dicatat, sehingga mudah untuk melihat siapa yang mengubah apa dan kapan.
- **Collaboration:** Memfasilitasi kerja tim dengan memungkinkan banyak pengembang bekerja pada proyek yang sama secara bersamaan tanpa mengganggu pekerjaan satu sama lain. Ini dilakukan melalui fitur branching dan merging
- **Branching dan Merging:** Memungkinkan pengembang untuk bekerja pada fitur atau perbaikan bug secara terpisah dan menggabungkannya kembali ke cabang utama.
- **Backup dan pemulihan:** Menyimpan riwayat lengkap dari semua perubahan, sehingga jika terjadi kesalahan, pengembang dapat dengan mudah kembali ke versi sebelumnya

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

1. **Kemudahan Penggunaan**: Menyediakan banyak fitur bawaan yang memudahkan pengembang pemula untuk memulai tanpa harus membangun semuanya dari awal. Ini membuat proses belajar menjadi lebih cepat dan efisien.

2. **Dokumentasi yang Lengkap**: Memiliki dokumentasi yang sangat baik dan komprehensif, yang sangat membantu bagi pemula untuk memahami konsep-konsep dasar dan mendapatkan panduan langkah demi langkah.

3. **Keamanan**: Memiliki banyak fitur keamanan bawaan yang membantu melindungi aplikasi dari serangan umum seperti SQL injection dan cross-site scripting (XSS). Ini memberikan pemahaman awal tentang pentingnya keamanan dalam pengembangan perangkat lunak.

### 5. Mengapa model pada Django disebut sebagai ORM?

Karena berfungsi sebagai jembatan antara database relasional dan objek dalam kode Python.
- **Abstraksi Database:** ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python alih-alih menulis query SQL secara langsung, membuat kode lebih bersih dan mudah dipahami.
- **Mapping Objek ke Tabel:** Dalam ORM, setiap model Django merepresentasikan tabel dalam database. Setiap atribut model merepresentasikan kolom dalam tabel tersebut. Dengan demikian, ORM memetakan objek Python ke tabel database relasional.
- **Operasi CRUD:** ORM memudahkan operasi Create, Read, Update, dan Delete (CRUD) pada database. Pengembang dapat melakukan operasi ini dengan metode Python yang sederhana tanpa perlu menulis query SQL yang kompleks.