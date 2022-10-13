### LINK DEPLOYMENT HEROKU
### https://katalog-barang.herokuapp.com/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming merupakan proses eksekusi program secara sequential, di mulai dari line pertama dan seterusnya sesuai hierarki. Sementara itu, asynchronous programming merupakan proses eksekusi program yang tidak terikat pada hierarki. Eksekusi program dilakukan dengan tidak terikan pada proses lain atau independen. 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah paradigma pemrograman yang alur programnya ditentukan oleh event yang merupakan keluaran dari suatu proses. Contohnya ketika tombol `Create Task` diklik, maka akan mengarahkan pada modal create-task.

## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX menerapkan asynchronous programming sehingga pengembang (developer) tidak perlu mereload browser jika ada perubahan data yang kecil. AJAX secara otomatis akan meng-update semua perubahan-perubahan yang dibuat developer ke websitenya. Hal ini disebut asynchronous programming karena AJAX tidak perlu menunggu respon dari server terkait request yang diajukan pada saat mengeksekusi program. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya mengatur `views.py` milik todolist. Saya menambahkan fungsi `show_todolist_json` dan `add_task`. Kedua fungsi tersebut saya import ke `urls.py`. Di sana, saya buat path yang mengarah ke dua fungsi tersebut. Kemudian, saya menambahkan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` di `base.html`. Setelah selesai melakukan konfigurasi ajax, saya mulai mengimplementasikan ajax di `todolist.html`. Di sana, saya menambahkan button add task yang memunculkan 2 input field, yaitu title dan description untuk task baru. Input field akan menerima input user yang kemudian akan membuat objek task baru dengan memanggil fungsi `add_task`. Objek tersebut disimpan di json. Untuk melihat data objek, dapat memanggil fungsi `show_todolist_json`.

Kemudian, untuk menyelesaikan bonus pada tugas ini, saya membuat fungsi `delete_task_ajax` di `views.py`. Fungsi tersebut akan mengambil objek task yang ingin dihapus dan menghapusnya. `delete_task_ajax` saya import ke urls.py dan membuat path `todolist/delete/`. Setelah itu, saya membuat fungsi baru di `todolist.html` khusus untuk meng-handle delete task dengan ajax. Nama fungsinya adalah `deleteTask(pk)`. Parameter pk akan membantu fungsi `delete_task_ajax` di `views.py` mencari objek yang ingin dihapus. Ketika objek berhasil dihapus, maka akan looping content sesuai data di json.
