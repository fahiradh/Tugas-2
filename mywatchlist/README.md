### Fahira Adindiah / PBP - D

## Link Heroku
https://katalog-barang.herokuapp.com/mywatchlist/

## Jelaskan perbedaan antara JSON, XML, dan HTML!
JavaScript Object Notation atau yang lebih dikenal dengan JSON merupakan markup language yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server yang disajikan kepada pembaca dalam bentuk key dan value.
HyperText Markup Language atau HTML merupakan sebuah markup language yang menitikberatkan pada bagaimana format tampilan dari data.
Extensible Markup Language atau XML merupakan markup language untuk yang menitikberatkan pada struktur dan transfer data.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery berguna untuk memudahkan platform mengirim data antara clients dengan server. Terdapat beberapa data tertentu yang memerlukan format khusus dalam proses pertukarannya. Format yang umum digunakan adalah HTML, XML, dan JSON. Dengan ketiga format di atas, proses pertukaran data akan menjadi lebih sederhana karena data akan lebih mudah dipahami oleh berbagai bahasa pemrograman dan API.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
Pertama, saya mengaktifkan virtual env di direktori Tugas-2. Kemudian, saya membuat folder django app `mywatchlist` dengan menjalankan  command `python3 manage.py startapp mywatchlist`. Setelah folder `mywatchlist` berhasil dibuat, saya mengisi views.py dengan 3 fungsi, yaitu `show_watchlist`, `show_xml`, dan `show_json`. Selanjutnya, saya juga melengkapi path aplikasi pada file `urls.py` di dalam folder `mywatchlist`. Saya menambahkan path html, xml, dan json.

Pada `models.py`, saya membuat class baru bernama `WatchlistItem`. Class tersebut diisi dengan variabel data film yang akan ditampilkan di tabel, yaitu watched, title, rating, release_date, dan review. Saya juga melengkapi file `apps.py` dengan `MywatchlistConfig`. Selanjutnya, saya membuat `mywatchlist.html` untuk membuat format yang ingin ditampilkan di halaman web. Data-data yang dibutuhkan, seperti 10 film yang kan ditampilkan, saya buat di folder `fixtures` dengan `initial_mywatchlist_data.json`. 

Setelah semua berhasil saya lakukan, saya melakukan migration dengan `python3 manage.py makemigrations` dan `pytho3 manage.py migrate`. Dan karena konten belum bisa ditampilkan di website, saya melakukan loaddata dengan `python3 manage.py loaddata initial_mywatchlist_data.json` di console heroku.

## Postman
HTML: https://ristek.link/html
XML: https://ristek.link/xml
JSON: https://ristek.link/json
