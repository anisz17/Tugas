# Lentera — Perpustakaan Digital (Django)

Website perpustakaan digital berbasis **Django** dengan fitur katalog buku, peminjaman, pembaca PDF, bookmark, riwayat, leaderboard, achievement, streak membaca, dan dashboard admin.

README ini disusun sebagai bahan belajar dan penjelasan proyek. Isinya:

1. Gambaran proyek dan struktur
2. Alur program
3. Pengertian pilar OOP beserta analogi dan contoh kode
4. Penerapan OOP di proyek (termasuk alasan mengapa sebuah contoh dihitung sebagai polimorfisme) dan relasi antarobjek (asosiasi, agregasi, komposisi, dependensi), semuanya dengan potongan kode
5. Penjelasan kode penting per file
6. Kumpulan pertanyaan dan jawaban
7. Catatan jujur (hal yang perlu dicek sebelum pengujian)

> **Cakupan.** README ini hanya menjelaskan file yang sudah dilampirkan: `config/urls.py`, `perpustakaan/urls.py`, `models.py`, `admin.py`, `tests.py`, potongan `views.py`, serta template `dashboard.html`, `baca.html`, dan `kelola_buku.html`. Bagian yang belum dilampirkan ditandai di bagian 7.

---

## 1. Gambaran Proyek

### Teknologi
- Python dan Django (pola MTV)
- SQLite (`db.sqlite3`)
- HTML + Django Template Language, CSS, JavaScript
- PDF.js untuk membaca PDF di browser
- Font Awesome untuk ikon

### Struktur folder (ringkas)

```
Perpus-Digital/
├── config/                  # pengaturan proyek (settings, urls utama)
├── perpustakaan/            # app utama
│   ├── models.py            # struktur data + logika objek (inti OOP)
│   ├── views.py             # logika halaman anggota
│   ├── views_admin.py       # logika halaman admin
│   ├── urls.py              # peta alamat app
│   ├── admin.py             # tampilan admin bawaan Django
│   ├── tests.py             # tes otomatis
│   ├── migrations/          # riwayat perubahan struktur database
│   ├── static/perpustakaan/ # css, js, img
│   └── templates/perpustakaan/  # katalog, peminjaman, dashboard, baca, dll.
├── media/                   # file upload (PDF buku, foto profil, background)
├── manage.py
├── requirements.txt
└── db.sqlite3
```

### Menjalankan

```bash
python -m venv venv
venv\Scripts\activate            # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py test            # menjalankan tes otomatis
```

---

## 2. Alur Program

### 2.1 Siklus satu request (pola MTV)

```
Browser
  │  1. meminta alamat, mis. /katalog/
  ▼
config/urls.py            → memeriksa admin/ dan simpan_progress, lalu include('perpustakaan.urls')
  ▼
perpustakaan/urls.py      → mencocokkan 'katalog/' ke views.katalog_view
  ▼
views.py (View)           → cek login, baca parameter, ambil data lewat ORM
  ▼
models.py (Model)         → BukuDigital.objects... → db.sqlite3
  ▼
views.py                  → render(request, "perpustakaan/katalog.html", context)
  ▼
Template (HTML + DTL)     → {{ variabel }}, {% for %}, {% url %}
  ▼
Browser                   → menampilkan halaman (CSS/JS dari static)
```

| Lapisan | Tugas | File |
|---|---|---|
| **M**odel | Struktur data dan aturan objek | `models.py` |
| **T**emplate | Tampilan | folder `templates/` |
| **V**iew | Logika: menerima request, mengolah data, memilih template | `views.py`, `views_admin.py` |

### 2.2 Alur katalog

1. User membuka `/katalog/` (`katalog_view`, wajib login).
2. View membaca `kategori` dan `q` dari `request.GET`.
3. Jika `q` sama persis dengan nama atau label kategori dan belum ada kategori dipilih, `q` dianggap filter kategori.
4. Filter kategori memakai `Q(...) | Q(...)` dengan `icontains`, sehingga nilai baru (`computer_science`) dan label lama (`Computer Science`) sama-sama cocok.
5. Pencarian `q` mencari di judul, penulis, kategori, dan deskripsi.
6. Hasil diubah menjadi daftar dictionary (`buku_lokal`), diurutkan berdasarkan judul, lalu dikirim ke `katalog.html` bersama `kategori_list` dan `tersimpan_ids` (id buku yang sudah di-bookmark).

### 2.3 Alur peminjaman

**Meminjam** (`pinjam_buku`, hanya POST, alamat `buku/<olid>/pinjam/`):

1. Validasi format id dengan `ITEM_ID_RE`; jika tidak cocok → 404.
2. Jika buku itu sudah dipinjam dan masih aktif → pesan info, redirect ke detail buku.
3. Jika pinjaman aktif sudah mencapai `user.max_loans` (default 5) → pesan error.
4. `_pastikan_buku` memastikan data buku tersedia.
5. `Peminjaman.objects.create(user=user, buku_digital=buku)` dengan status awal `"Dibaca"`.
6. Notifikasi dikirim, pesan sukses ditampilkan, lalu redirect ke `/peminjaman/`.

**Daftar pinjaman** (`peminjaman_view`): menampilkan pinjaman berstatus `"Dibaca"`, menempelkan `jatuh_tempo` ke tiap objek, dan menghitung `sisa_slot = max(batas - aktif, 0)`.

**Perpanjang** (`perpanjang_buku`, POST): hanya untuk pinjaman milik user yang masih aktif. Jika `perpanjangan >= MAKS_PERPANJANG` → error. Jika belum, jatuh tempo ditambah `MASA_PERPANJANG_HARI` dan counter `perpanjangan` naik 1.

**Mengembalikan** (`kembalikan_buku`): status menjadi `"Selesai"`, `progress_baca = 100`, `tanggal_kembali` diisi waktu sekarang, notifikasi dikirim. Pencapaian 5/10/25/50 buku selesai memicu notifikasi khusus.

### 2.4 Alur membaca, EXP, dan streak

1. Tombol "Lanjut Baca" mengarah ke `baca/<olid>/` (`baca_buku`) yang merender `baca.html`.
2. `buku.js` memuat PDF dari `data-link` memakai PDF.js; posisi terakhir dibaca dari `data-progress`.
3. Progres disimpan ke `simpan_progress`; detik baca dikirim berkala oleh `baca-ring.js` ke `waktu_baca` (`api/waktu-baca/`).
4. `waktu_baca` (POST):
   - membatasi klaim detik dari browser dengan selisih waktu nyata (anti-curang, memakai `session["ring_terakhir"]`);
   - menambah waktu ke `Peminjaman.waktu_baca_detik`;
   - mengelola "kolam" detik: setiap `RING_DETIK_PENUH` detik memberi `RING_EXP` EXP;
   - menambah `detik_baca_hari_ini` (maksimal `TARGET_HARIAN_DETIK` = 1800 detik atau 30 menit) dan mereset hitungan jika tanggal berganti;
   - memanggil `reset_streak_if_expired()` dan `update_streak()` milik `CustomUser`;
   - mengirim notifikasi: streak 3/7/14/30, EXP bertambah, level naik (`level = exp // 100 + 1`), dan peringkat naik.
5. Peringkat = 1 + jumlah member non-admin yang EXP-nya lebih tinggi.

### 2.5 Peta URL (ringkas)

| Kelompok | Alamat → view |
|---|---|
| Akun | `login/`, `register/`, `logout/` |
| Dashboard | `''` → `dashboard` |
| Katalog | `katalog/` → `katalog_view`; `buku/<olid>/` → `buku_detail`; `buku/<olid>/pinjam/` → `pinjam_buku`; `buku/<olid>/bookmark/` → `toggle_bookmark` |
| Peminjaman | `peminjaman/`; `kembalikan/<int:pinjaman_id>/`; `perpanjang/<int:pinjaman_id>/` |
| Membaca | `baca/<olid>/`; `api/waktu-baca/`; `buku/<olid>/progress/` (didaftarkan di `config/urls.py`) |
| Koleksi pribadi | `bookmarks/`, `riwayat/`, `ejournal/` |
| Gamifikasi | `leaderboard/`, `achievement/`, `api/update-pinned/` |
| Profil | `profil/`, `profil/<username>/` |
| Admin | semua berawalan `dashboard-admin/` → `views_admin.*` |

---

## 3. Pilar OOP: Pengertian dan Analogi

### 3.0 Dasar: Class dan Object

- **Class** adalah cetak biru yang mendefinisikan atribut (data) dan method (perilaku).
- **Object** adalah hasil nyata (instance) dari class itu, dengan nilai atribut masing-masing.

**Analogi:** class adalah cetakan kue, object adalah kue-kuenya. Satu cetakan bisa menghasilkan banyak kue, dan tiap kue bisa punya topping berbeda.

**Di proyek:** `BukuDigital` adalah class; satu baris buku tertentu, misalnya "Buku Tes Lokal", adalah object.

**Contoh kode umum:**

```python
class Kucing:                       # class = cetakan
    def __init__(self, nama):
        self.nama = nama            # atribut

k1 = Kucing("Mimi")                 # object 1
k2 = Kucing("Tom")                  # object 2 (nilai atribut berbeda)
```

**Potongan kode proyek** (`tests.py`): objek dibuat dari class `BukuDigital`.

```python
self.book = BukuDigital.objects.create(
    id_item='OL1234567W',
    judul='Buku Tes Lokal',
    penulis='Penulis Tes',
    tahun_terbit='2020',
)
```

### 3.1 Encapsulation (Enkapsulasi)

**Pengertian:** membungkus data dan method yang mengolah data itu dalam satu unit (class), serta mengatur agar data diubah lewat method yang punya aturan, bukan diubah sembarangan dari luar.

**Analogi: mesin ATM.** Saldo (data) tidak bisa kamu ubah langsung. Kamu hanya bisa memakai menu tarik atau setor (method), dan menu itu punya aturan sendiri: harus PIN benar, saldo harus cukup. Nasabah tidak perlu tahu cara aturan itu dijalankan.

**Catatan Python:** Python tidak punya `private` yang ketat seperti Java. Enkapsulasi dilakukan lewat pengelompokan data dan perilaku dalam class, serta konvensi awalan `_` untuk method internal.

**Contoh kode umum:**

```python
class Rekening:
    def __init__(self, saldo):
        self._saldo = saldo              # data dibungkus (awalan _ = internal)

    def tarik(self, jumlah):             # satu-satunya jalan mengubah saldo
        if jumlah > self._saldo:
            raise ValueError("Saldo tidak cukup")
        self._saldo -= jumlah
```
#### Penjelasan detail: `add_exp()`

```python
# models.py: CustomUser
def add_exp(self, points):
    self.exp += points
    self.save()
```

**Apa yang dilakukan method ini**

| Baris | Fungsi |
|---|---|
| `def add_exp(self, points)` | Method milik objek `CustomUser`. `self` adalah user yang sedang dipegang, `points` adalah jumlah EXP yang ditambahkan. |
| `self.exp += points` | Menambah atribut `exp` milik user itu. |
| `self.save()` | Menyimpan perubahan ke database, supaya EXP tidak hilang saat halaman dimuat ulang. |

Cara memakainya:

```python
user.add_exp(50)    # EXP bertambah 50 dan langsung tersimpan
```

**Mengapa ini enkapsulasi**

1. **Data dan perilaku dibungkus dalam satu class.** Atribut `exp` dan operasi yang mengubahnya (`add_exp`) sama-sama berada di `CustomUser`. Ini inti enkapsulasi: data tidak berdiri sendiri, ia dibungkus bersama method yang mengelolanya.
2. **Aturan perubahan ditulis satu kali.** Langkah "tambah EXP, lalu simpan" ada di satu tempat. Pemanggil cukup menulis `user.add_exp(50)` tanpa tahu atau mengulang langkah di dalamnya.
3. **Perubahan aturan cukup di satu tempat.** Kalau besok EXP perlu dibatasi (misalnya tidak boleh negatif) atau perlu memicu notifikasi, cukup ubah `add_exp()`. Semua pemanggil otomatis ikut.

**Perbandingan**

```python
# Tanpa enkapsulasi: langkah ditulis ulang di setiap tempat yang membutuhkan
user.exp += 50
user.save()

# Dengan enkapsulasi: pemanggil hanya memberi perintah
user.add_exp(50)
```

**Analogi: mesin ATM.** Saldo tidak bisa kamu ubah langsung. Kamu memakai menu setor atau tarik, dan menu itu yang menjalankan aturannya. Di sini, `exp` adalah saldo dan `add_exp()` adalah menu setor.

**Pertanyaan yang mungkin muncul**

**Q: Mengapa `add_exp()` termasuk enkapsulasi?**
A: Karena data (`exp`) dan perilaku yang mengubahnya (`add_exp`) dibungkus dalam satu class, dan pemanggil mengubah EXP lewat method itu, bukan dengan menulis ulang langkahnya sendiri.

**Q: Apa gunanya `self.save()` di dalam method?**
A: Mengubah atribut hanya mengubah objek di memori. `save()` menuliskannya ke database agar tidak hilang.

**Q: Apakah `exp` benar-benar tersembunyi dari luar?**
A: Tidak sepenuhnya. Python tidak punya `private` yang ketat, jadi `user.exp` tetap bisa dibaca dan diubah langsung. Enkapsulasi di Python berupa pengelompokan data dengan method dan kesepakatan pemakaian, bukan penguncian.

**Q: Apa bedanya dengan `update_streak()`?**
A: Idenya sama, yaitu aturan dibungkus dalam method. `add_exp()` sederhana (tambah lalu simpan), sedangkan `update_streak()` punya aturan lebih banyak (cek target harian, cek hari kemarin, mulai ulang streak).

**Catatan jujur**

- `add_exp()` belum memeriksa nilai `points` (misalnya negatif), jadi pembungkusnya masih sederhana.
- `self.save()` menyimpan semua field. Di bagian lain proyek, `save(update_fields=[...])` dipakai untuk menyimpan sebagian saja.
- Di `waktu_baca` (`views.py`), EXP ditambah langsung (`user.exp += exp_gain`) lalu disimpan dengan `update_fields`, bukan lewat `add_exp()`. Cari `add_exp(` dengan `Ctrl+F` di `views.py` dan `views_admin.py` untuk melihat di mana method ini benar-benar dipanggil. Kalau penguji bertanya, tunjukkan pemanggilnya, dan kalau tidak ada, jawab jujur bahwa method ini disiapkan sebagai antarmuka resmi untuk menambah EXP.


Potongan kode proyek ada di bagian 4.3 (`add_exp`, `update_streak`, `reset_streak_if_expired`).

### 3.2 Abstraction (Abstraksi)

**Pengertian:** menyembunyikan detail rumit dan hanya menampilkan hal yang perlu. Bentuknya bisa berupa class kerangka yang tidak dibuat objeknya langsung, atau lapisan yang menyembunyikan proses di baliknya.

**Analogi: mengemudi mobil.** Pengemudi memakai setir dan pedal gas tanpa perlu tahu bagaimana mesin membakar bahan bakar. Contoh lain: denah gedung yang hanya menggambar ruangan, tanpa menggambar tiap kabel dan pipa.

**Contoh kode umum** (abstract class murni Python):

```python
from abc import ABC, abstractmethod

class Bentuk(ABC):                  # kerangka, tidak bisa dibuat objeknya
    @abstractmethod
    def luas(self): ...

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):                 # subclass wajib mengisi detailnya
        return self.sisi ** 2

# Bentuk()  ->  TypeError (class abstrak tidak bisa diinstansiasi)
```
Potongan kode proyek ada di bagian 4.1 (`ItemKatalog` dan ORM).

#### Penjelasan detail: `ItemKatalog` (abstract base class)

```python
# models.py
class ItemKatalog(models.Model):
    id_item = models.CharField(max_length=20, unique=True, primary_key=True)
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    tahun_terbit = models.CharField(max_length=4, blank=True)
    cover = models.URLField(blank=True, null=True)
    tanggal_ditambahkan = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
```

**Apa yang dilakukan class ini**

| Bagian | Fungsi |
|---|---|
| `class ItemKatalog(models.Model)` | Class model Django yang mewarisi `models.Model`. |
| `id_item` | Kunci utama item katalog. Bisa berupa id buku seperti `OL1234567W`. |
| `judul`, `penulis`, `tahun_terbit`, `cover` | Atribut yang dimiliki **semua** item katalog, baik buku maupun jurnal. |
| `tanggal_ditambahkan` | Waktu item masuk katalog, default waktu sekarang. |
| `class Meta: abstract = True` | Menandai class ini sebagai **kerangka**. Django tidak membuat tabel untuknya. |

**Siapa yang memakainya**

```python
class BukuDigital(ItemKatalog):    # tabel sendiri: atribut ItemKatalog + isbn, link_unduh, ...
    ...

class Jurnal(ItemKatalog):         # tabel sendiri: atribut ItemKatalog + issn, volume, ...
    ...
```

Tabel `BukuDigital` dan `Jurnal` masing-masing mendapat salinan field `ItemKatalog`. Tidak ada tabel `ItemKatalog`.

**Mengapa ini abstraksi**

1. **Hanya cetak biru.** `ItemKatalog` tidak mewakili item nyata apa pun. Ia hanya mendefinisikan apa yang dimiliki *semua* item katalog.
2. **Tidak bisa dibuat objeknya langsung.** Mencoba `ItemKatalog()` ditolak Django dengan error (`Abstract models cannot be instantiated`). Hanya subclass yang bisa dibuat.
3. **Detail diserahkan ke subclass.** Hal yang khusus (ISBN untuk buku, ISSN untuk jurnal) tidak dipaksakan di sini. `BukuDigital` dan `Jurnal` menambahkan sendiri.
4. **Hanya yang umum yang ditampilkan.** Kamu cukup tahu "setiap item katalog punya judul, penulis, tahun, cover", tanpa tahu apakah itu buku atau jurnal.

**Hubungannya dengan pewarisan**

Abstraksi dan pewarisan bekerja bersama di sini. Abstraksi menentukan **apa yang dibagi** (`ItemKatalog` sebagai kerangka), pewarisan menentukan **cara membagikannya** (`BukuDigital(ItemKatalog)` dan `Jurnal(ItemKatalog)`). Hasilnya atribut dasar tidak ditulis dua kali (prinsip DRY).

**Analogi: formulir kosong di loket.** Formulir dasar berisi kolom nama, alamat, dan tanggal. Formulir itu sendiri tidak diserahkan ke siapa pun. Tiap layanan memakai salinannya lalu menambah kolom khusus. Di sini, `ItemKatalog` adalah formulir dasar, `BukuDigital` dan `Jurnal` adalah formulir yang sudah ditambah kolom khusus.

**Komentar `ENKAPSULASI` di dalam class**

Di kodemu ada komentar bahwa field di class ini juga contoh enkapsulasi, karena atribut data dikelompokkan dalam satu class. Itu benar dalam arti paling dasar (data dibungkus sebagai field class). Tetapi `ItemKatalog` tidak punya method yang mengatur perubahan datanya. Untuk contoh enkapsulasi yang lebih kuat, tunjuk `CustomUser` (`add_exp`, `update_streak`, `reset_streak_if_expired`).

**Pertanyaan yang mungkin muncul**

**Q: Apa arti `abstract = True`?**
A: Class itu hanya cetak biru. Django tidak membuat tabelnya, dan objeknya tidak bisa dibuat langsung. Field-nya disalin ke tabel subclass.

**Q: Kenapa `BukuDigital` dan `Jurnal` dibuat dari `ItemKatalog`?**
A: Keduanya punya atribut yang sama (id, judul, penulis, tahun, cover, tanggal). Dengan abstract base class, atribut itu ditulis sekali dan diwarisi keduanya.

**Q: Apa bedanya dengan `abc.ABC` di Python?**
A: `abc.ABC` dengan `@abstractmethod` memaksa subclass mengimplementasikan method tertentu. `ItemKatalog` adalah abstract base *model* Django: ia tidak memaksa method, tetapi tidak membuat tabel dan tidak bisa dibuat objeknya langsung.

**Q: Kalau `ItemKatalog` tidak membuat tabel, di mana datanya disimpan?**
A: Di tabel masing-masing subclass. Tabel `BukuDigital` dan `Jurnal` sama-sama punya kolom `id_item`, `judul`, `penulis`, dan seterusnya.

**Q: Apa bedanya abstraksi dan pewarisan di sini?**
A: Abstraksi: `ItemKatalog` sebagai kerangka umum yang tidak berdiri sendiri. Pewarisan: `BukuDigital` dan `Jurnal` mengambil atribut dari kerangka itu dan menambah milik sendiri.

**Q: Kenapa tidak membuat satu class `Item` saja?**
A: Buku punya ISBN dan format file, jurnal punya ISSN dan volume. Satu class berisi semuanya akan penuh kolom yang tidak terpakai. Dengan kerangka umum dan dua subclass, tiap class hanya berisi yang relevan.

**Catatan jujur**

- Ini abstraksi gaya Django (abstract base model), bukan `abc.ABC`. Jelaskan seperti itu supaya tidak dianggap keliru.
- `id_item` memakai `unique=True` dan `primary_key=True` sekaligus. Kunci utama sudah otomatis unik, jadi `unique=True` redundan. Tidak merusak apa pun, dan tidak perlu diubah sebelum pengujian.
- Class ini belum punya method sendiri, jadi abstraksinya berupa **kerangka atribut**, bukan kerangka perilaku.

### 3.3 Inheritance (Pewarisan)

**Pengertian:** sebuah class (anak/subclass) mewarisi atribut dan method dari class lain (induk/superclass), lalu boleh menambah atau mengubah. Hubungannya **"is-a"**: anak adalah jenis dari induk.

**Analogi: pewarisan dalam keluarga.** Anak mewarisi sifat orang tua tetapi punya ciri sendiri. Contoh lain: formulir baku berisi nama dan alamat, lalu formulir peminjaman menambah kolom khusus tanpa menulis ulang kolom dasar.

**Contoh kode umum:**

```python
class Hewan:                        # induk
    def __init__(self, nama):
        self.nama = nama

class Kucing(Hewan):                # anak: nama induk ditulis di dalam kurung
    def mengeong(self):
        return f"{self.nama}: meong"

k = Kucing("Mimi")
print(k.nama)                       # atribut diwarisi dari Hewan
print(k.mengeong())                 # method milik Kucing sendiri
```

Potongan kode proyek ada di bagian 4.2.

### 3.4 Polymorphism (Polimorfisme)

**Pengertian:** "banyak bentuk". Satu nama method atau satu cara pemanggilan bisa menghasilkan **perilaku berbeda** tergantung objek yang menerimanya. Bentuk yang paling umum adalah **method overriding**: subclass menulis ulang method milik induk dengan perilaku sendiri.

**Analogi: tombol "Play".** Tombol yang sama ada di pemutar musik, video, dan podcast. Cara menekannya sama, tetapi yang terjadi berbeda. Contoh lain: guru berkata "Bersuara!" ke kucing dan anjing; perintahnya sama, kucing mengeong dan anjing menggonggong.

**Catatan Python:** Python tidak mendukung method overloading (nama sama dengan parameter berbeda) seperti Java. Polimorfisme di Python muncul lewat overriding dan duck typing.

**Contoh kode umum:**

```python
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."

class Kucing(Hewan):
    def suara(self):                # overriding
        return "meong"

class Anjing(Hewan):
    def suara(self):                # overriding
        return "guk"

for h in (Kucing("Mimi"), Anjing("Bobi")):
    print(h.suara())                # pemanggilan sama, hasil berbeda: meong / guk
```

Potongan kode proyek ada di bagian 4.4.

### 3.5 Relasi antarobjek: asosiasi, agregasi, komposisi, dependensi

Objek jarang berdiri sendiri. Ada empat tingkat keterikatan, dari yang paling longgar ke yang paling erat:

| Relasi | Makna | Siklus hidup | Analogi | Lambang UML |
|---|---|---|---|---|
| **Dependensi** | "memakai sementara" | tidak terikat sama sekali | tukang memakai palu untuk satu pekerjaan | panah putus-putus |
| **Asosiasi** | "berhubungan" | masing-masing hidup sendiri | anggota dan buku yang dihubungkan kartu peminjaman | garis |
| **Agregasi** | "memiliki" (lemah, has-a) | bagian **bisa hidup tanpa** induk | perpustakaan dan bukunya: perpustakaan tutup, buku tetap ada | belah ketupat **kosong** |
| **Komposisi** | "memiliki" (kuat, has-a) | bagian **ikut hilang** bersama induk | rumah dan kamarnya: rumah dibongkar, kamar ikut hilang | belah ketupat **terisi** |

Pertanyaan cepat untuk membedakan agregasi dan komposisi: *"kalau induknya dihapus, apakah bagiannya masih bermakna?"* Masih → agregasi. Tidak → komposisi.

#### Asosiasi

**Pengertian:** objek saling berhubungan, dan satu objek menyimpan referensi ke objek lain tanpa menyalin datanya. Di Django bentuknya `ForeignKey`.

**Analogi:** kartu peminjaman di perpustakaan fisik mencatat anggota mana meminjam buku mana. Kartu itu tidak menyalin buku, hanya menunjuk ke keduanya.

**Contoh kode umum:**

```python
class Anggota:
    def __init__(self, nama):
        self.nama = nama

class Buku:
    def __init__(self, judul):
        self.judul = judul

class Peminjaman:                       # menghubungkan dua objek
    def __init__(self, anggota, buku):
        self.anggota = anggota          # hanya menunjuk, tidak menyalin
        self.buku = buku

budi = Anggota("Budi")
b1 = Buku("Algoritma")
pinjam = Peminjaman(budi, b1)
```

#### Agregasi

**Pengertian:** induk memegang objek bagian, tetapi bagian itu dibuat dan hidup di luar induk. Induk dihapus, bagian tetap ada dan bisa dipakai induk lain.

**Analogi:** perpustakaan dan buku-bukunya. Perpustakaan ditutup, bukunya masih ada dan bisa dipindah ke perpustakaan lain.

**Contoh kode umum:**

```python
class Perpustakaan:
    def __init__(self, daftar_buku):
        self.daftar_buku = daftar_buku  # buku dibuat DI LUAR, hanya dititipkan

b1 = Buku("Algoritma")
b2 = Buku("Basis Data")
p = Perpustakaan([b1, b2])
del p                                   # perpustakaan hilang...
print(b1.judul)                         # ...buku tetap ada
```

#### Komposisi

**Pengertian:** induk membuat dan memiliki bagiannya. Bagian tidak bermakna tanpa induk, dan siklus hidupnya terikat: induk dihapus, bagian ikut hilang.

**Analogi:** rumah dan kamar-kamarnya. Kamar tidak bisa berdiri sendiri; rumah dibongkar, kamarnya ikut hilang.

**Contoh kode umum:**

```python
class Kamar:
    def __init__(self, nama):
        self.nama = nama

class Rumah:
    def __init__(self):
        self.kamar = [Kamar("Tidur"), Kamar("Mandi")]   # dibuat DI DALAM Rumah

# Rumah dihapus -> kamar-kamarnya ikut hilang, tidak ada di tempat lain
```

#### Dependensi

**Pengertian:** satu class atau fungsi memakai objek lain **sementara** (sebagai parameter atau variabel lokal) tanpa menyimpannya sebagai atribut.

**Analogi:** tukang meminjam palu untuk satu pekerjaan, lalu mengembalikannya.

**Contoh kode umum:**

```python
def cetak_struk(transaksi):
    total = transaksi.hitung_total()    # hanya memakai, tidak disimpan
    print(f"Total: {total}")
```

Di Django, asosiasi, agregasi, dan komposisi diwujudkan lewat `ForeignKey` dan `on_delete`. Potongan kode proyek ada di bagian 4.5.

### 3.6 Ringkasan

| Pilar | Inti | Kata kunci | Analogi |
|---|---|---|---|
| Encapsulation | Data dan method dibungkus, akses terkontrol | bundling, aturan | ATM |
| Abstraction | Sembunyikan detail, tampilkan yang perlu | kerangka, penyederhanaan | Mengemudi mobil |
| Inheritance | Anak mewarisi induk | is-a, reuse | Keluarga |
| Polymorphism | Nama sama, perilaku beda | overriding | Tombol Play |
| Dependensi | Memakai sementara | parameter, variabel lokal | Tukang dan palu |
| Asosiasi | Berhubungan | atribut referensi | Kartu peminjaman |
| Agregasi | Has-a lemah | bagian hidup sendiri | Perpustakaan dan buku |
| Komposisi | Has-a kuat | bagian ikut hilang | Rumah dan kamar |

---

## 4. Penerapan OOP di Proyek

### 4.1 Abstraction — `ItemKatalog` (`models.py`)

```python
class ItemKatalog(models.Model):
    id_item = models.CharField(max_length=20, unique=True, primary_key=True)
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    tahun_terbit = models.CharField(max_length=4, blank=True)
    cover = models.URLField(blank=True, null=True)
    tanggal_ditambahkan = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
```

**Mengapa ini abstraksi:**
- `abstract = True` membuat class ini hanya cetak biru. Django tidak membuat tabel untuknya, dan objeknya tidak bisa dibuat langsung (Django menolaknya).
- Ia hanya memuat atribut umum item katalog. Detail khusus diserahkan ke subclass.
- Abstraksi lain: **ORM Django**. Kode `BukuDigital.objects.filter(...)` menyembunyikan SQL di baliknya.

**Catatan:** ini abstraksi gaya Django (abstract base model), bukan `abc.ABC` dengan `@abstractmethod`. Jelaskan seperti itu bila ditanya.

**Potongan kode abstraksi lain: ORM** (`views.py`, `katalog_view`)

```python
buku_queryset = BukuDigital.objects.all().distinct()
...
buku_queryset = buku_queryset.filter(
    Q(judul__icontains=search_query) |
    Q(penulis__icontains=search_query) |
    Q(kategori__icontains=search_query) |
    Q(deskripsi__icontains=search_query)
).distinct()
```

Tidak ada satu baris SQL pun yang ditulis. ORM menyembunyikan pembuatan query dan koneksi database, dan kamu cukup memakai method `filter()` dan objek `Q`.

### 4.2 Inheritance (Pewarisan)

| Subclass | Induk | Yang diwarisi | Yang ditambah |
|---|---|---|---|
| `BukuDigital` | `ItemKatalog` | id_item, judul, penulis, tahun_terbit, cover, tanggal_ditambahkan | kategori, isbn, link_unduh, ukuran_file, format_file, deskripsi |
| `Jurnal` | `ItemKatalog` | atribut yang sama | kategori, issn, volume, bidang_ilmu, link_akses |
| `CustomUser` | `AbstractUser` (Django) | username, password, login, permission | is_admin, nama_tampilan, foto_profil, exp, streak_days, OTP, dan lainnya |
| `AchievementGambarAdmin` | `admin.ModelAdmin` | seluruh fitur admin bawaan | list_display, list_filter, search_fields, preview gambar |
| `LocalCatalogLoanFlowTests` dkk. | `django.test.TestCase` | client, database tes, assertion | tes khusus proyek |

**Mengapa ini pewarisan:** hubungannya "is-a". `BukuDigital` **adalah** `ItemKatalog`, dan `CustomUser` **adalah** `AbstractUser`. Atribut induk tidak ditulis ulang (prinsip DRY).

**Potongan kode:**

```python
# models.py: turunan dari class buatan sendiri
class BukuDigital(ItemKatalog):
    kategori = models.CharField(max_length=50, default="", blank=True)
    isbn = models.CharField(max_length=20, blank=True, default="")
    link_unduh = models.URLField(default="https://example.com")
    ukuran_file = models.FloatField(default=2.5, help_text="dalam MB")
    format_file = models.CharField(max_length=10, default="PDF")
    deskripsi = models.TextField(blank=True, default="")

class Jurnal(ItemKatalog):
    kategori = models.CharField(max_length=50, default="", blank=True)
    issn = models.CharField(max_length=9, blank=True, default="")
    volume = models.CharField(max_length=50, blank=True)
    bidang_ilmu = models.CharField(max_length=100, blank=True)
    link_akses = models.URLField(default="https://example.com")

# models.py: turunan dari class bawaan Django
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    nama_tampilan = models.CharField(max_length=100)
    exp = models.IntegerField(default=0)
    streak_days = models.IntegerField(default=0)
    # ... field lain

# admin.py
class AchievementGambarAdmin(admin.ModelAdmin):
    ...

# tests.py
class LocalCatalogLoanFlowTests(TestCase):
    ...
```

Nama induk ditulis di dalam kurung setelah nama class (`class BukuDigital(ItemKatalog)`). Itulah sintaks pewarisan di Python.

**Pewarisan di template:** `kelola_buku.html` memakai `{% extends 'perpustakaan/base_admin.html' %}` dan hanya mengisi `{% block %}`. Ini ide yang sama: kerangka di induk, isi khusus di anak.
(`dashboard.html` dan `baca.html` **tidak** memakai `{% extends %}`; keduanya halaman mandiri.)

```django
{# kelola_buku.html #}
{% extends 'perpustakaan/base_admin.html' %}

{% block title %}Kelola Buku · Lentera{% endblock %}
{% block page_title %}Kelola Buku{% endblock %}

{% block content %}
  ... isi khusus halaman ini ...
{% endblock %}
```

### 4.3 Encapsulation (Enkapsulasi)

**a. Data dan perilaku dibungkus dalam `CustomUser`:**

```python
def add_exp(self, points):
    self.exp += points
    self.save()

def update_streak(self):
    today = timezone.localdate()
    if (self.tanggal_baca_harian != today
        or self.detik_baca_hari_ini < TARGET_HARIAN_DETIK
        or self.last_read_date == today):
        return
    if self.last_read_date == today - timedelta(days=1):
        self.streak_days += 1
    elif not self.last_read_date or self.last_read_date < today - timedelta(days=1):
        self.streak_days = 1
    self.last_read_date = today
    self.save()

def reset_streak_if_expired(self):
    """Hapus streak yang sudah melewatkan satu hari tanpa target baca."""
    today = timezone.localdate()
    if (
        self.streak_days
        and self.last_read_date
        and self.last_read_date < today - timedelta(days=1)
    ):
        self.streak_days = 0
        self.save(update_fields=["streak_days"])
```

**Mengapa ini enkapsulasi:** data (`exp`, `streak_days`, `last_read_date`) dan aturan yang mengubahnya berada di satu objek. View `waktu_baca` cukup memanggil `user.update_streak()` tanpa menulis ulang aturan streak. Kalau aturan berubah, cukup diubah di satu tempat.

**b. `@property` sebagai antarmuka baca:** `kategori_label`, `nama_asli`, dan `ikon_tampil` dihitung dari data lain dan dibaca seperti atribut biasa (`user.nama_asli`).

```python
# models.py: CustomUser
@property
def nama_asli(self):
    nama_lengkap = self.get_full_name().strip()
    if nama_lengkap:
        return nama_lengkap
    nama = (self.nama_tampilan or "").strip()
    if nama.startswith("User_") and nama[5:].isdigit():
        return self.username
    return nama or self.username

# models.py: BukuDigital
@property
def kategori_label(self):
    return label_kategori(self.kategori)
```

Template cukup menulis `{{ user.nama_asli }}` atau `{{ buku.kategori_label }}`, tanpa tanda kurung dan tanpa tahu aturan di baliknya.

**c. Method internal berawalan `_`:** `_preview` dan `_ikon` di `admin.py`, serta `_notifikasi`, `_pastikan_buku`, `_jatuh_tempo` di `views.py` adalah helper internal. Pemakai class hanya memakai pintu masuknya.

**d. Pola singleton di `Pengaturan`:** `save()` memaksa `pk = 1` dan `muat()` memakai `get_or_create(pk=1)`, jadi aturan "hanya satu baris pengaturan" dikunci di dalam class, bukan diserahkan ke pemanggil.

```python
# models.py
class Pengaturan(models.Model):
    masa_pinjam_hari = models.PositiveIntegerField(default=14)

    def save(self, *args, **kwargs):
        self.pk = 1                          # selalu baris nomor 1
        super().save(*args, **kwargs)

    @classmethod
    def muat(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
```

`Pengaturan.muat()` dipanggil dari class, tanpa membuat objek lebih dulu (`@classmethod`).

### 4.4 Polymorphism — dan mengapa contoh-contoh ini termasuk

#### Uji empat ciri

Sebuah contoh dihitung polimorfisme bila memenuhi:

1. Ada hubungan class (induk dan anak, atau beberapa class yang berbagi antarmuka).
2. Method yang **namanya sama**.
3. Dipanggil dengan **cara yang sama**.
4. **Hasil atau perilakunya berbeda** tergantung objeknya.

#### Contoh 1: `__str__` (contoh paling kuat)

Semua model mewarisi `models.Model` (yang punya `__str__` bawaan). Tiap class menimpanya:

| Class | Hasil `str(objek)` |
|---|---|
| `BukuDigital` | `[Digital] <judul>` |
| `Jurnal` | `[Jurnal] <judul>` |
| `Peminjaman` | `<username> <item> (<status>)` |
| `Bookmark` | `<username> saved <item>` |
| `Achievement` | `[<kategori>] <nama>` |
| `AchievementGambar` | `[<kategori>] <nama>` |
| `UserAchievement` | `<username> <nama achievement>` |
| `Notifikasi` | `<username>: <judul>` |
| `CustomUser` | `<username>` |
| `Pengaturan` | `Masa pinjam: <n> hari` |

**Potongan kode:**

```python
# models.py: BukuDigital
def __str__(self):
    return f"[Digital] {self.judul}"

# models.py: Jurnal
def __str__(self):
    return f"[Jurnal] {self.judul}"

# models.py: Notifikasi
def __str__(self):
    return f"{self.user.username}: {self.judul}"
```

Cara memanggilnya sama untuk semua objek:

```python
for obj in (buku, jurnal):
    print(obj)
# [Digital] Buku Tes Lokal
# [Jurnal] <judul jurnal>
```

**Mengapa ini polimorfisme:**
1. Ada hierarki: semua mewarisi `models.Model`.
2. Nama method sama: `__str__`.
3. Dipanggil dengan cara yang sama: `str(objek)` atau `print(objek)`. Halaman admin juga memanggilnya otomatis untuk menampilkan nama tiap data.
4. Hasilnya berbeda per class.

Ini disebut **method overriding**: subclass menimpa method milik induk.

#### Contoh 2: polimorfisme yang terjadi sungguhan di `Peminjaman.__str__`

```python
def __str__(self):
    item = self.buku_digital or self.jurnal
    return f"{self.user.username} {item} ({self.status})"
```

Variabel `item` bisa berisi `BukuDigital` **atau** `Jurnal`. Kode yang sama (`f"{item}"`) memanggil `__str__` milik class yang sedang dipegang:

- jika `item` adalah buku → `[Digital] Buku Tes Lokal`
- jika `item` adalah jurnal → `[Jurnal] Judul Jurnal`

Kode pemanggil tidak perlu memeriksa tipe objeknya. Itulah inti polimorfisme: **pemanggil memperlakukan beberapa jenis objek dengan cara yang sama, dan tiap objek menjalankan versinya sendiri.**

#### Contoh 3: `Pengaturan.save()`

```python
def save(self, *args, **kwargs):
    self.pk = 1
    super().save(*args, **kwargs)
```

`save()` milik `Model` ditimpa dengan perilaku tambahan (memaksa satu baris), lalu `super().save()` menjalankan versi induk. Perilaku `save()` di `Pengaturan` **benar-benar berbeda** dari `save()` pada model lain.

#### Contoh 4: `AchievementGambarAdmin` menimpa atribut `ModelAdmin`

`list_display`, `list_filter`, dan `search_fields` mengganti nilai bawaan `ModelAdmin`. Mekanisme admin Django tetap sama untuk semua model, tetapi tampilan tiap model berbeda.

```python
# admin.py
@admin.register(AchievementGambar)
class AchievementGambarAdmin(admin.ModelAdmin):
    list_display = ("nama", "kategori", "tipe_syarat", "target",
                    "preview_terkunci", "preview_terbuka")
    list_filter = ("kategori", "tipe_syarat")
    search_fields = ("nama", "deskripsi")
```

#### Contoh 5: `setUp()` di `tests.py`

Semua class tes mewarisi `TestCase`. Test runner memanggil `setUp()` dengan cara yang sama untuk tiap class, dan isinya berbeda: membuat user dan buku untuk satu class, hanya user untuk class lain.

```python
# tests.py
class LocalCatalogLoanFlowTests(TestCase):
    def setUp(self):                         # menimpa setUp() milik TestCase
        self.user = CustomUser.objects.create_user(
            username='catalog-test',
            password='test-password',
        )
        self.book = BukuDigital.objects.create(...)
        self.client.force_login(self.user)

class CollectionPaginationTests(TestCase):
    def setUp(self):                         # nama sama, isi berbeda
        self.user = CustomUser.objects.create_user(
            username='pagination-test',
            password='test-password',
        )
        self.client.force_login(self.user)
```

#### Contoh yang lemah (jujur)

`CustomUser.save()` saat ini hanya berisi `super().save(*args, **kwargs)`. Secara teknis itu overriding, tetapi **perilakunya belum berbeda** dari induk. Jangan jadikan contoh utama. Gunakan `__str__`, `Peminjaman.__str__`, dan `Pengaturan.save()`.

### 4.5 Relasi antarobjek: asosiasi, agregasi, komposisi, dependensi

Django mewujudkan relasi antarobjek lewat `ForeignKey`. Jenis relasinya ditentukan oleh `on_delete`: `SET_NULL` (dengan `null=True`) mengarah ke **agregasi**, sedangkan `CASCADE` mengarah ke **komposisi**.

> Pemetaan ini adalah tafsiran konseptual. Django tidak punya kata kunci "agregasi" atau "komposisi", dan komentar di `models.py` hanya menyebut "asosiasi antarobjek". Jelaskan sebagai **perilaku** hasil `on_delete`.

#### Asosiasi: `Peminjaman` dan `Bookmark`

```python
# models.py
class Peminjaman(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    buku_digital = models.ForeignKey(
        BukuDigital, null=True, blank=True, on_delete=models.SET_NULL
    )
    jurnal = models.ForeignKey(
        Jurnal, null=True, blank=True, on_delete=models.SET_NULL
    )

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    buku_digital = models.ForeignKey(
        BukuDigital, null=True, blank=True, on_delete=models.CASCADE
    )
    jurnal = models.ForeignKey(
        Jurnal, null=True, blank=True, on_delete=models.CASCADE
    )
```

**Mengapa asosiasi:** kedua class menghubungkan `CustomUser` dengan item katalog lewat **referensi**, tanpa menyalin data buku atau user. Keduanya juga membawa atribut sendiri (`status`, `progress_baca`, `tanggal_pinjam`, `tanggal_disimpan`). Dalam UML, class seperti ini disebut **kelas asosiasi** (tabel penghubung): satu user boleh meminjam banyak item, dan satu item boleh dipinjam banyak user.

#### Agregasi: `Peminjaman` ke `BukuDigital` / `Jurnal`

```python
buku_digital = models.ForeignKey(
    BukuDigital, null=True, blank=True, on_delete=models.SET_NULL
)

# Efeknya:
buku.delete()
# Peminjaman TETAP ada; kolom buku_digital menjadi NULL
```

**Mengapa agregasi:** buku dan jurnal hidup sendiri di katalog. Kalau buku dihapus admin, riwayat peminjaman tetap tersimpan. Bagian (buku) tidak ikut terhapus bersama pemegang referensinya, dan sebaliknya.

#### Komposisi: `Notifikasi` dan `UserAchievement` ke `CustomUser`

```python
# models.py
class Notifikasi(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifikasi"
    )

class UserAchievement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_achievements'
    )
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

# Efeknya:
user.delete()
# Notifikasi dan UserAchievement milik user itu ikut terhapus

# related_name memberi jalan balik dari user ke bagiannya:
user.notifikasi.all()
```

**Mengapa komposisi:** notifikasi dan catatan pencapaian hanya bermakna bagi satu user dan siklus hidupnya mengikuti user itu (`CASCADE`). `Peminjaman.user` dan `Bookmark.user` juga memakai `CASCADE`, jadi riwayat dan bookmark milik user ikut hilang bersamanya.

**Batasan jujur:** komposisi murni berarti bagian tidak punya identitas sendiri, sedangkan di Django tiap model tetap punya id dan tabel sendiri. Karena itu sebut sebagai "mendekati komposisi", bukan "komposisi sempurna".

#### Dependensi: view memakai model

```python
# views.py: waktu_baca (disingkat)
user = request.user
user.reset_streak_if_expired()
...
user.update_streak()
...
_notifikasi(user, "gamifikasi", "EXP bertambah", f"Kamu mendapatkan {exp_gain} EXP dari membaca.", "profil")
peringkat_baru = 1 + CustomUser.objects.filter(is_member=True, is_admin=False, exp__gt=user.exp).count()
```

**Mengapa dependensi:** fungsi `waktu_baca` hanya **memakai** `CustomUser` dan `_notifikasi` selama fungsinya berjalan. Tidak ada atribut yang menyimpannya. View bergantung pada model, tetapi tidak memilikinya.

#### Pemetaan cepat

| Relasi di kode | `on_delete` | Jenis | Pertanyaan pembeda |
|---|---|---|---|
| `Peminjaman` → `BukuDigital` / `Jurnal` | `SET_NULL` | Agregasi | Buku dihapus, riwayat tetap ada |
| `Notifikasi` → `CustomUser` | `CASCADE` | Komposisi | User dihapus, notifikasi ikut hilang |
| `UserAchievement` → `CustomUser` | `CASCADE` | Komposisi | User dihapus, catatan pencapaian ikut hilang |
| `Bookmark` → user dan item | `CASCADE` | Asosiasi | Bergantung pada dua pihak sekaligus |
| `waktu_baca` memakai `CustomUser` | tidak ada | Dependensi | Hanya dipakai sementara dalam fungsi |

#### Ringkasan `ForeignKey` di proyek

| Class | Relasi | `on_delete` |
|---|---|---|
| `Peminjaman` | `user`, `buku_digital`, `jurnal` | user: `CASCADE`; buku dan jurnal: `SET_NULL` |
| `Bookmark` | `user`, `buku_digital`, `jurnal` | semuanya `CASCADE` |
| `UserAchievement` | `user`, `achievement` | `CASCADE` |
| `Notifikasi` | `user` | `CASCADE` |

- `CASCADE`: data induk dihapus → data terkait ikut dihapus.
- `SET_NULL`: data induk dihapus → kolom relasinya dikosongkan. Riwayat peminjaman tetap ada walau bukunya dihapus.

### 4.6 Peta cepat: pilar → lokasi

| Pilar | Lokasi utama |
|---|---|
| Abstraction | `ItemKatalog` (`models.py`), ORM |
| Inheritance | `BukuDigital`, `Jurnal`, `CustomUser`, `AchievementGambarAdmin`, class tes; `{% extends %}` di `kelola_buku.html` |
| Encapsulation | `CustomUser.add_exp / update_streak / reset_streak_if_expired`, `@property`, helper `_...`, `Pengaturan.muat()` |
| Polymorphism | `__str__` di semua model, `Peminjaman.__str__`, `Pengaturan.save()`, `ModelAdmin`, `setUp()` |
| Asosiasi | `Peminjaman` dan `Bookmark` (menghubungkan user dengan buku atau jurnal) |
| Agregasi | `Peminjaman.buku_digital` dan `Peminjaman.jurnal` (`SET_NULL`) |
| Komposisi | `Notifikasi.user` dan `UserAchievement.user` (`CASCADE`) |
| Dependensi | `waktu_baca` memakai `CustomUser.update_streak()` dan `_notifikasi()` |

### 4.7 Konsep Pendukung (membantu menjawab pertanyaan lanjutan)

**a. DRY (Don't Repeat Yourself): satu logika dipakai dua kali** (`admin.py`)

```python
@admin.display(description="Gambar terkunci")
def preview_terkunci(self, obj):
    return self._preview(obj, terbuka=False)

@admin.display(description="Gambar terbuka")
def preview_terbuka(self, obj):
    return self._preview(obj, terbuka=True)
```

Dua method publik memanggil satu helper internal `_preview(obj, terbuka)` dengan parameter berbeda, jadi logikanya tidak ditulis dua kali.

**b. Dekorator: menambah perilaku tanpa mengubah isi fungsi** (`views.py`)

```python
@login_required(login_url="login")
@require_POST
def pinjam_buku(request, olid):
    ...
```

`@login_required` memaksa user login, dan `@require_POST` menolak akses selain POST. Isi fungsi tidak perlu mengecek keduanya lagi.

**c. Inner class `Meta`: pengaturan untuk model** (`models.py`)

```python
class ItemKatalog(models.Model):
    class Meta:
        abstract = True            # tidak membuat tabel

class Notifikasi(models.Model):
    class Meta:
        ordering = ["-dibuat", "-pk"]   # terbaru dulu

class Pengaturan(models.Model):
    class Meta:
        verbose_name_plural = "Pengaturan"
```

**d. Method biasa, `@property`, dan `@classmethod`**

| Jenis | Cara memanggil | Contoh di proyek |
|---|---|---|
| Method biasa | `user.add_exp(50)` | `add_exp`, `update_streak` |
| `@property` | `user.nama_asli` (tanpa kurung) | `nama_asli`, `kategori_label`, `ikon_tampil` |
| `@classmethod` | `Pengaturan.muat()` (dari class) | `Pengaturan.muat` |

**e. Pemisahan tanggung jawab (separation of concerns)**

| Lapisan | Hanya mengurus | Contoh |
|---|---|---|
| Model | data dan aturan objek | `update_streak()` |
| View | menerima request dan memilih data | `katalog_view` |
| Template | tampilan | `katalog.html` |
| URL | memetakan alamat ke view | `urls.py` |

Cara mengingatnya: aturan streak berada di model, bukan di view dan bukan di template. Itu sebabnya `update_streak()` bisa dites tanpa membuka halaman.

---

## 5. Penjelasan Kode Penting per File

### 5.1 `models.py`

- **`KATEGORI_PRODI` dan `label_kategori()`:** 10 program studi; `label_kategori` mengubah nilai (`teknik_sipil`) menjadi label (`Teknik Sipil`), dengan cadangan `replace("_", " ").title()`.
- **`TARGET_HARIAN_DETIK = 30 * 60`:** target baca harian 1800 detik.
- **`Peminjaman`:** punya dua `ForeignKey` yang boleh kosong (`buku_digital` dan `jurnal`) karena satu peminjaman berisi salah satunya. Field penting: `status` (`Dibaca`/`Selesai`), `progress_baca` (0–100), `waktu_baca_detik`, `perpanjangan`.
- **`Notifikasi`:** jenis `katalog`, `pengumuman`, `peminjaman`, `tenggat`, `gamifikasi`; diurutkan terbaru dulu lewat `Meta.ordering`.
- **`CustomUser`:** menambah `is_admin`, `is_member`, `menunggu_persetujuan`, profil, OTP, `exp`, `waktu_baca_detik`, `detik_baca_hari_ini`, `streak_days`, `last_read_date`, `max_loans`, `pinned_achievements`.
- **`Pengaturan`:** singleton berisi `masa_pinjam_hari` (default 14).
- **`AchievementGambar`:** achievement dengan gambar terkunci/terbuka, `tipe_syarat` (buku_selesai, buku_dimulai, genre, pinjam_total, pinjam_selesai, bookmark, exp, streak), dan `target`. `ikon_tampil` memakai urutan: field `ikon` → kamus `IKON_ACHIEVEMENT_BERSIH` → kosong.
- **`path_gambar_terkunci/terbuka`:** nama file upload diganti `uuid` agar unik dan aman.

### 5.2 `views.py` (potongan yang dilampirkan)

Semua view anggota memakai `@login_required(login_url="login")`. Aksi yang mengubah data (`pinjam_buku`, `perpanjang_buku`, `waktu_baca`) memakai `@require_POST`.

| View | Inti |
|---|---|
| `katalog_view` | Filter kategori + pencarian, kirim `buku_lokal` ke template |
| `pinjam_buku` | Validasi id, cek pinjaman ganda, cek batas, buat `Peminjaman` |
| `peminjaman_view` | Daftar pinjaman aktif + hitung slot |
| `perpanjang_buku` | Batasi jumlah perpanjangan, geser jatuh tempo |
| `kembalikan_buku` | Ubah status jadi `Selesai`, isi tanggal kembali |
| `waktu_baca` | Hitung EXP, target harian, streak, notifikasi |

### 5.3 Template

- **`dashboard.html`:** halaman mandiri. Menampilkan banner streak (`streak_hari`, `menit_hari_ini`, `target_menit`, `persen_target`), empat kartu statistik, rekomendasi buku, dan kartu "Lanjutkan Bacaan" (`bacaan_terakhir`). Sapaan dibuat JavaScript dari jam perangkat.
- **`baca.html`:** halaman baca layar penuh. Data dari Django dititipkan lewat atribut `data-*` (`data-link`, `data-progress-url`, `data-progress`, `data-pinjam`, `data-url`); `buku.js` dan PDF.js yang menampilkan PDF-nya.
- **`kelola_buku.html`:** halaman admin yang mewarisi `base_admin.html`. Berisi tabel koleksi, modal tambah/edit/hapus, hapus massal lewat checkbox yang dihubungkan ke form dengan atribut `form="formHapusMassal"`, dan `{% csrf_token %}` di setiap form POST.

Elemen Django Template Language yang dipakai: `{% load static %}`, `{% url %}`, `{% for %}…{% empty %}`, `{% if %}`, `{% extends %}`, `{% block %}`, `{% include %}`, `{% csrf_token %}`, serta filter `truncatechars`, `slice`, `upper`, `default`.

### 5.4 `admin.py`

Sebagian besar model didaftarkan dengan `admin.site.register(Model)` (tampilan bawaan). `AchievementGambar` memakai `@admin.register` dan class `AchievementGambarAdmin` dengan kolom, filter, pencarian, dan preview gambar (`_preview`, `_ikon`). Placeholder berwarna sesuai kategori: umum hijau, langka biru, epik ungu. `format_html` dipakai agar HTML aman dari XSS.

### 5.5 `tests.py`

Tes otomatis yang menjadi dokumentasi aturan bisnis:

| Class tes | Yang diuji |
|---|---|
| `LocalCatalogLoanFlowTests` | Alur katalog → pinjam → kembalikan → riwayat; 10 kategori prodi; filter kategori (nilai admin dan label lama) |
| `CollectionPaginationTests` | Pagination bookmark dan riwayat (10 per halaman); filter bookmark per kategori |
| `DailyReadingGoalTests` | Batas 30 menit per hari; streak naik; streak reset setelah melewatkan hari |
| `ProfileAndAdminRegressionTests` | Halaman profil dan achievement tampil; hitungan "dibaca"; toggle bookmark mengembalikan JSON; laporan admin tidak menghitung pinjaman admin; leaderboard (EXP tertinggi = peringkat 1) |

Hal yang berguna diingat: `refresh_from_db()` memuat ulang objek dari database karena view mengubahnya di database, sementara objek di tes masih menyimpan nilai lama.

---

#### Jenis-jenis pewarisan di proyek

| Jenis | Ada? | Contoh di kode |
|---|---|---|
| Single | Ya | `CustomUser(AbstractUser)`, `AchievementGambarAdmin(admin.ModelAdmin)` |
| Multilevel | Ya | `BukuDigital` → `ItemKatalog` → `models.Model` |
| Hierarchical | Ya | `ItemKatalog` → `BukuDigital` dan `Jurnal` |
| Multiple | Tidak ditulis sendiri | `AbstractUser` (Django) mewarisi `AbstractBaseUser` dan `PermissionsMixin` secara internal |
| Hybrid | Tidak ada | - |

**Single inheritance:** satu class mewarisi satu induk.

```python
class CustomUser(AbstractUser): ...
```

**Multilevel inheritance:** pewarisan berjenjang (kakek → ayah → anak).

```python
class ItemKatalog(models.Model):        # tingkat 1
    class Meta:
        abstract = True

class BukuDigital(ItemKatalog):         # tingkat 2
    ...
```

`BukuDigital` mendapat atribut dari `ItemKatalog` (judul, penulis, dan lainnya) dan method dari `models.Model` (`save()`, `delete()`, `objects`).

**Hierarchical inheritance:** satu induk, banyak anak.

```python
class BukuDigital(ItemKatalog): ...
class Jurnal(ItemKatalog): ...
```

Pola yang sama ada di `tests.py`, yaitu empat class tes yang semuanya mewarisi `TestCase`.

**Multiple inheritance:** satu class mewarisi lebih dari satu induk (`class C(A, B)`). Proyek ini tidak menulisnya sendiri. `CustomUser` hanya mendapatkannya secara tidak langsung lewat `AbstractUser` bawaan Django.

**Hybrid inheritance:** gabungan beberapa jenis di atas. Tidak ada di proyek ini.

**Analogi:**
- Single: anak dan orang tuanya.
- Multilevel: cucu, ayah, kakek (tiga generasi).
- Hierarchical: satu orang tua dengan dua anak (`BukuDigital` dan `Jurnal`).
- Multiple: anak yang mewarisi sifat ayah dan ibu sekaligus.

**Tanya-jawab:**

**Q: Jenis pewarisan apa yang kamu pakai di proyekmu?**
A: Multilevel, hierarchical, dan single. Multilevel: `BukuDigital` → `ItemKatalog` → `models.Model`. Hierarchical: `ItemKatalog` punya dua anak, `BukuDigital` dan `Jurnal`. Single: `CustomUser(AbstractUser)`.

**Q: Apakah kamu memakai multiple inheritance?**
A: Tidak saya tulis sendiri. `CustomUser` mewarisinya secara tidak langsung karena `AbstractUser` di Django mewarisi dua induk.

**Q: Kenapa `BukuDigital` termasuk multilevel?**
A: Karena rantai pewarisannya dua tingkat dalam kode saya: `BukuDigital(ItemKatalog)` dan `ItemKatalog(models.Model)`.

**Q: Kenapa `BukuDigital` dan `Jurnal` termasuk hierarchical?**
A: Karena keduanya anak dari satu induk yang sama, `ItemKatalog`.

## 6. Pertanyaan dan Jawaban

### A. Konsep OOP

**1. Apa itu OOP?**
Paradigma pemrograman yang memodelkan program sebagai kumpulan objek. Objek menyimpan data (atribut) dan perilaku (method). Empat pilarnya: encapsulation, abstraction, inheritance, polymorphism.

**2. Apa beda class dan object?**
Class adalah cetak biru, object adalah wujud nyatanya. `BukuDigital` adalah class; satu buku tertentu di database adalah object.

**3. Jelaskan encapsulation dan contohnya di proyekmu.**
Membungkus data dan method pengolahnya dalam satu class. Contoh: `CustomUser` menyimpan `exp` dan `streak_days` bersama method `add_exp()`, `update_streak()`, dan `reset_streak_if_expired()`. View cukup memanggil method itu tanpa menulis ulang aturannya.

**4. Jelaskan abstraction dan contohnya.**
Menyembunyikan detail dan menampilkan yang perlu. Contoh: `ItemKatalog` (abstract base model, hanya kerangka atribut umum) dan ORM yang menyembunyikan SQL.

**5. Jelaskan inheritance dan contohnya.**
Subclass mewarisi atribut dan method induk. `BukuDigital` dan `Jurnal` mewarisi `ItemKatalog`, dan `CustomUser` mewarisi `AbstractUser`.

**6. Jelaskan polymorphism dan contohnya.**
Nama method yang sama berperilaku berbeda tergantung objeknya. Contoh: `__str__` yang ditimpa di banyak model, sehingga `str(buku)` menghasilkan `[Digital] ...` dan `str(jurnal)` menghasilkan `[Jurnal] ...`.

**7. Mengapa `__str__` termasuk polimorfisme?**
Karena ada hierarki (semua mewarisi `models.Model`), nama method sama, dipanggil dengan cara sama (`str(obj)`), dan hasilnya berbeda per class. Ini method overriding.

**8. Apakah ada polimorfisme yang terjadi saat program berjalan, bukan hanya definisi?**
Ya, di `Peminjaman.__str__`. Variabel `item = self.buku_digital or self.jurnal` bisa berisi buku atau jurnal, dan `f"{item}"` otomatis memanggil `__str__` milik class yang sedang dipegang.

**9. Apa beda overriding dan overloading?**
Overriding: subclass menulis ulang method induk dengan nama dan parameter sama. Overloading: nama sama dengan parameter berbeda dalam satu class. Python tidak mendukung overloading secara langsung; yang dipakai proyek ini adalah overriding.

**10. Apa itu `super()`?**
Memanggil method milik class induk, misalnya `super().save(*args, **kwargs)` agar proses simpan bawaan Django tetap berjalan.

**11. Apa arti `abstract = True` pada `ItemKatalog`?**
Class itu hanya cetak biru: tidak membuat tabel sendiri dan tidak bisa dibuat objeknya langsung. Field-nya disalin ke tabel subclass.

**12. Kenapa `BukuDigital` dan `Jurnal` dibuat dari `ItemKatalog`?**
Keduanya berbagi atribut dasar (id, judul, penulis, tahun, cover, tanggal), jadi tidak perlu menulis ulang (DRY).

**13. Apa beda abstraction dan encapsulation?**
Abstraction fokus pada apa yang disembunyikan dari pemakai (detail rumit, kerangka umum). Encapsulation fokus pada membungkus data dengan method yang mengaturnya. Abstraksi: `ItemKatalog` dan ORM. Enkapsulasi: `CustomUser` dengan `add_exp()` dan `update_streak()`.

**14. Apa itu asosiasi antarobjek?**
Objek saling terhubung lewat referensi tanpa menyalin data. Di Django memakai `ForeignKey`, misalnya `Peminjaman` menghubungkan `user` dengan `buku_digital` atau `jurnal`.

**15. Apa beda `CASCADE` dan `SET_NULL`?**
`CASCADE` menghapus data terkait saat induknya dihapus. `SET_NULL` hanya mengosongkan kolom relasinya. `Peminjaman.buku_digital` memakai `SET_NULL` agar riwayat tetap ada, sedangkan `Bookmark` memakai `CASCADE`.

**16. Apa fungsi `@property`?**
Membuat method dibaca seperti atribut tanpa tanda kurung, misalnya `buku.kategori_label` dan `user.nama_asli`. Nilainya dihitung dari data lain dan tidak disimpan di database.

**17. Apa fungsi `@classmethod` pada `Pengaturan.muat()`?**
Method dipanggil dari class tanpa membuat objek dulu (`Pengaturan.muat()`), lalu mengambil atau membuat satu-satunya baris pengaturan.

### B. Alur program

**18. Jelaskan alur program dari awal sampai halaman tampil.**
Browser meminta alamat → `config/urls.py` → `perpustakaan/urls.py` → fungsi di `views.py` → model mengambil data dari database → `render()` mengirim data ke template → HTML dikirim ke browser.

**19. Apa itu MTV?**
Model (data), Template (tampilan), View (logika). Setara dengan MVC dengan perbedaan istilah: View di Django ≈ Controller di MVC, dan Template Django ≈ View di MVC.

**20. Kenapa `urls.py` dipecah dua?**
`config/urls.py` adalah pintu utama proyek dan meneruskan ke app lewat `include()`. `perpustakaan/urls.py` berisi alamat khusus app, jadi tiap app mengurus alamatnya sendiri.

**21. Apa gunanya `name=` di `path()`?**
Memberi nama pada alamat agar bisa dipanggil lewat `{% url 'katalog' %}` dan `reverse('katalog')` tanpa menulis alamat manual. Kalau alamat berubah, template tidak perlu diubah.

**22. Apa arti `<int:pinjaman_id>` dan `<str:olid>`?**
Bagian alamat yang ditangkap sebagai variabel dan dikirim ke view. `int` hanya menerima angka, `str` menerima teks tanpa garis miring.

**23. Bagaimana alur meminjam buku?**
POST ke `buku/<olid>/pinjam/` → `pinjam_buku` memeriksa format id, pinjaman ganda, dan batas pinjam → membuat `Peminjaman` berstatus `Dibaca` → notifikasi → redirect ke `/peminjaman/`.

**24. Bagaimana alur mengembalikan buku?**
`kembalikan/<id>/` → `kembalikan_buku` mengambil pinjaman milik user, mengubah status menjadi `Selesai`, mengisi `progress_baca = 100` dan `tanggal_kembali`, lalu mengirim notifikasi dan redirect.

**25. Bagaimana pencarian dan filter di katalog bekerja?**
Lewat parameter URL `q` dan `kategori`. Kategori disaring dengan gabungan `Q` objek (OR), pencarian memakai `icontains` di judul, penulis, kategori, dan deskripsi.

**26. Kenapa filter kategori mengenali `computer_science` dan `Computer Science`?**
`KATEGORI_FILTER_TERMS` memberi beberapa istilah per kategori, sehingga nilai baru dari admin dan label lama dari data lama sama-sama cocok. Ini diuji di `test_catalog_category_filter_matches_admin_value_and_legacy_label`.

**27. Bagaimana batas pinjam diterapkan?**
`pinjam_buku` menghitung pinjaman aktif user dan menolak jika sudah mencapai `user.max_loans` (default 5).

**28. Bagaimana perpanjangan dibatasi?**
Field `perpanjangan` dihitung. Jika sudah mencapai `MAKS_PERPANJANG`, perpanjangan ditolak. Jika belum, jatuh tempo ditambah `MASA_PERPANJANG_HARI` dan counter naik.

**29. Bagaimana streak dihitung?**
`update_streak()` berjalan saat detik baca hari itu mencapai 1800. Jika terakhir baca kemarin, streak +1. Jika lebih lama atau belum pernah, streak mulai lagi dari 1. `reset_streak_if_expired()` mengembalikan streak ke 0 jika sudah melewatkan satu hari.

**30. Bagaimana sistem mencegah waktu baca dipalsukan?**
`waktu_baca` membatasi detik yang diklaim browser sebesar selisih waktu nyata sejak permintaan sebelumnya (disimpan di `session["ring_terakhir"]`).

**31. Bagaimana peringkat dan level dihitung?**
Peringkat = 1 + jumlah member non-admin yang EXP-nya lebih tinggi. Level = `exp // 100 + 1`.

**32. Kenapa user tidak bisa mengembalikan atau memperpanjang pinjaman orang lain?**
`get_object_or_404(Peminjaman, id=..., user=request.user)` hanya menemukan pinjaman milik user yang login; selain itu hasilnya 404.

**33. Dari mana `jatuh_tempo` di template peminjaman berasal?**
Bukan field model. `peminjaman_view` menempelkannya ke tiap objek lewat `_jatuh_tempo()` di dalam perulangan, lalu template membacanya.

### C. Keamanan dan Django

**34. Apa fungsi `{% csrf_token %}`?**
Token perlindungan terhadap serangan CSRF. Wajib di setiap form POST.

**35. Kenapa aksi seperti meminjam memakai POST, bukan GET?**
Aksi yang mengubah data sebaiknya lewat POST dengan token CSRF agar tidak terpicu tidak sengaja atau dari situs lain. `@require_POST` memaksa aturan itu.

**36. Apa fungsi `@login_required`?**
Mengalihkan user yang belum login ke halaman login sebelum view dijalankan.

**37. Apa itu migrasi?**
Catatan perubahan struktur model ke database. `makemigrations` membuat berkasnya, `migrate` menerapkannya. Proyek ini sudah sampai migrasi 0008.

**38. Kenapa pakai ORM, bukan SQL langsung?**
Lebih ringkas, aman dari SQL injection, dan database mudah diganti tanpa mengubah kode.

**39. Apa fungsi `format_html` di `admin.py`?**
Membuat HTML yang aman dengan meng-escape nilai variabel, sehingga terhindar dari XSS.

**40. Apa fungsi `enctype="multipart/form-data"`?**
Diperlukan agar file (PDF buku) ikut terkirim bersama form.

### D. Template

**41. Apa itu `{% extends %}` dan `{% block %}`?**
`{% extends %}` membuat halaman mewarisi template induk, dan `{% block %}` adalah bagian yang diisi ulang oleh halaman anak. Contoh: `kelola_buku.html` mewarisi `base_admin.html`.

**42. Apa fungsi `{% for %}…{% empty %}`?**
Mengulang daftar, dan menampilkan isi `{% empty %}` jika daftarnya kosong.

**43. Kenapa data dititipkan lewat `data-*` di `baca.html`?**
Agar file JavaScript tetap statis dan bisa dipakai ulang, sementara data dinamis dari Django cukup ditaruh di HTML.

**44. Kenapa PDF.js dimuat sebelum `buku.js`?**
`buku.js` memakai PDF.js, jadi urutan pemuatan penting. Atribut `defer` membuat script berjalan setelah HTML selesai dimuat.

**45. Bagaimana sapaan "Selamat Pagi/Siang/Sore/Malam" dibuat?**
JavaScript di `dashboard.html` membaca jam perangkat dengan `new Date().getHours()` dan mengganti teks elemen `#salam`. Ini berjalan di browser, bukan di Django.

**46. Bagaimana hapus massal di `kelola_buku.html` bekerja?**
Checkbox bernama `ids` dihubungkan ke form `formHapusMassal` lewat atribut `form`. Saat dikonfirmasi, form dikirim ke `hapus_buku_massal`.

### E. Tes

**47. Apa fungsi `tests.py` dan bagaimana menjalankannya?**
Menguji otomatis bahwa fitur berjalan sesuai aturan, sehingga perubahan kode tidak diam-diam merusak fitur lama. Dijalankan dengan `python manage.py test`.

**48. Apa fungsi `setUp()` dan mengapa ditimpa?**
Dijalankan sebelum tiap tes untuk menyiapkan data awal (user dan buku). Versi bawaannya kosong, jadi ditimpa (overriding).

**49. Apa fungsi `refresh_from_db()`?**
Memuat ulang objek dari database. View mengubah data di database, sedangkan objek di tes masih menyimpan nilai lama.

**50. Apa fungsi `force_login`?**
Membuat user langsung dalam keadaan login tanpa mengisi form, agar tes fokus pada fitur yang diuji.

### F. Pertanyaan jebakan

**51. Apakah enkapsulasi di Python benar-benar menyembunyikan data?**
Tidak seketat Java. Python memakai konvensi (awalan `_`) dan pengelompokan data dengan method dalam class.

**52. Kenapa `kembalikan_buku` bisa lewat GET?**
Tombolnya berupa tautan, sehingga tanpa `@require_POST`. Secara praktik yang baik, aksi seperti ini lebih tepat memakai POST dengan CSRF; itu bahan perbaikan ke depan.

**53. Kenapa `tanggal_kembali` dipakai untuk jatuh tempo sekaligus tanggal pengembalian?**
Selama pinjaman aktif ia menyimpan jatuh tempo (hasil perpanjangan), dan saat dikembalikan ia diisi waktu pengembalian. Itu pilihan desain; desain yang lebih bersih memakai field `jatuh_tempo` terpisah.

**54. Apa yang kamu kembangkan jika ada waktu lagi?**
Contoh jawaban jujur: memindahkan `kembalikan_buku` ke POST, memisahkan field `jatuh_tempo`, membersihkan sisa kode lama, dan menambah tes untuk kasus stok habis dan pinjam ganda.

### G. Relasi antarobjek

**55. Apa itu asosiasi? Contohnya di proyekmu?**
Hubungan antarobjek lewat referensi tanpa menyalin data. `Peminjaman` dan `Bookmark` menghubungkan `CustomUser` dengan `BukuDigital` atau `Jurnal` lewat `ForeignKey`.

**56. Apa itu agregasi? Contohnya?**
Hubungan "memiliki" yang lemah: bagian bisa hidup tanpa induk. `Peminjaman.buku_digital` memakai `SET_NULL`, jadi buku bisa dihapus tanpa menghapus riwayat peminjaman.

**57. Apa itu komposisi? Contohnya?**
Hubungan "memiliki" yang kuat: bagian ikut hilang bersama induk. `Notifikasi.user` dan `UserAchievement.user` memakai `CASCADE`, jadi kalau user dihapus, data itu ikut terhapus.

**58. Apa beda agregasi dan komposisi?**
Tanyakan: "kalau induk dihapus, apakah bagian masih bermakna?" Masih → agregasi (rumah tutup, buku tetap ada). Tidak → komposisi (rumah dibongkar, kamar ikut hilang).

**59. Apakah Django menandai relasi itu secara eksplisit?**
Tidak. Django hanya punya `ForeignKey` dan `on_delete`. Agregasi dan komposisi adalah tafsiran dari perilaku `SET_NULL` dan `CASCADE`.

**60. Apa itu dependensi? Contohnya?**
Satu bagian kode memakai objek lain secara sementara tanpa menyimpannya. View `waktu_baca` memakai `user.update_streak()` dan `_notifikasi()` selama fungsinya berjalan.

**61. Apa beda asosiasi dan dependensi?**
Asosiasi disimpan sebagai atribut (relasi tetap, seperti `Peminjaman.user`). Dependensi hanya dipakai sementara sebagai parameter atau variabel lokal.

**62. Kenapa `Peminjaman` punya dua `ForeignKey` yang boleh kosong (`buku_digital` dan `jurnal`)?**
Karena satu peminjaman berisi salah satunya, buku atau jurnal. Itu sebabnya `__str__` memakai `self.buku_digital or self.jurnal`.

**63. Apa itu `related_name`?**
Nama jalan balik dari objek induk ke objek terkait, misalnya `user.notifikasi.all()` untuk mengambil semua notifikasi milik user.

**64. Apa yang terjadi pada data lain saat sebuah buku dihapus?**
`Peminjaman` tetap ada dengan kolom buku kosong (`SET_NULL`), sedangkan `Bookmark` untuk buku itu ikut terhapus (`CASCADE`).

### H. Cara menjawab dan menunjuk kode

**Rumus 3 langkah:** (1) sebut pengertian singkat, (2) tunjuk contoh nyata di kodemu (nama file dan class atau method), (3) jelaskan alasan mengapa itu termasuk pilar tersebut.

**Contoh jawaban polimorfisme:**
"Polimorfisme adalah method bernama sama yang berperilaku berbeda tergantung objeknya. Di `models.py`, `__str__` ditimpa di `BukuDigital`, `Jurnal`, dan model lain. `str(buku)` menghasilkan `[Digital] ...` dan `str(jurnal)` menghasilkan `[Jurnal] ...`. Ini polimorfisme karena nama method sama, cara memanggilnya sama, tetapi hasilnya berbeda per class."

**Tips menunjuk kode:** komentar di `models.py` memakai penanda yang bisa dicari dengan `Ctrl+F`: `[ABSTRAKSI]`, `[PEWARISAN]`, `[POLIMORFISME - overriding]`, dan `ASOSIASI ANTAROBJEK`. Buka file itu dan cari penanda tersebut kalau penguji meminta ditunjukkan.

---

## 7. Catatan Jujur (Cek Sebelum Pengujian)

1. **Tes EXP vs. kode pengembalian.** `tests.py` menegaskan `self.user.exp == 50` setelah buku dikembalikan, tetapi `kembalikan_buku` yang dilampirkan **tidak menambah EXP**. EXP bertambah di `waktu_baca`. Jalankan `python manage.py test` untuk memastikan hasilnya. Jika tes itu gagal, kemungkinan sumbernya EXP yang dipindah ke sistem waktu baca dan tes belum disesuaikan.
2. **`CustomUser.save()` belum menambah perilaku.** Method itu hanya memanggil `super().save()`. Secara teknis overriding, tetapi bukan contoh polimorfisme yang kuat.
3. **Kode tidak terjangkau di `admin.py`.** Di `_ikon`, semua kode setelah `return` pertama tidak pernah dijalankan, dan memakai `IKON_ACHIEVEMENT_BERSIH` yang tidak di-import di file itu. Logikanya sudah dipindah ke properti `ikon_tampil` di model; sisa lamanya belum dihapus.
4. **`id_item` memakai `unique=True` dan `primary_key=True` sekaligus.** `unique` redundan, tetapi tidak merusak.
5. **`simpan_progress` didaftarkan di `config/urls.py`,** bukan di `perpustakaan/urls.py` bersama alamat lainnya. Berfungsi normal; bisa dipindahkan.
6. **`baca.html` masih punya CSS `iframe`** dengan komentar Internet Archive, kemungkinan sisa versi lama karena buku sekarang dibaca lewat PDF.js.
7. **Tipe `pk` anggota tidak seragam** di `urls.py`: `<str:pk>` untuk edit/hapus/aktifkan, `<int:pk>` untuk setujui/tolak.
8. **Belum dilampirkan, sehingga belum dijelaskan baris per baris:** `katalog.html`, `peminjaman.html`, `views_admin.py`, `baca_buku`, `simpan_progress`, dan helper di `views.py` (`_pastikan_buku`, `_jatuh_tempo`, `_notifikasi`), serta nilai konstanta `ITEM_ID_RE`, `MASA_PINJAM_HARI`, `MAKS_PERPANJANG`, `RING_DETIK_PENUH`, `RING_EXP`. Nilai `data-total="120"` di `baca.html` juga perlu dicek artinya di `baca-ring.js`.
9. **Agregasi dan komposisi adalah tafsiran.** Pemetaan di bagian 4.5 berasal dari perilaku `on_delete` (`SET_NULL` dan `CASCADE`), bukan sesuatu yang tertulis di kode. Komentar di `models.py` hanya menyebut "asosiasi antarobjek". Jelaskan sebagai perilaku, dan jangan mengklaim bahwa Django mendefinisikannya secara eksplisit.