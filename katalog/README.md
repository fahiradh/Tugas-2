Fahira Adindiah (2106751575) / PBP D

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
Jawab:


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab:
Virtual envinronment membantu mengeliminasi konflik dependensi yang mungkin terjadi. Contohnya, kita baru saja menginstall versi terbaru dari django, lalu kita diberikan project django yang menggunakan versi lebih lama dari yang baru kita install. Agar projectnya dapat berjalan, kita mungkin saja menginstall versi lama django yang dibutuhkan. Namun, solusi tersebut tidak efektif jika semua project django yang kita punya menggunakan versi django yang berbeda-beda. Oleh karena itu, virtual environment membantu menjalankan project django di semua versi django, python, dan module yang terisolasi satu sama lain.

Virtual environment tidak wajib digunakan. Aplikasi web tetap dapat berjalan meskipun tanpa virtual environment. Akan tetapi, berdasarkan penjelasan singkat tentang peran virtual environment di atas, akan lebih efektif jika membuat aplikasi web berbasis Djangp menggunakan virtual environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawab:
Langkah pertama yang saya lakukan adalah membuat fungsi show_katalog di views.py untuk mengambil data dari model dan dikembalikan ke dalam sebuah HTML. Selanjutnya, saya membuat routing yang memetakan fungsi di views.py ke urls.py. Saya juga mengisi dan memperbarui konten yang ditampilkan dengan mengedit katalog.html. Saya menambahkan beberapa style seperti warna, ukuran, dan pengaturan tabel. Untuk memasukkan konten ke dalam tabel, saya mengambil data dari initial_catalog_data.json. Setelah selesai melakukan semua tahapan tersebut, saya melakukan migrasi database.

Setelah berhasil menampilkan web di https://localhost:8000/katalog/, saya melakukan git add, commit, push ke ropositori Tugas-2-PBP yang sudah saya buat sebelumnya.

Untuk mendeploy otomatis dari GitHub ke Heroku, 




===================================================================================================================================
Untuk mendeploy secara otomatis dari Gitlab ke Heroku, diperlukan CI, Continuous Integration antara gitlab dan heroku. Untuk mengatur ini, diperlukan sebuah pipeline yang berfungsi menghubungkan repo gitlab dengan app pada heroku.

Kita perlu membuat suatu file .gitlab-ci.yml dimana isinya adalah perintah-perintah yang dilakukan pada beberapa tahapan. test, deploy, dll. Namun dari template file yang saya dapat dari Kak Pewe, isinya hanya mengenai deployment. Command-command yang terdapat di file ini akan dijalankan saat kita melakukan push ke gitlab. Salah satu command yang diperlukan adalah dpl (deploy). Parameter yang perlu diisi ada provider (heroku) dan beberapa data penting lainnya (nama app, url app, dan API key). Untuk mempermudah pengisian file yml ini, saya masukkan ketiga data penting tersebut sebagai variable pada repo saya. Sehingga untuk memanggilnya hanya perlu $(NAMA_VARIABEL).

Selain file gitlab-ci, kita juga harus mengatur bagian django. Beberapa hal yang harus dilakukan adalah mengatur static files dengan whitenoise dan menambahkan url app heroku sebagai salah satu allowed host di settings. Terakhir, dibutuhkan web process untuk berjalan saat kita mengakses heroku. Setelah sekian banyak try and error saya menemukan cara untuk mengaktifkan web process. Menggunakan module gunicorn dan file Procfile untuk menjalankan project. Demikian, web yang saya buat ini online di heroku.