## Fahira Adindiah (2106751575) - PBP D

## LINK DEPLOYMENT
### https://katalog-barang.herokuapp.com/todolist/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Perbedaan inline, internal, dan external CSS dapat dilihat dari cara pada penggunaannya di dalam file HTML. Internal class merupakan kode yang dituliskan dengan tag `<style>` pada bagian header dan merujuk pada satu class spesifik. Kelebihan dari internal CSS adalah memudahkan kostuminsasi design karena tidak perlu mengunggah beberapa file tambahan. Namun, banyaknya isi internal CSS akan memengaruhi waktu loading page. Berbeda dengan internal, inline CSS merupakan CSS yang dituliskan langsung pada atribut elemen HTML. Spesifiknya, inline CSS dituliskan di dalam atribut style elemen HTML. Inline CSS membuat proses request HTTP yang kecil untuk loading website jadi lebih cepat. Sementara itu, external CSS adalah CSS yang ditulis di luar file HTML dengan ekstensi .css. Biasanya CSS tersebut dipanggil di bagian header file HTML atau setelah `<head>`.

## Jelaskan tag HTML5 yang kamu ketahui.
`<h1>`hingga `<h5>` : Mencetak tulisan sebagai header. Semakin kecil angka, semakin besar ukuran header yang akan dicatak <br/>
`<p>` : Mencetak teks dalam bentuk paragraf<br/>
`<a>` : Me-refer link web tujuan<br/>
`<title>` : Mengatur judul halaman<br/>
`<button>` : Membuat sebuah tombol yang dapat di-klik<br/>
`<table> `: Membuat tabel<br/>
`<tr>` : Mendefinisikan baris pada tabel<br/>
`<td>` : Mendefinisikan kolom pada tabel

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Tag Selector : selector yang akan memilih elemen berdasarkan nama tag
ID Selector : selector yang akan memilih elemen berdasarkan nama class yang diberikan. Class yang dipilih spesifik. Umumnya, ID Selector ditandai dengan `#`.
Class Selector : sama dengan ID Selector, namun Class Selector dapat digunakan oleh beberapa elemen. Class Selector ditandai dengan `.`.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Untuk mengimplementasikan checklist 1-2, saya banyak mengambil referensi dari https://codepen.io/. Setelah memilih framework yang bagus dan cocok untuk saya terapkan di todolist, saya menyalin kode CSS-nya dan mengedit informasi yang ditambilkan lewat file HTML masing-masing halaman web. Selanjutnya, untuk checklist 3-4, saya dibantu oleh website https://developer.mozilla.org/. Setelah semua tambilan berhasil saya kostumisasi, saya melakukan git add, commit, dan push ke GitHub.