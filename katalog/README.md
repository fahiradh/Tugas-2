Fahira Adindiah (2106751575) / PBP D

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
Jawab:
https://ristek.link/RequestClient

Jika URL menerima request, maka secara otomatis akan memanggil urls.py. Request diteruskan oleh urls.py ke views.py. Oleh views.py akan dipanggil model (models.py) untuk membaca dan menuliskan data. Selanjutnya, template (<filename>.html) akan memberikan data yang dibutuhkan ke views.py. Terakhir, data yang sudah didapat diteruskan views.py ke HTTP untuk ditampilkan di halaman web.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab:
Virtual envinronment membantu mengeliminasi konflik dependensi yang mungkin terjadi. Contohnya, kita baru saja menginstall versi terbaru dari django, lalu kita diberikan project django yang menggunakan versi lebih lama dari yang baru kita install. Agar projectnya dapat berjalan, kita mungkin saja menginstall versi lama django yang dibutuhkan. Namun, solusi tersebut tidak efektif jika semua project django yang kita punya menggunakan versi django yang berbeda-beda. Oleh karena itu, virtual environment membantu menjalankan project django di semua versi django, python, dan module yang terisolasi satu sama lain.

Virtual environment tidak wajib digunakan. Aplikasi web tetap dapat berjalan meskipun tanpa virtual environment. Akan tetapi, berdasarkan penjelasan singkat tentang peran virtual environment di atas, akan lebih efektif jika membuat aplikasi web berbasis Django menggunakan virtual environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawab:
Langkah pertama yang saya lakukan adalah membuat fungsi show_katalog di views.py untuk mengambil data dari model dan dikembalikan ke dalam sebuah HTML. Selanjutnya, saya membuat routing yang memetakan fungsi di views.py ke urls.py. Saya juga mengisi dan memperbarui konten yang ditampilkan dengan mengedit katalog.html. Saya menambahkan beberapa style seperti warna, ukuran, dan pengaturan tabel. Untuk memasukkan konten ke dalam tabel, saya mengambil data dari initial_catalog_data.json. Setelah selesai melakukan semua tahapan tersebut, saya melakukan migrasi database.

Setelah berhasil menampilkan web di https://localhost:8000/katalog/, saya melakukan git add, commit, push ke ropositori Tugas-2 yang sudah saya buat sebelumnya.

Untuk mendeploy aplikasi ke Heroku, saya membuat satu aplikasi bernama katalog-barang di Heroku. Kemudian, saya menyalin API key yang ada di Heroku. API key ini akan digunakan untuk mengatur konfigurasi repositori Tugas-2. Saya menyimpan API key dengan variabel HEROKU_API_KEY dan katalog-barang dengan variabel HEROKU_APP_NAME di secret actions repositori. Selain itu, saya juga mengatur static files dengan whitenoise, menggunakan module gunicorn, dan file Procfile untuk menjalankan project. Tahap terakhir, saya menjalankan workflow aplikasi. Dengan demikian, web yang saya buat berstatus online di Heroku (https://katalog-barang.herokuapp.com/katalog/).