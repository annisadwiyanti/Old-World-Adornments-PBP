# Old-World Adornments

### Akses aplikasi pada link berikut👇🏻
[Old-World Adornments Website](http://annisa-dwiyanti-oldworldadornmentspbp.pbp.cs.ui.ac.id/)

## Tugas 2
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

- **Kemudahan Penggunaan**: Menyediakan banyak fitur bawaan yang memudahkan pengembang pemula untuk memulai tanpa harus membangun semuanya dari awal. Ini membuat proses belajar menjadi lebih cepat dan efisien.
- **Dokumentasi yang Lengkap**: Memiliki dokumentasi yang sangat baik dan komprehensif, yang sangat membantu bagi pemula untuk memahami konsep-konsep dasar dan mendapatkan panduan langkah demi langkah.
- **Keamanan**: Memiliki banyak fitur keamanan bawaan yang membantu melindungi aplikasi dari serangan umum seperti SQL injection dan cross-site scripting (XSS). Ini memberikan pemahaman awal tentang pentingnya keamanan dalam pengembangan perangkat lunak.

### 5. Mengapa model pada Django disebut sebagai ORM?

Karena berfungsi sebagai jembatan antara database relasional dan objek dalam kode Python.
- **Abstraksi Database:** ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python alih-alih menulis query SQL secara langsung, membuat kode lebih bersih dan mudah dipahami.
- **Mapping Objek ke Tabel:** Dalam ORM, setiap model Django merepresentasikan tabel dalam database. Setiap atribut model merepresentasikan kolom dalam tabel tersebut. Dengan demikian, ORM memetakan objek Python ke tabel database relasional.
- **Operasi CRUD:** ORM memudahkan operasi Create, Read, Update, dan Delete (CRUD) pada database. Pengembang dapat melakukan operasi ini dengan metode Python yang sederhana tanpa perlu menulis query SQL yang kompleks.


## Tugas 3
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian sebuah platform karena memungkinkan transfer data atau komunikasi anatara server dan klien ataupun antara berbagai komponen sistem, aplikasi, atau layanan. Ini memastikan bahwa data yang dibutuhkan tersedia di tempat yang tepat dan waktu yang tepat, memungkinkan integrasi yang lancar dan operasional yang efisien. Tanpa data delivery yang efektif, platform mungkin mengalami keterlambatan, kehilangan data, atau ketidakcocokan data, yang dapat menghambat fungsionalitas dan kinerja keseluruhan.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Kedua format, XML dan JSON, memiliki kelebihan dan kekurangannya masing-masing,
- Kelebihan XML: Mendukung skema yang kompleks, validasi data, dan namespace.
- Kekurangan XML: Lebih verbose, lebih sulit dibaca manusia, dan parsing yang lebih lambat.
- Kelebihan JSON: Lebih ringan, lebih mudah dibaca manusia, dan parsing yang lebih cepat.
- Kekurangan JSON: Kurang mendukung skema yang kompleks dan validasi data.

JSON dianggap lebih baik dibandingkan XML karena kesederhanaannya dan efisiensinya dalam pengiriman data, terutama dalam aplikasi web dan API. JSON lebih mudah dibaca dan ditulis oleh manusia, serta lebih cepat diproses oleh mesin, menjadikannya pilihan yang lebih praktis dalam aplikasi web.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua persyaratan validasi yang telah didefinisikan, seperti tipe data yang benar, panjang karakter, atau pola tertentu. Method ini mengembalikan nilai boolean `True` atau `False`. Jika `is_valid()` mengembalikan `True`, data form dianggap valid dan dapat diproses lebih lanjut. Jika `False`, form akan mengandung pesan kesalahan yang menjelaskan mengapa data tidak valid. Method ini penting untuk memastikan bahwa data yang diterima oleh aplikasi adalah data yang benar dan sesuai dengan aturan yang telah ditetapkan, sehingga mencegah kesalahan dan potensi masalah keamanan.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` digunakan untuk melindungi aplikasi web dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang dapat membuat pengguna yang terautentikasi melakukan tindakan yang tidak diinginkan di aplikasi web tanpa sepengetahuan mereka. Jika kita tidak menambahkan `csrf_token` pada form Django, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan kelemahan ini untuk mengirim permintaan berbahaya yang tampaknya sah dari pengguna yang terautentikasi, seperti mengubah kata sandi atau melakukan transaksi tanpa izin. Dengan `csrf_token`, Django memvalidasi bahwa permintaan yang dibuat berasal dari pengguna yang benar-benar mengunjungi situs, bukan dari sumber eksternal yang tidak sah.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. **Pertama**
saya membuat project Django dan memetakan struktur aplikasinya, seperti model, views, dan template.
Kemudian, saya mulai dengan membuat form dan menggunakan method is_valid() untuk memvalidasi data input.
Selanjutnya, saya memastikan bahwa setiap form memiliki csrf_token untuk melindungi aplikasi dari serangan CSRF.
Setelah itu, saya memastikan penggunaan JSON sebagai format pengiriman data yang efisien antara klien dan server.
Terakhir, saya melakukan testing secara berkala untuk memastikan bahwa semua langkah berjalan sesuai harapan dan aplikasi bebas dari masalah validasi serta keamanan.
1. **Membuat Input Form**
   - Mengimplemntasikan skeleton dengan membuat berkas `base.html` sebagai template dasar untuk halaman web lainnya di dalam proyek.
   - Mengubah Primary Key Dari Integer Menjadi UUID pada `models.py` lalu melakukan migrasi.
   - Membuat file `forms.py` untuk membuat struktur form yang akan menerima data entry yang baru.
   - Menambahkan import redirect pada `views.py` lalu membuat fungsi baru `create_adornments_entry` yang menerima parameter `request` yang nantinya akan menambah data entry secara otomatis.
   - Melakukan import fungsi yang dibuat sebelumnya dan menambhakan path URL.
   - Membuat berkas `create_adornments_entry.html`, menambhkan `csrf_token`, dan `{% block content %}` untuk menampilkan data d serta tombol baru yang akan redirect langsung ke form.
   - Menjalankan perintah `python manage.py runserver`

2. **Menambahkan Views untuk Menampilkan Data dalam Format XML dan JSON**
   - Menambahkan import `HttpResponse` dan `Serializer`
   - Membuat fungsi yang menerima parameter request dan menambahkan return function `HttpResponse`, untuk mengembalikan data dalam bentuk `XML`
   - Membuat fungsi yang menerima parameter request dan menambahkan return function `HttpResponse`, untuk mengembalikan data dalam bentuk `json`
   - Membuat fungsi yang menyimpan hasil query data dengan id tertentu dan menambahkan return function `HttpResponse` dengan value `application/xml` dan `application/json`

3. **Membuat Routing URL**
   - Manambahkan import untuk fungsi yang dibuat sebelumnya `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`
   - Menambahkan path URL untuk keempat fungsi yang sebelumnya diimport

### SCREENSHOTS POSTMAN
**POSTMAN XML**
![Request Get XML](postman/XML.jpeg)
**POSTMAN json**
![Request Get json](postman/json.jpeg)
**POSTMAN XML by ID**
![Request Get XML by ID](postman/XMLbyID.jpeg)
**POSTMAN json by ID**
![Request Get json by ID](postman/jsonbyID.jpeg)
