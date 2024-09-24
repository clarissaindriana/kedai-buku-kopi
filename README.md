# Kedai Buku Kopi

Nama: Clarissa Indriana P
NPM: 2306211660
Kelas: PBP B

Tautan aplikasi PWS: http://clarissa-indriana-kedaibukukopi.pbp.cs.ui.ac.id 


## Tugas 2

### Pembuatan Project Django
Mengetahui bahwa: 
main = direktori aplikasi
kedai_buku_kopi = direktori project

1. Membuat sebuah proyek Django baru bernama kedai_buku_kopi yang sebelumnya berada di direktori utama kedai-buku-kopi dan terhubung ke direktori github
2. Membuat direktori aplikasi bernama main
3. Mendaftarkan aplikasi main ke dalam proyek kedai_buku_kopi
4. Setelah itu membuat model di dalam models.py dalam aplikasi main dengan nama class Product, fungsi model adalah untuk menyimpan script database
5. Membuat direktori templates di dalam direktori main. Di dalam direktori templates akan terdapat template (main.html) yang berguna untuk menampilkan data program kedai buku kopi (saat ini aplikasi kedai buku kopi belum punya data apapun)
6. Membuat sebuah fungsi di dalam views.py yang terdapat di dalam direktori aplikasi main untuk dikembalikan ke dalam sebuah template html (view menghubungkan model dengan template)
7. Routing URL aplikasi main dengan cara membuat urls.py di dalam direktori aplikasi main untuk mengatur rute URL yang terkait dengan aplikasi main. Dalam tugas-2 kali ini, urls.py pada aplikasi main digunakan untuk memetakan fungsi yang telah dibuat pada views.py
8. Routing URL proyek kedai_buku_kopi menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan main
9. Deployment ke PWS dengan menambahkan server PWS ke ALLOWED HOST proyek kedai_buku_kopi
10. Proyek sekarang dapat diakses melalui internet

### SOAL

**Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya.**
Membuat request dari internet -> webserver environment -> run django -> extract argument dari request -> diteruskan ke views.py <-> views akan mencari data terkatit di models.py -> mengembalikan data ke dalam template html untuk ditampilkan ke pada user atas respon dari request.
![bagan_mtv](https://github.com/user-attachments/assets/680e029c-f078-4f5e-b691-82ab33ac95e3)

**Fungsi git dalam pengembangan perangkat lunak!**
Git digunakan untuk beberapa hal, seperti:
1. Pengelolaan Repositori: Git digunakan untuk penyimpanan dan pengelolaan repositori baik di lokal komputer maupun server seperti github.
2. Melacak Perubahan Kode: Terdapat history revisi yang memungkinkan pengembang untuk melacak setiap perubahan yang dilakukan pada kode sumber. Setiap kali ada perubahan yang disimpan (disebut sebagai commit), Git mencatat versi baru dari proyek, lengkap dengan catatan siapa yang membuat perubahan, kapan perubahan itu dibuat, dan deskripsi perubahan tersebut.
3. Kolaborasi Tim: Git memudahkan banyak pengembang untuk bekerja bersama pada proyek yang sama. Dengan Git, setiap pengembang dapat bekerja pada salinan lokal dari proyek, membuat perubahan, dan kemudian menggabungkannya kembali ke repositori utama.

**Dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
1. Mudah dipelajari
2. Terstruktur
3. Pendekatan berbasis MVT yang banyak digunakan dalam pengembangan perangkat lunak. Memahami MVT membantu pemula mengerti konsep dasar pemisahan tanggung jawab dan manajemen pengembangan aplikasi, dan hal tersebut sangat penting dalam pengembangan perangkat lunak skala besar.
4. Popularitas, sudah digunakan di industri Django digunakan oleh banyak perusahaan besar dan proyek skala industri.

**Mengapa model pada Django disebut sebagai ORM?**
Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai lapisan yang menghubungkan antara objek dalam kode Python dengan tabel dalam basis data relasional. ORM memungkinkan pengembang untuk bekerja dengan data menggunakan konsep objek dalam bahasa pemrograman, tanpa harus menulis SQL secara langsung untuk berinteraksi dengan basis data. 

## Tugas 3

### Implementasi Form dan Data Delivery

**Skeleton sebagai kerangka views**
Berfungsi sebagai kerangka views dari situs web dan dapat memastikan adanya konsistensi dalam desain situs web serta memperkecil kemungkinan terjadinya redundansi kode.

1. Buat direktori templates pada direktori utama (root folder)
Membuat berkas html baru bernama base.html. Berkas base.html berfungsi sebagai template dasar. Template turunan akan me-extend template dasar (base.html) dan mengganti konten di dalam {% block %}  sesuai kebutuhan.

2. Memasukkan direktori templates ke dalam settings.py yang ada di dalam direktori proyek (kedai_buku_kopi)
'DIRS': [BASE_DIR / 'templates']

3. Di subdirektori templates yang terdapat di direktori main (main/templates/) buat main.html meng-extends base.html sebagai template utama dengan menambahkan block tertentu

**Membuat Form Input Data dan Menampilkan Data Product Pada HTML**
1. Mengubah primary key ID dari setiap objek model dari integer ke UUID pada berkas models.py untuk keamanan

2. Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data Product baru

model = Product 
Digunakan untuk menunjukkan model yang akan digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product

fields = ['name', 'price', 'description', 'rating', 'pairing']
Untuk menunjukkan field dari model Product yang digunakan untuk form. 

3. Di berkas views.py, buat fungsi baru dengan nama create_product yang menerima parameter request untuk menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data di-submit dari form.

4. Menambahkan key:value baru di dalam context di fungsi show_main yang berada di views.py berdasarkan product_entries = Product.objects.all() yang digunakan untuk mengambil seluruh objek Product yang tersimpan pada database.

5. Buka urls.py yang ada pada direktori main. Import fungsi baru yang sudah dibuat, yaitu create_product, dan tambahkan URL path ke dalam variable urlpatterns untuk mengakses fungsi create_product
	
6. Buat berkas HTML baru dengan nama create_product.html pada direktori main/templates. Terdapat template tag yang digunakan untuk menampilkan fields form yang sudah dibuat pada forms.py sebagai table. Selain itu, ada tombol submit untuk mengirimkan request ke view create_product(request). Menggunakan form dengan metode FORM

7. Buka berkas main.html dan menambahkan kode untuk menampilkan data Product dalam bentuk tabel serta tombol "Add New Product” yang akan redirect ke halaman form.

**Mengembalikan Data dalam Bentuk XML dan JSON**
1. Buat fungsi baru di views.py direktori main  yang menerima parameter request dengan nama show_xml dan show_json 

2. Buat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product dan me-return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML atau JSON

3. Buka urls.py di direktori main untuk mengimport fungsi baru yang sudah dibuat dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor

**Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON**
1. Buka views.py yang ada pada direktori main dan membuat dua fungsi baru yang menerima parameter request dan id dengan nama show_xml_by_id dan show_json_by_id

2. Buat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada Product dan me-return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML atau JSON

3. Buka urls.py di direktori main untuk mengimport fungsi baru yang sudah dibuat dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor

### SOAL
**Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform**
Data delivery memungkinkan data yang ada di server atau database pusat dapat diakses oleh pengguna di berbagai lokasi. Platform perlu berintegrasi dengan layanan lain seperti API eksternal. Data delivery memastikan data yang diperlukan dapat dikirim dan direrima dengan format yang sesuai, sehingga memungkinkan kolaborasi antar sistem.

**Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
JSON
- JSON memiliki struktur yang lebih sederhana dan ringan. Formatnya terdiri atas key:value. JSON lebih mudah dipahami dan lebih sederhana dalam hal sintaks dibandingkan XML.
- JSON dirancang untuk pertukaran data, sehingga lebih cocok digunakan dalam API, web services, dan komunikasi data antar aplikasi.

XML
- XML menggunakan elemen dan tag, seperti <element></element>, membuatnya lebih sulit dibaca dan dipahami secara visual.
- XML selain digunakan untuk pertukaran data, juga dirancang untuk mendeskripsikan dokumen yang kompleks dan memiliki struktur hierarki yang lebih formal. XML lebih cocok untuk dokumen yang membutuhkan metadata atau markup yang lebih kompleks.

Kesimpulan: JSON lebih baik dalam hal kecepatan, kesederhanaan, dan efisiensi. XML digunakan dalam konteks di mana dibutuhkan dokumen yang lebih kompleks dan terstruktur secara mendetail. JSON lebih populer karena lebih sesuai dengan kebutuhan teknologi modern yang mengutamakan kecepatan, efisiensi, dan kesederhanaan.

**Apa fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method is_valid() pada form di Django memiliki fungsi utama untuk memvalidasi data yang dikirimkan melalui form. Ketika sebuah form menerima data input dari pengguna, seperti melalui POST request, method ini digunakan sebagai sistem validasi otomatis untuk berbagai jenis input (misalnya, integer, email, URL) sehingga pengembang tidak perlu menulis validasi sendiri setiap kali menerima input dari pengguna.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
csrf_token adalah nilai unik yang dihasilkan secara acak dan dimasukkan ke dalam form. Token ini bertindak sebagai lapisan keamanan tambahan dengan memastikan bahwa permintaan yang dikirimkan berasal dari pengguna yang sah dan bukan dari penyerang yang berusaha mengeksploitasi sesi pengguna yang telah diautentikasi. Saat permintaan dikirim ke server, server akan memeriksa apakah token yang dikirim sesuai dengan token yang disimpan di sesi pengguna. Jika token tidak valid atau tidak ada, permintaan akan ditolak, melindungi aplikasi dari serangan CSRF. Jika aplikasi tidak menggunakan token CSRF, penyerang dapat memanfaatkan sesi yang telah diautentikasi untuk melakukan tindakan atas nama pengguna, bahkan tanpa interaksi pengguna langsung.

### POSTMAN
**XML**
<img width="1275" alt="XML" src="https://github.com/user-attachments/assets/82a66c98-c9ae-4e57-b007-4e9b07ea9188">

**JSON**
<img width="1275" alt="JSON" src="https://github.com/user-attachments/assets/b284b7ab-79a6-4450-a23d-93c943f64b21">

**XML by ID**
<img width="1275" alt="XML_by_ID" src="https://github.com/user-attachments/assets/a08a0199-5440-47e1-9c81-ffb3eb75ee98">

**JSON by ID**
<img width="1275" alt="JSON_by_ID" src="https://github.com/user-attachments/assets/2ed730b2-6c8e-4e20-912d-98b0a652341b">


## Tugas 4

### Implementasi Autentikasi, Session, dan Cookies pada Django

**Membuat Fungsi dan Form Registrasi**
1. Import UserCreationForm dan import messages di views.py 
UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web tanpa harus menulis kode dari awal.

2. Tambah fungsi register di views.py 
Berguna untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

3. Buat berkas HTML baru dengan nama register.html pada direktori main/templates. Isi dari register.html adalah untuk laman register.

4. Buka urls.py di subdirektori main dan import fungsi register dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

**Membuat Fungsi Login**
1. Import di views.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

Fungsi authenticate dan login yang di-import di atas adalah fungsi bawaan Django yang dapat digunakan untuk melakukan autentikasi dan login (jika autentikasi berhasil).

2. Tambah fungsi login_user di views.py. 
Fungsi ini berfungsi untuk mengautentikasi pengguna yang ingin login.

3. Buat berkas HTML baru dengan nama login.html untuk menampilkan laman login

4. Buka urls.py untuk import login_user dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

**Membuat Fungsi Logout**
1. Import di views.py
from django.contrib.auth import logout

2. Tambah fungsi logout_user di views.py
Fungsi ini berfungsi untuk melakukan mekanisme logout

3. Add logout button di main.html pada main/templates

4. Buka urls.py untuk import logout_user dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi

**Merestriksi Akses Halaman Main**
1. Import di views.py

from django.contrib.auth.decorators import login_required

digunakan untuk mengimpor sebuah decorator yang bisa mengharuskan pengguna masuk (login) terlebih dahulu sebelum dapat mengakses suatu halaman web.

2. Tambahkan potongan kode @login_required(login_url='/login') di atas fungsi show_main agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

**Menggunakan Data Dari Cookies**
Penggunaan cookies dengan menambahkan data last login dan menampilkannya ke halaman main.

1. import di views.py

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


Pada fungsi login_user, akan ada fungsionalitas menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login.

2. Pada fungsi show_main, tambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context

'last_login': request.COOKIES['last_login'] berfungsi menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web.

3. Ubah fungsi logout_user

response.delete_cookie('last_login') berfungsi untuk menghapus cookie last_login saat pengguna melakukan logout.

5. Di main.html dan tambahkan potongan kode setelah tombol logout untuk menampilkan data last login.

**Menghubungkan Model Product dengan User**

Menghubungkan setiap objek Product yang akan dibuat dengan pengguna yang membuatnya, sehingga pengguna yang sedang terotorisasi hanya melihat Product entries yang telah dibuat sendiri

1. import di models.py
from django.contrib.auth.models import User

2. Pada model Product yang sudah dibuat, tambahkan User
user = models.ForeignKey(User, on_delete=models.CASCADE)

Berfungsi untuk menghubungkan satu product entry dengan satu user melalui sebuah relationship, dimana sebuah product entry pasti terasosiasikan dengan seorang user.

3. Di views.py ubah kode dalam create_product 

Parameter commit=False yang digunakan pada potongan kode diatas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. 

Pada kasus ini, kita akan mengisi field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.

4. Ubah value dari product_entries dan context pada fungsi show_main 

product_entries = Product.objects.filter(user=request.user)
'name': request.user.username,

**Mempersiapkan aplikasi web kita untuk environtment production**
Menambahkan sebuah import baru pada settings.py yang ada pada subdirektori kedai_buku_kopi

PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION

### SOAL
1. Apa perbedaan antara HttpResponseRedirect() dan redirect() 
HttpResponseRedirect() maupun redirect() digunakan untuk mengarahkan pengguna ke URL lain

HttpResponseRedirect()
- Mengirimkan kode status HTTP 302 ke browser, HTTP response status codes yang bertugas sebagai Redirection messages (300–399). 
- return HttpResponseRedirect('/new-url/') dalam mereturn HttpResponseRedirect() harus mengisi secara manual URL yang ingin dituju

redirect()
- Dapat menerima beberapa jenis argumen (seperti URL, nama view, atau objek model) dan mengembalikannya sebagai respons redirect. Django akan membuat URL yang benar secara di balik layar tanpa kita harus menuliskannya secara eksplisit di parameter fungsi

2. Jelaskan cara kerja penghubungan model Product dengan User! 
a. Tambahkan User pada model Product yang sudah dibuat

user = models.ForeignKey(User, on_delete=models.CASCADE)

- Foreign key user Berfungsi untuk menghubungkan satu product entry dengan satu user melalui sebuah relationship, dimana sebuah product entry pasti terasosiasikan dengan seorang user.
- on_delete=models.CASCADE memastikan bahwa jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.

b. Pada saat produk baru dibuat melalui form, produk tersebut harus secara otomatis terhubung dengan pengguna yang sedang login. Hal ini dilakukan di views.py dengan menambahkan logika untuk mengisi field user dari objek Product yang akan disimpan.

product_entry = form.save(commit=False)
product_entry.user = request.user

- form.save(commit=False) mencegah form dari langsung menyimpan data ke database. Ini memberikan kesempatan untuk memodifikasi objek sebelum disimpan.
- product_entry.user = request.user menghubungkan produk yang baru dibuat dengan pengguna yang sedang login.

c. Untuk menampilkan hanya produk yang dimiliki oleh pengguna yang sedang login, filter produk di query berdasarkan request.user

product_entries = Product.objects.filter(user=request.user)

- Product.objects.filter(user=request.user) akan mengambil semua produk yang dimiliki oleh pengguna yang sedang login. 

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses memverifikasi identitas pengguna (misalnya melalui login).
Authorization adalah proses menentukan izin atau akses pengguna terhadap fitur tertentu setelah mereka terautentikasi.

Saat pengguna login: Pengguna memasukkan username dan password, Django melakukan verifikasi apakah input sama dengan data di database (melalui model User), Django menyimpan informasi pengguna yang berhasil login di sesi (session) dan masuk ke otorisasi. Setelah pengguna berhasil login (terautentikasi), Django dapat membatasi akses berdasarkan permissions atau roles.

Implementasi:

a. Authentication
Django menyediakan sistem autentikasi bawaan yang memungkinkan pengelolaan login, logout, dan otentikasi pengguna. 

Seperti pada:
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

if form.is_valid():
    user = form.get_user()
    login(request, user)
    return redirect('main:show_main')

b. Authorization
Django juga mendukung peran berbasis grup. Misalnya, Anda dapat mengelompokkan pengguna ke dalam grup seperti admin, editor, atau viewer

Django menyediakan decorator seperti @permission_required atau @login_required untuk memastikan pengguna memiliki izin yang sesuai sebelum mengakses view

Seperti pada:
@login_required(login_url='/login')
def show_main(request):
    ...

Menggunakan @login_required untuk mengizinkan hanya pengguna yang login yang mengakses halaman tertentu

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Login: 
Ketika pengguna berhasil login, Django membuat session untuk pengguna tersebut. Session ini adalah data sementara yang disimpan oleh server dan terhubung dengan pengguna. Django mengirimkan cookie ke browser pengguna yang berisi ID session. Cookie ini biasanya bernama sessionid dan digunakan untuk mengidentifikasi session di sisi server. Setiap kali pengguna melakukan permintaan (request) setelah login, cookie ini akan dikirimkan ke server bersama permintaan tersebut. Django kemudian menggunakan ID session dari cookie untuk mencari data session di server yang berisi informasi pengguna yang login (misalnya, request.user), sehingga sistem tahu siapa pengguna tersebut.

Kegunaan lain dari Cookies:
Menyimpan preferensi pengguna, melacak aktivitas pengguna, login otomatis

Apakah semua cookies aman digunakan?
Cookies Biasa (Non-Secure Cookies):
Cookies biasa dikirim melalui protokol HTTP yang tidak terenkripsi, sehingga rentan terhadap serangan man-in-the-middle (MITM)

Secure Cookies:
Secure Cookies adalah cookies yang hanya dikirimkan melalui koneksi HTTPS (yang terenkripsi). Dengan menggunakan atribut Secure, cookies ini tidak akan dikirimkan melalui HTTP yang tidak aman, sehingga lebih terlindungi dari serangan MITM.

