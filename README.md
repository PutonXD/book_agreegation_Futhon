# Manajemen Toko Buku
Program ini merupakan implementasi sederhana untuk manajemen toko buku menggunakan konsep Aggregation dengan dua kelas utama: Book (Buku) dan Bookstore (Toko Buku). Program ini memungkinkan pengguna untuk menambahkan buku ke dalam toko buku dan menampilkan daftar buku yang tersedia.

# Kelas Book
Kelas Book merepresentasikan atribut-atribut yang dimiliki oleh sebuah buku. Setiap objek Book memiliki atribut sebagai berikut:

- title (string): judul buku.
- author (string): penulis buku.
- price (float): harga buku.
  
# Kelas Bookstore
Kelas Bookstore merepresentasikan sebuah toko buku yang memiliki daftar buku yang tersedia. Setiap objek Bookstore memiliki atribut sebagai berikut:
- name (string): nama toko buku.
- books (list): daftar objek Book yang tersedia di toko.

Selain atribut, kelas Bookstore juga memiliki metode sebagai berikut:
- add_book(book): untuk menambahkan buku baru ke dalam daftar buku toko.
- display_books(): untuk menampilkan daftar buku yang tersedia beserta informasi detailnya, seperti judul, penulis, dan harga.

# Cara Menggunakan Program
Berikut adalah langkah-langkah untuk menggunakan program ini:

- Buat objek Bookstore dengan menyediakan nama toko buku.
- Buat objek Book dengan menyediakan judul, penulis, dan harga buku.
- Tambahkan objek Book ke dalam objek Bookstore menggunakan metode add_book().
- Panggil metode display_books() untuk menampilkan daftar buku yang tersedia di toko.
