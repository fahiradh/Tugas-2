### Fahira Adindiah (2106751575) / PBP D

## LINK HEROKU
### https://katalog-barang.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} digunakan untuk memberi perlindungan website dari Cross Site Request Forgeries. Cross Site Request Forgeries merupakan tindakan dimana website diberikan tautan, formulir, atau beberapa request lain yang dibuat oleh malicious user (penipu). Dengan csrf_token, akan dibatasi request yang dapat diterima, yaitu request yang hanya berasal dari page dengan token yang sudah didaftarkan sebelumnya. 

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Setiap elemen atribut form bisa dibuat secara manual dengan menggunakan {{ form.name_of_field }}. Elemen atribut tersebut akan dirender otomatis oleh django. Selain itu, kita juga bisa membuat form sendiri dengan <form> di dalam file HTML. Data dari <form> diambil dengan request.POST.get('nama') dengan nama adalah elemen yang ditambahkan ke <form> tag html.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Contoh pada submisi create-task. Url https://katalog-barang.herokuapp.com/create-task/ akan menerima input dari pengguna. Input tersebut diterima karena create_task.html redirect ke fungsi create_task(request) yang ada di views.py. Fungsi create_task(request) akan membuat object TodoList sesuai dengan input data yang dimasukkan user. Setelah object berhasil dibuat, data object diterima variabel data_todolist dalam fungsin show_todolist di views.py. Dan karena todolist.html redirect ke data_todolist, object yang baru dibuat akan ditambilkan ke dalam tabel todolist.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat folder todolist dengan `python3 manage.py startapp todolist`
2. Menambahkan path di urls.py project_django
`path('todolist/', include('todolist.urls'))`
3. Membuat class TodoList dengan parameter model di models.py
```
class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
4. Migrasi database

5. Membuat fungsi show_todolist, login_user, logout_user, register, create_task, update_task, delete_task di views.py dengan import model dari models.py
6. Membuat folder templates dan membuat 4 file html, yaitu create_task.html, login.html, register.html, todolist.html. Keempat file tersebut memuat elemen atribut form, button, title, dan lainnya yang redirect ke fungsi di views.py
7. Menambahkan masing-masing path ke urls.py
```
    ....
    path('login/', login_user, name='login'), 
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create-task'),
    path('logout/', logout_user, name='logout'),
    path('deletetask/<int:id>', delete_task, name='deletetask'),
    path('updatetask/<int:id>', update_task, name='updatetask')
    ....
```
8. Git add, commit, push ke GitHub
