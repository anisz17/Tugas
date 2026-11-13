\<a id="top"></a>

<div align="center">

# 🐧 Catatan Praktikum Sistem Operasi

**Rekap Soal & Jawaban · Persiapan Pengujian Akhir**

`Modul 2` &nbsp;·&nbsp; `Modul 3` &nbsp;·&nbsp; `Modul 4` &nbsp;·&nbsp; `Modul 5` &nbsp;·&nbsp; `Modul 6` &nbsp;·&nbsp; `Modul 7` &nbsp;·&nbsp; `Modul 8`

*Ubuntu VM via SSH · Linux CLI · Bash · Python*

</div>

---

> 🎯 **Tujuan file ini:** satu tempat untuk mengulang semua soal latihan beserta jawabannya, supaya saat pengujian akhir tidak perlu mencari-cari lagi. Setiap soal ditulis utuh, lengkap dengan perintah, hasil, dan penjelasan.

## 📑 Daftar Isi

1. [Gambaran Umum](#gambaran-umum)
2. [Cara Membaca File Ini](#cara-membaca)
3. [Aturan Emas: Membaca Jalur Folder](#aturan-jalur)
4. [Modul 2 · Manajemen File, User & Permissions](#modul-2)
   - [Latihan Set 1 (7 soal)](#modul-2-set-1)
   - [Latihan Set 2 (12 soal, tema posttest)](#modul-2-set-2)
   - [Contekan Modul 2](#contekan-modul-2)
5. [Modul 3 · Program, Environment & Manajemen Proses](#modul-3)
   - [Latihan Set 1 (13 soal)](#modul-3-set-1)
   - [Latihan Set 2 (17 soal)](#modul-3-set-2)
   - [Contekan Modul 3](#contekan-modul-3)
6. [Modul 4 · Sinkronisasi Proses](#modul-4)
7. [Modul 5 · Deadlock](#modul-5)
8. [Modul 6 · Manajemen Memori](#modul-6)
   - [Latihan Set 1 · Memori 1 (7 soal)](#modul-6-set-1)
   - [Latihan Set 2 · Memori 2 (11 soal)](#modul-6-set-2)
   - [Contekan Modul 6](#contekan-modul-6)
9. [Modul 7 · Manajemen Penyimpanan](#modul-7)
10. [Modul 8 · Keamanan Komputer](#modul-8)
    - [Latihan (8 soal)](#modul-8-latihan)
    - [Contekan Modul 8](#contekan-modul-8)
11. [Kesalahan Paling Sering Terulang](#kesalahan)
12. [Checklist Sebelum Ujian](#checklist)

---

<a id="gambaran-umum"></a>

## 🗺️ Gambaran Umum

### Format pengujian akhir

| Hal | Keterangan |
|---|---|
| **Jenis** | Praktik langsung di terminal (CLI) |
| **Jumlah soal** | 15 soal dengan bobot berbeda-beda |
| **Waktu** | 2 jam 30 menit |
| **Cara kerja** | Per individu, soal bebas dikerjakan tanpa harus urut |
| **Materi** | Modul 2 sampai 8 (referensi: modul dan posttest-posttest) |
| **Bantuan** | Soal ujian dan hint disediakan |

### Isi file ini

| Modul | Topik | Jumlah soal latihan |
|---|---|:---:|
| 2 | Manajemen File, User & Permissions | 7 (Set 1) + 12 (Set 2) = **19** |
| 3 | Program, Environment & Manajemen Proses | 13 (Set 1) + 17 (Set 2) = **30** |
| 4 | Sinkronisasi Proses | 6 latihan + 2 posttest = **8** |
| 5 | Deadlock | **5** |
| 6 | Manajemen Memori (Memori 1 dan 2) | 7 (Set 1) + 11 (Set 2) = **18** |
| 7 | Manajemen Penyimpanan | **5** |
| 8 | Keamanan Komputer | **8** (+ ringkasan konsep dan command) |
| | **Total** | **93** |

> ℹ️ **Catatan:** semua soal latihan di sini buatan Claude. Set 2 Modul 2 mengikuti alur contoh posttest, tetapi seluruh nama folder, user, dan grup sudah diganti. Modul 3 dan Modul 6 punya dua set karena dikerjakan di dua sesi belajar berbeda (nama folder dan program contoh berbeda, isi konsepnya saling melengkapi). Modul 4 dan 5 memakai **Python** (`threading`), bukan hanya perintah Bash.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="cara-membaca"></a>

## 🧭 Cara Membaca File Ini

| Ikon | Arti |
|:---:|---|
| 📝 | **Soal** (teks soal utuh) |
| ✅ | **Jawaban** (perintah yang benar) |
| 💡 | **Penjelasan** (kenapa jawabannya begitu) |
| ⚠️ | **Catatan / jebakan** yang pernah terjadi saat latihan |

---

<a id="aturan-jalur"></a>

## 🧱 Aturan Emas: Membaca Jalur Folder

Banyak error latihan (`No such file or directory`) berasal dari satu sebab: **posisi folder tidak cocok dengan jalur yang diketik.**

| Cara menulis | Dibaca mulai dari | Hasil |
|---|---|---|
| `~/ujian_so` | folder home (`/home/magang`) | **selalu sama**, dari mana pun |
| `/home/magang/ujian_so` | akar sistem `/` | **selalu sama**, dari mana pun |
| `ujian_so` (tanpa awalan) | folder **tempat kamu berdiri** | bergantung posisi, cek dengan `pwd` |

```bash
pwd          # lihat posisi sekarang
cd           # kembali ke home
echo ~       # lihat alamat home, hasilnya /home/magang
```

> 💡 **Tips cepat:** prompt `magang@praktikum-ubuntu:~$` berarti kamu berdiri di home. Prompt `...:~/ujian_so/proyek_web$` berarti kamu berdiri di dalam `proyek_web`. Soal yang tidak menyebut lokasi berarti dikerjakan dari home. Kalau ragu, ketik `cd` dulu atau tulis jalur dengan awalan `~/`.

> ⚠️ **Jangan** memakai `~` di dalam tanda kutip pada `export PATH="..."`, karena `~` tidak diganti menjadi alamat home. Tulis alamat lengkap `/home/magang/...`.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-2"></a>

# 📁 Modul 2 · Manajemen File, User & Permissions

<a id="modul-2-set-1"></a>

## Latihan Set 1 (7 soal)

### Soal 1 — Membuat folder dan file

> 📝 **Soal:** Dalam satu perintah, buat struktur folder `praktikum/tugas/so`. Lalu buat file kosong `catatan.txt` di dalam folder `so`, dan tampilkan isi folder `so`.

✅ **Jawaban**

```bash
mkdir -p praktikum/tugas/so
touch praktikum/tugas/so/catatan.txt
ls praktikum/tugas/so
```

💡 Flag `-p` membuat folder bertingkat sekaligus.

---

### Soal 2 — `head` dan `tail`

> 📝 **Soal:** Buat `data.txt` berisi 15 baris dengan nano atau vim. Tampilkan 3 baris paling atas saja, lalu 4 baris paling bawah saja.

✅ **Jawaban**

```bash
nano data.txt
head -n 3 data.txt
tail -n 4 data.txt
```

⚠️ Kamu sempat menulis `tail -n 3`. Angka di `-n` harus sama dengan jumlah baris yang diminta soal.

---

### Soal 3 — `find` dan `grep`

> 📝 **Soal:** Cari semua file berakhiran `.txt` mulai dari folder saat ini termasuk subfolder. Lalu tampilkan nama file yang isinya mengandung kata "baris".

✅ **Jawaban**

```bash
find . -name "*.txt"
grep -rl "baris" *
```

💡 `find` mencari berdasarkan **nama file**, `grep` mencari berdasarkan **isi file**. Flag `-r` rekursif, `-l` hanya menampilkan nama file.

⚠️ Pola `*.txt` wajib diberi **tanda kutip**. Tanpa kutip, shell mengganti `*.txt` lebih dulu dan `find` bingung (error `paths must precede expression`).

---

### Soal 4 — User dan grup

> 📝 **Soal:** Buat user `ren` lengkap dengan folder home. Buat grup `sirkel`, lalu masukkan `ren` ke grup itu tanpa mengeluarkannya dari grup lain. Buktikan dengan identitas dan daftar grup `ren`.

✅ **Jawaban**

```bash
sudo useradd -m ren
sudo groupadd sirkel
sudo usermod -aG sirkel ren
id ren
```

💡 `-m` membuat folder home. `-a` (append) harus berpasangan dengan `-G`, kalau `-a` lupa, user keluar dari grup sekunder lainnya.

⚠️ Di VM-mu `useradd -m ren` ditolak karena grup `ren` sudah ada, jadi kamu memakai `-g sirkel`. Contoh `tel` lebih pas menggambarkan soal ini:

```text
uid=1031(tel) gid=1033(tel) groups=1033(tel),1031(h2h)
```

`gid` adalah grup utama, `groups` adalah semua grup (utama + tambahan). Urutan `usermod -aG` adalah **grup dulu, baru user**.

---

### Soal 5 — Mengganti nama user dengan rapi

> 📝 **Soal:** Ubah nama user lama menjadi nama baru, pindahkan home-nya ke `/home/namabaru`, dan pastikan kepemilikannya benar, semuanya dengan **satu perintah**. Buktikan lewat file konfigurasi user. (Kamu mengerjakannya dengan `ray` menjadi `rafi`.)

✅ **Jawaban**

```bash
sudo usermod -l rafi -d /home/rafi -m ray
grep rafi /etc/passwd
```

Buktimu di VM:

```text
rafi:x:1028:1029::/home/rafi:/bin/sh
```

💡 **Pola:** `-l` nama baru, `-d` home baru, `-m`, lalu **nama lama di paling akhir**. `-m` (move) memindahkan isi home dan mengurus kepemilikannya, dan hanya bisa dipakai bersama `-d`.

📌 **Versi panjang** (lima perintah, hasilnya sama):

```bash
sudo usermod -l ray ren
sudo cp -r /home/ren/ /home/ray/
sudo usermod -d /home/ray/ ray
sudo groupmod -n ray ren
sudo chown -R ray:ray /home/ray
```

⚠️ Versi gabungan tidak mengganti nama **primary group**. Itu butuh `groupmod -n` terpisah (kolom GID di `/etc/passwd` tetap, tetapi nama grupnya masih lama). Nama baru tidak boleh sudah dipakai user lain, dan `ren/ray` bukan nama valid karena ada tanda `/`.

---

### Soal 6 — Permission dengan angka

> 📝 **Soal:** Buat file `rahasia.sh`. Atur izinnya dengan notasi angka: owner baca, tulis, jalankan; group baca dan jalankan; others tanpa izin. Buktikan dengan `ls -l`.

✅ **Jawaban**

```bash
touch rahasia.sh
chmod 750 rahasia.sh
ls -l
```

Target hasil: `-rwxr-x---`

💡 **Rumus:** r = 4, w = 2, x = 1, strip = 0. Jumlahkan **per kelompok**, urutan **owner, group, others**:

| Kelompok | Izin | Hitungan | Digit |
|---|:---:|:---:|:---:|
| Owner | `rwx` | 4+2+1 | **7** |
| Group | `r-x` | 4+1 | **5** |
| Others | `---` | 0 | **0** |

⚠️ Kamu sempat membuat `rahasia.txt` lalu `mv rahasia.txt rahasia.sh`, hasil akhirnya sama. `mv` mengganti nama tanpa mengubah isi dan izin.

---

### Soal 7 — `chown` dan kunci akun

> 📝 **Soal:** Buat folder `tugas_video`, jadikan root pemiliknya beserta semua isinya, dan tampilkan info folder itu saja. Lalu buat user (kamu memakai `carmen`), kunci akunnya, dan tampilkan statusnya.

✅ **Jawaban**

```bash
mkdir tugas_video
sudo chown -R root tugas_video
ls -ld tugas_video
sudo useradd carmen
sudo passwd -l carmen
sudo passwd -S carmen
```

💡 Format `chown`: **flag, pemilik baru, lalu target**. `-R` membuat semua isi ikut. Status `passwd -S`: huruf **L** artinya terkunci, **P** artinya password aktif. Kamu membuktikan perubahan P menjadi L setelah dikunci.

⚠️ Soal hanya meminta pemilik, jadi tulis `root` saja (kamu sempat menulis `root:sirkel` sehingga grupnya ikut berubah). Di `passwd`, `-l` dan `-u` huruf **kecil**, `-S` huruf **besar**. Akun tanpa password tidak bisa dibuka kuncinya dengan `-u`.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-2-set-2"></a>

## Latihan Set 2 (12 soal, tema posttest)

Alur 12 langkah berurutan seperti contoh posttest, dengan tema baru: folder **`ujian_so`**, user **`kirana`**, dan grup **`tim_web`**.

> 💡 **Sebelum mulai**, cek dulu bahwa `id kirana` dan `getent group tim_web` kosong ("no such user"), supaya tidak bentrok dengan sisa latihan.

### Soal 1 — Struktur folder dengan satu baris

> 📝 **Soal:** Buat struktur direktori bertingkat dengan **satu baris perintah**: `ujian_so/proyek_web/arsip` dan `ujian_so/proyek_web/riwayat`. Tampilkan isi folder `ujian_so/proyek_web`.

✅ **Jawaban**

```bash
mkdir -p ujian_so/proyek_web/arsip ujian_so/proyek_web/riwayat
ls -l ujian_so/proyek_web
```

💡 `mkdir` boleh diberi lebih dari satu jalur sekaligus, dipisah spasi.

---

### Soal 2 — File log dengan editor

> 📝 **Soal:** Buat `kegiatan.log` di `ujian_so/proyek_web/riwayat/` dengan nano atau vim, isi minimal **15 baris**, lalu buktikan file tersimpan.

✅ **Jawaban**

```bash
nano ujian_so/proyek_web/riwayat/kegiatan.log
less -N ujian_so/proyek_web/riwayat/kegiatan.log
```

💡 Nano: simpan `Ctrl+O` lalu Enter, keluar `Ctrl+X`. Keluar dari `less` dengan `q`. Flag `-N` menampilkan nomor baris, jadi terlihat isinya tepat 15 baris.

---

### Soal 3 — 5 baris pertama dan terakhir

> 📝 **Soal:** Tampilkan **hanya 5 baris pertama** `kegiatan.log`, lalu **5 baris terakhirnya**, langsung di terminal tanpa editor.

✅ **Jawaban**

```bash
head -n 5 kegiatan.log
tail -n 5 kegiatan.log
```

⚠️ Dikerjakan dari dalam folder `riwayat`. Dari home, tulis jalur lengkap `~/ujian_so/proyek_web/riwayat/kegiatan.log`. Bentuk `head -5` juga jalan, tetapi modul memakai `-n`.

---

### Soal 4 — User baru dengan home dan password

> 📝 **Soal:** Buat user `kirana` dengan home otomatis `/home/kirana`, tentukan passwordnya, dan buktikan folder home-nya ada.

✅ **Jawaban**

```bash
sudo useradd -m kirana
sudo passwd kirana
ls -l /home
```

💡 Password diketik **dua kali** dan layar tidak menampilkan apa pun (itu normal). Folder home semua user ada di `/home`, bukan di folder tempatmu berdiri. Hasil `ls -l /home` memuat baris `kirana kirana`.

---

### Soal 5 — Grup baru dan tambah user

> 📝 **Soal:** Buat grup `tim_web`, lalu tambahkan `kirana` ke grup itu tanpa menghapus keanggotaan grup lain. Tampilkan identitas `kirana`.

✅ **Jawaban**

```bash
sudo groupadd tim_web
sudo usermod -aG tim_web kirana
id kirana
```

Hasil:

```text
uid=1033(kirana) gid=1035(kirana) groups=1035(kirana),1036(tim_web)
```

💡 Alternatif yang juga benar: `sudo gpasswd -a kirana tim_web`. **Urutan keduanya terbalik**:

| Perintah | Urutan |
|---|---|
| `usermod -aG` | **grup dulu**, baru user |
| `gpasswd -a` | **user dulu**, baru grup |

---

### Soal 6 — File kosong di `arsip`

> 📝 **Soal:** Buat file kosong `catatan.txt` di `ujian_so/proyek_web/arsip/` dan tampilkan isi folder `arsip`.

✅ **Jawaban**

```bash
touch ujian_so/proyek_web/arsip/catatan.txt
ls -l ujian_so/proyek_web/arsip
```

⚠️ Buktinya adalah **isi folder** (`ls -l`), bukan `cat catatan.txt`.

---

### Soal 7 — Ubah pemilik secara rekursif

> 📝 **Soal:** Ubah kepemilikan `ujian_so` beserta seluruh isinya secara rekursif menjadi milik user `kirana` dan grup `tim_web`. Tampilkan info `ujian_so`, lalu isi folder `arsip`.

✅ **Jawaban**

```bash
sudo chown -R kirana:tim_web ~/ujian_so
ls -ld ~/ujian_so
ls -l ~/ujian_so/proyek_web/arsip
```

💡 Target `chown` harus **folder paling atas** (`ujian_so`), bukan satu file. Awalan `~/` membuat jalurnya tidak bergantung posisi. Setelah berhasil, kolom pemilik dan grup di semuanya berubah menjadi `kirana tim_web`.

⚠️ Setelah ini, `catatan.txt` dimiliki `kirana`, jadi akun `magang` yang menulis ke dalam folder itu akan kena `Permission denied`.

---

### Soal 8 — Permission oktal

> 📝 **Soal:** Atur izin `catatan.txt` dengan notasi oktal: owner `rw-`, group `r--`, others `---`. Buktikan dengan `ls -l`.

✅ **Jawaban**

```bash
sudo chmod 640 ujian_so/proyek_web/arsip/catatan.txt
ls -l ujian_so/proyek_web/arsip
```

Target hasil: `-rw-r-----`

| Kelompok | Izin | Digit |
|---|:---:|:---:|
| Owner | `rw-` (4+2) | **6** |
| Group | `r--` (4) | **4** |
| Others | `---` | **0** |

⚠️ Butuh `sudo`, karena file sudah dimiliki `kirana` (error `Operation not permitted` tanpa `sudo`). `chmod` hanya bisa dipakai pemilik file atau root.

---

### Soal 9 — Cari semua `.txt`

> 📝 **Soal:** Cari semua berkas berakhiran `.txt` di seluruh `ujian_so` dengan satu perintah pencarian.

✅ **Jawaban**

```bash
find ~/ujian_so -name "*.txt"
```

💡 Hasilnya hanya `catatan.txt`. `kegiatan.log` tidak muncul karena ekstensinya `.log`.

---

### Soal 10 — Cari kata tanpa membedakan huruf

> 📝 **Soal:** Cari kata tertentu di `kegiatan.log` tanpa membedakan huruf besar atau kecil.

✅ **Jawaban**

```bash
grep -i "c" ~/ujian_so/proyek_web/riwayat/kegiatan.log
```

💡 Flag `-i` = *ignore case*. Untuk membuktikannya, cari dengan huruf yang **berbeda kapital** dari aslinya (misalnya `"C"`), hasilnya tetap muncul.

---

### Soal 11 — Pindah ke akun `kirana`

> 📝 **Soal:** Beralih ke akun `kirana` dengan memuat profil penuh dan pindah ke home-nya, lalu periksa identitas teknis user.

✅ **Jawaban**

```bash
su - kirana
pwd
id
```

Hasil:

```text
/home/kirana
uid=1033(kirana) gid=1035(kirana) groups=1035(kirana),1036(tim_web)
```

💡 Tanda strip `-` membuat profil dimuat penuh dan langsung pindah ke home. Tanpa strip, environment dan folder masih milik user lama. Prompt `kirana` hanya `$` karena shell-nya `/bin/sh`.

---

### Soal 12 — Kembali dan kunci akun

> 📝 **Soal:** Kembali ke akun utama, kunci akun `kirana`, dan tampilkan statusnya.

✅ **Jawaban**

```bash
exit
sudo passwd -l kirana
sudo passwd -S kirana
```

Hasil akhir harus `kirana L ...`.

⚠️ **Jangan** menjalankan `-u` sesudahnya, karena akun terbuka lagi (status kembali `P`). Kalau sesinya bertumpuk, `exit` bisa perlu diketik lebih dari sekali, dan `whoami` membantu memastikan kamu sedang jadi siapa. Flag `-s` kecil dan `-P` bukan flag status.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="contekan-modul-2"></a>

## 📌 Contekan Modul 2

### Melihat, membuat, dan mencari

| Perintah | Fungsi |
|---|---|
| `cat file` | tampilkan semua isi (bisa banyak file) |
| `head -n 5` / `tail -n 5` | 5 baris atas / bawah (default 10) |
| `less -N file` | baca per layar dengan nomor baris. Spasi turun, `b` naik, `/kata` cari, `n` berikutnya, `q` keluar |
| `touch` / `mkdir -p a/b/c` | buat file kosong / folder bertingkat |
| `rm`, `rm -r`, `rm -i` | hapus file / folder / dengan konfirmasi |
| `cp` / `mv` | salin / pindah atau ganti nama |
| `find . -name "x.txt"` | cari **nama** file |
| `find /etc -size +512k` | cari berdasarkan ukuran |
| `grep "kata" file` | cari **isi** file (`-i` abaikan huruf, `-rl` daftar file, `-n` nomor baris) |
| `history \| grep "curl"` | cari di riwayat perintah |

### User, password, dan grup

| Perintah | Fungsi |
|---|---|
| `who` / `id` | siapa login / uid, gid, groups |
| `useradd -m` | buat user **+ home** (m = make) |
| `useradd -u 1024` | UID khusus |
| `usermod -l` `-d` `-m` | ganti **l**ogin, **d**irektori home, **m**ove isi home |
| `userdel -r` | hapus user **+ home** |
| `passwd -l` / `-u` / `-S` | **L**ock / **U**nlock / **S**tatus (L atau P) |
| `su paras` / `su - paras` | ganti user biasa / **penuh** (strip = serius) |
| `groupadd` | buat grup |
| `gpasswd -M a,b grup` | tetapkan anggota (**menimpa**, M besar) |
| `gpasswd -a user grup` | tambah satu anggota |
| `usermod -aG grup user` | tambah ke grup (**wajib** `-a`) |
| `groupmod -n` / `-g` | ganti nama / GID |
| `groupdel` | hapus grup (bukan primary group) |

### Permission dan pemilik

| Perintah | Fungsi |
|---|---|
| `ls -l` / `ls -ld folder` | lihat izin / info folder itu saja |
| `chmod u=rwx,g=rx,o= file` | cara simbol |
| `chmod 764 file` | cara angka (r=4, w=2, x=1) |
| `chmod u+x` / `chmod -x` | tambah / cabut izin eksekusi |
| `chown -R user:grup folder` | ganti pemilik (butuh `sudo`) |
| `./program.sh` | jalankan skrip di folder sendiri |

Format izin: `[jenis][owner][group][others]`, jenis: `-` file, `d` folder, `l` symlink.

### Editor

| Editor | Shortcut |
|---|---|
| **nano** | `Ctrl+X` keluar · `Ctrl+O` simpan (lalu Enter) · `Ctrl+W` cari · `Ctrl+K` potong baris · `Ctrl+U` tempel · `Ctrl+_` ke baris · `Alt+/` ke baris paling bawah |
| **micro** | `Ctrl+S` simpan · `Ctrl+Q` keluar (dipakai di Modul 4, 5, dan 7) |
| **vim** | `i` insert · `Esc` normal · `u` undo · `x` hapus huruf · `dd` hapus baris · `:w` simpan · `:q` keluar · `:wq` / `ZZ` simpan keluar · `:q!` keluar paksa |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-3"></a>

# ⚙️ Modul 3 · Program, Environment & Manajemen Proses

Dua set latihan: **Set 1** (13 soal, folder `latihan_modul3`) dan **Set 2** (17 soal, folder `latihan_os`). Keduanya dikerjakan di akun `magang`.

<a id="modul-3-set-1"></a>

## Latihan Set 1 (13 soal)

### Soal 1 — Membuat script dan menjalankannya

> 📝 **Soal:** Buat folder baru bernama `latihan_modul3` di folder home, lalu masuk ke dalamnya. Di dalam folder itu, buat script bernama `sapa.sh` yang mencetak tulisan `Selamat belajar Sistem Operasi!` dan memakai shebang Bash sebagai penerjemahnya. Beri izin eksekusi, lalu jalankan script itu dan tampilkan hasilnya.

✅ **Jawaban**

```bash
cd
mkdir latihan_modul3
cd latihan_modul3
nano sapa.sh
```

Isi file `sapa.sh`:

```bash
#!/bin/bash
echo "Selamat belajar Sistem Operasi!"
```

Simpan (`Ctrl+O`, Enter), keluar (`Ctrl+X`), lalu:

```bash
chmod u+x sapa.sh
./sapa.sh
cat sapa.sh
```

Hasil `./sapa.sh`: `Selamat belajar Sistem Operasi!`

⚠️ Memanggil `sapa.sh` tanpa `./` menghasilkan `command not found`, karena folder itu belum ada di PATH. Tanda seru di akhir tulisan sempat terlewat, jadi cocokkan hasil dengan soal karakter demi karakter.

---

### Soal 2 — Shebang untuk Python

> 📝 **Soal:** Masih di folder `latihan_modul3`, buat script bernama `halo.py` yang mencetak tulisan `Halo dari Python!` dan memakai shebang Python 3 sebagai penerjemahnya. Beri izin eksekusi, jalankan langsung tanpa mengetik kata `python3` di depannya, lalu tampilkan isi script-nya.

✅ **Jawaban**

```bash
which python3
nano halo.py
```

Isi file `halo.py`:

```python
#!/usr/bin/python3
print("Halo dari Python!")
```

```bash
chmod u+x halo.py
./halo.py
cat halo.py
```

⚠️ Kamu sempat memakai `chmod u+w`. Huruf `w` artinya izin **menulis**, izin **menjalankan** adalah `x`.

---

### Soal 3 — Mendaftarkan folder ke PATH (sementara)

> 📝 **Soal:** Daftarkan folder `~/latihan_modul3` ke dalam PATH di terminal yang sedang aktif. Buktikan script `sapa.sh` bisa dijalankan dari folder lain (misalnya `/tmp`) tanpa awalan `./`, dan tampilkan isi PATH untuk membuktikan foldernya sudah masuk.

✅ **Jawaban**

```bash
cd ~/latihan_modul3
pwd
export PATH="$PATH:/home/magang/latihan_modul3"
echo $PATH
cd /tmp
sapa.sh
```

💡 Hasil `echo $PATH` berakhir dengan `/home/magang/latihan_modul3`, dan `sapa.sh` dari `/tmp` mencetak `Selamat belajar Sistem Operasi!`.

⚠️ Alamat di `export` harus **lengkap** dari `/home/...` (kamu sempat menulis `/home/latihan_modul3` yang salah). Tampilkan isi PATH dengan `echo $PATH`, bukan `echo halo.py`. Jalankan `export` **sekali** supaya PATH tidak bertumpuk (kemarin folder itu muncul tiga kali).

---

### Soal 4 — Redirect hasil dan error

> 📝 **Soal:** Pindah ke folder `~/latihan_modul3`. Di sana, simpan tulisan `Praktikum SO` ke dalam file `catatan.txt` memakai pengalihan hasil, tanpa membuka editor. Jalankan `cat` pada file `file_hilang.txt` (file ini tidak ada) dan simpan pesan errornya ke `galat.txt`, bukan ke layar. Lalu tampilkan isi `catatan.txt` dan `galat.txt`.

✅ **Jawaban**

```bash
cd ~/latihan_modul3
echo "Praktikum SO" > catatan.txt
cat file_hilang.txt 2> galat.txt
cat catatan.txt
cat galat.txt
```

Hasil:

```text
Praktikum SO
cat: file_hilang.txt: No such file or directory
```

💡 `>` mengalihkan hasil sukses (**stdout**), `2>` mengalihkan pesan error (**stderr**, angka 2 = nomor jalur error).

⚠️ Pastikan prompt berakhiran `~/latihan_modul3$` sebelum mengerjakan, supaya file terbentuk di folder yang diminta.

---

### Soal 5 — Pipe dan menghitung

> 📝 **Soal:** Di folder `latihan_modul3`, kerjakan dua hal dengan pipe. Pertama, hitung jumlah kata dari kalimat `Belajar Linux itu seru sekali` tanpa membuat file. Kedua, hitung jumlah baris dari file `sapa.sh` dengan menyalurkan isinya lewat pipe.

✅ **Jawaban**

```bash
echo "Belajar Linux itu seru sekali" | wc -w
cat sapa.sh | wc -l
```

Hasil: `5` dan `2`.

💡 Pipe `|` mengambil hasil perintah di kiri sebagai masukan perintah di kanan. `wc -w` menghitung kata (word), `wc -l` menghitung baris (line).

---

### Soal 6 — Proses di latar belakang

> 📝 **Soal:** Jalankan proses tiruan `sleep 5000` di latar belakang. Tampilkan daftar proses lalu saring hanya baris yang mengandung kata `sleep`. Hentikan proses itu memakai PID-nya, lalu buktikan prosesnya sudah hilang dengan mengulang perintah penyaringan.

✅ **Jawaban**

```bash
sleep 5000 &
ps aux | grep sleep
kill 3198
ps aux | grep sleep
```

Ganti `3198` dengan PID milikmu (muncul setelah `sleep 5000 &`, bentuknya `[1] 3198`). Pada `ps aux | grep sleep` pertama muncul baris `sleep 5000` dengan STAT `S`, setelah `kill` muncul `Terminated`, dan di pengecekan terakhir hanya baris `grep --color=auto sleep` yang tersisa.

⚠️ Setelah tanda pipe harus ada **nama perintah** (`grep`), bukan angka PID (kamu sempat menulis `ps aux | 3198 sleep`).

---

### Soal 7 — Exit code

> 📝 **Soal:** Jalankan perintah yang sukses, yaitu `ls`, lalu tampilkan exit code-nya. Jalankan perintah yang gagal, yaitu menampilkan isi file `tidak_ada.txt` (file ini tidak ada), lalu tampilkan exit code-nya. Jelaskan arti angka yang muncul.

✅ **Jawaban**

```bash
ls
echo $?
cat tidak_ada.txt
echo $?
```

Hasil `echo $?`: `0`, lalu `1`.

💡 **Penjelasan:** `0` berarti perintah terakhir **sukses**, angka selain `0` berarti perintah terakhir keluar karena **error**. Jika hanya mengetik `tidak_ada.txt` tanpa `cat`, shell menganggapnya nama perintah: hasilnya `command not found` dengan kode **127**. `$?` selalu milik perintah yang dijalankan **paling akhir**, jadi `echo $?` harus tepat setelah perintah yang diperiksa.

| Kode | Arti |
|:---:|---|
| `0` | sukses |
| `1` | error umum (misalnya `cat` file tidak ada) |
| `2` | `ls` gagal membuka folder yang tidak ada |
| `126` | perintah ditemukan tetapi tidak boleh dieksekusi (`Permission denied`) |
| `127` | perintah tidak ditemukan |
| `139` | dihentikan SIGSEGV (128 + 11) |

---

### Soal 8 — Konfigurasi terminal (`.bashrc`)

> 📝 **Soal:** Tampilkan semua file tersembunyi di folder home dan pastikan `.bashrc` ada. Buka file konfigurasi itu dengan nano, lalu tambahkan di baris paling bawah perintah yang mencetak `Halo Annisa dari config shell!`. Buktikan konfigurasinya bekerja tanpa menutup terminal dengan membaca ulang file itu di sesi aktif. Terakhir, hapus baris tadi agar terminalmu tidak berisik.

✅ **Jawaban**

```bash
ls -a ~
cat ~/.bashrc
echo $SHELL
nano ~/.bashrc
```

Di nano, tekan `Alt + /` untuk loncat ke baris paling bawah, lalu tambahkan **di bawah baris terakhir** (`fi`):

```bash
echo "Halo Annisa dari config shell!"
```

Simpan, keluar, lalu:

```bash
source ~/.bashrc
```

Sapaan langsung muncul di layar. Setelah terbukti, bersihkan:

```bash
nano ~/.bashrc          # kursor di baris sapaan, Ctrl+K, simpan, keluar
source ~/.bashrc
tail -3 ~/.bashrc
```

Sapaan tidak muncul lagi, dan baris terakhir file adalah `fi` bawaan Ubuntu.

⚠️ `.bashrc` bawaan Ubuntu panjang (sekitar 3771 byte), jadi baris barumu harus **setelah baris terakhir**, bukan diselipkan di tengah. `echo $SHELL` menampilkan `/bin/bash`, tanda `.bashrc` memang dibaca.

---

### Soal 9 — Interpreted vs compiled

> 📝 **Soal:** Cari lokasi program `sh` dengan satu perintah. Tampilkan isi program itu dan perhatikan hasilnya, lalu pulihkan terminalmu kalau tampilannya berantakan. Jelaskan kenapa hasilnya berantakan, dan apakah `sh` termasuk interpreted atau compiled, dibandingkan dengan `sapa.sh` yang terbaca normal.

✅ **Jawaban**

```bash
which sh
cat /usr/bin/sh
reset
```

Hasil `which sh`: `/usr/bin/sh`. Hasil `cat`: simbol aneh dan kotak-kotak, dengan penanda `ELF` di bagian paling awal. `reset` mengembalikan terminal ke normal.

💡 **Penjelasan:** hasilnya berantakan karena `sh` itu program **compiled**, isinya **kode mesin** (file biner) untuk dijalankan langsung oleh CPU, bukan teks untuk dibaca manusia. Sebaliknya, `sapa.sh` termasuk **interpreted** (shell script), isinya teks biasa yang diterjemahkan Bash (sesuai shebang-nya) baris demi baris, sehingga terbaca normal di `cat`.

| | Interpreted | Compiled |
|---|---|---|
| Isi | teks biasa | kode mesin (biner) |
| Dijalankan oleh | interpreter (Bash, Python) | CPU langsung |
| Contoh | `.sh`, `.py` | Go, C, C++, Rust, `/usr/bin/sh` |

---

### Soal 10 — Buku panduan dan memantau proses

> 📝 **Soal:** Buka buku panduan perintah `ps`, cari kata `memory` di dalamnya, lompat ke kemunculan berikutnya, lalu keluar. Setelah itu pantau proses secara langsung memakai `top`, urutkan berdasarkan pemakaian RAM terbanyak, sebutkan satu proses yang ada di urutan paling atas (kolom COMMAND), lalu keluar.

✅ **Jawaban**

```bash
man ps
```

Di dalam `man`: ketik `/memory` lalu Enter, tekan `n` untuk kemunculan berikutnya, lalu `q` untuk keluar. Setelah kembali ke prompt biasa:

```bash
top
```

Di dalam `top`: tekan **`M`** huruf besar (Shift + m) untuk mengurutkan berdasarkan RAM, lihat kolom COMMAND di baris paling atas, lalu `q` untuk keluar.

Hasil di VM-mu setelah `M`:

```text
  PID USER  PR  NI    VIRT    RES    SHR S  %CPU  %MEM  TIME+ COMMAND
 1537 root  20   0  366076  46396  40104 S   0.0   1.3  0:02.02 fwupd
 1080 root  20   0 1854600  42240  28716 S   0.0   1.2  0:03.24 snapd
 1138 root  20   0  126100  32924  18312 S   0.0   0.9  0:00.88 unattended-upgr
```

Proses teratas berdasarkan RAM adalah **`fwupd`** (1,3%).

⚠️ Tombol `M` hanya bekerja **di dalam `top`**, bukan di dalam `man`. Kedua tampilan dibuka dengan perintahnya sendiri-sendiri dan harus ditutup dengan `q` dulu. Kalau muncul `set mark:` di bawah layar, tekan `Esc` lalu `q`. Kalau kolom COMMAND terpotong, lebarkan jendela terminal.

---

### Soal 11 — Menghentikan proses di foreground

> 📝 **Soal:** Jalankan proses tiruan `sleep 300` di layar utama (foreground) tanpa simbol latar belakang. Hentikan proses itu dari keyboard yang sama, tanpa terminal lain dan tanpa PID. Buktikan prosesnya sudah hilang dengan mencari kata `sleep` di daftar proses, lalu sebutkan sinyal yang dikirim oleh kombinasi tombol itu.

✅ **Jawaban**

```bash
sleep 300
```

Tekan **`Ctrl + C`** (tampil sebagai `^C`), lalu:

```bash
ps aux | grep sleep
```

Yang tersisa hanya baris `grep --color=auto sleep`.

💡 **Penjelasan:** `Ctrl + C` mengirim sinyal **SIGINT** (interrupt), yang menghentikan proses di foreground. Proses di background dihentikan dengan `kill` + PID.

⚠️ `Ctrl + S` bukan untuk menghentikan proses, melainkan **membekukan tampilan** terminal. Lanjutkan dengan `Ctrl + Q`.

---

### Soal 12 — Script, redirect, dan exit code

> 📝 **Soal:** Buat script bernama `cek.sh` yang memakai shebang Bash dan isinya dua baris perintah. Pertama, menjalankan `ls` pada folder `/folder_tidak_ada` (folder ini tidak ada), dengan pesan errornya disimpan ke file `galat2.txt`, bukan ke layar. Kedua, mencetak `Kode keluar: ` diikuti exit code dari perintah `ls` tadi. Beri izin eksekusi, jalankan, tampilkan isi `galat2.txt`, lalu jelaskan apakah angka yang muncul 0 atau bukan, dan artinya.

✅ **Jawaban**

```bash
nano cek.sh
```

Isi file `cek.sh` (tiga baris saja):

```bash
#!/bin/bash
ls /folder_tidak_ada 2> galat2.txt
echo "Kode keluar: $?"
```

```bash
chmod u+x cek.sh
./cek.sh
cat galat2.txt
```

Hasil:

```text
Kode keluar: 2
ls: cannot access '/folder_tidak_ada': No such file or directory
```

💡 **Penjelasan:** angka `2` **bukan 0**, jadi perintah `ls` keluar karena **error** (folder tidak bisa diakses). Aturannya: `0` sukses, selain `0` error.

⚠️ Baris `echo` harus tepat setelah baris `ls`, karena `$?` selalu milik perintah terakhir. Kata `echo` ditulis **sekali**, di luar tanda kutip (kamu sempat menulis `echo2`). Menampilkan file cukup `cat galat2.txt`, tanpa tambahan `$?`. Kalau muncul `./galat2.txt: Permission denied`, ada baris yang menjalankan nama file itu sebagai perintah.

---

### Soal 13 — PATH permanen lewat `.bashrc`

> 📝 **Soal:** Daftarkan folder `~/latihan_modul3` ke PATH secara **permanen**, lalu buktikan `sapa.sh` bisa dijalankan dari folder lain tanpa awalan `./`. Setelah terbukti, bersihkan lagi barisnya dari file konfigurasi. Langkahnya: cek alamat lengkap folder dengan `pwd`, tambahkan baris `export PATH=...` di baris paling bawah file konfigurasi terminal, baca ulang file itu di sesi aktif lalu jalankan `sapa.sh` dari `/tmp`, dan terakhir hapus barisnya dan pastikan sudah hilang dengan `tail -3`.

✅ **Jawaban**

```bash
cd ~/latihan_modul3
pwd
nano ~/.bashrc
```

Hasil `pwd`: `/home/magang/latihan_modul3`. Di nano, `Alt + /` untuk ke baris paling bawah, lalu tambahkan di bawah baris terakhir:

```bash
export PATH="$PATH:/home/magang/latihan_modul3"
```

Simpan (`Ctrl+O`, Enter), keluar (`Ctrl+X`), lalu:

```bash
source ~/.bashrc
cd /tmp
sapa.sh
```

Hasil: `Selamat belajar Sistem Operasi!`. Pembuktian paling meyakinkan: buka **tab terminal baru**, lalu `echo $PATH` (berakhir di `/home/magang/latihan_modul3`), `cd /tmp`, `sapa.sh`.

Bersihkan setelah terbukti:

```bash
nano ~/.bashrc          # kursor di baris export, Ctrl+K, simpan, keluar
tail -3 ~/.bashrc
```

Baris `export` tidak boleh muncul lagi, dan baris terakhir kembali `fi`.

💡 **Penjelasan:** `export PATH=...` yang diketik langsung di terminal hanya berlaku **sementara** dan hilang saat terminal ditutup. Supaya **permanen**, baris itu ditulis di `~/.bashrc`, karena file itu dibaca setiap terminal baru dibuka.

⚠️ Menjalankan `sapa.sh` dari folder `latihan_modul3` sendiri, atau dari terminal yang sudah di-`export`, **tidak membuktikan apa-apa**. Buktikan dari folder lain atau dari tab terminal baru.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-3-set-2"></a>

## Latihan Set 2 (17 soal)

Set ini dikerjakan di folder **`latihan_os`** (script `info_saya.sh`, `halo.py`). Soal 1 sampai 16 berupa command, Soal 17 berupa penjelasan.

> 💡 **Catatan:** isi `echo` pada soal ini memakai nama contoh (`Kim Juun`, `Junnie`). Saat ujian, pakai tulisan **persis seperti yang diminta soal**.

### Soal 1 — Membuat folder dan masuk ke dalamnya

> 📝 **Soal:** Buat direktori baru bernama `latihan_os` di direktori home, lalu masuk ke dalamnya.

✅ **Jawaban**

```bash
mkdir latihan_os
cd latihan_os
```

💡 Prompt berubah menjadi `~/latihan_os`, tandanya sudah masuk ke folder.

⚠️ `mkdir` hanya membuat folder, tidak otomatis masuk. Perlu `cd` setelahnya.

---

### Soal 2 — Membuat shell script dengan shebang

> 📝 **Soal:** Di dalam folder `latihan_os`, buat script `info_saya.sh` memakai `nano`. Isinya shebang Bash yang valid di baris pertama dan perintah `echo` yang mencetak `Nama: [Nama Kamu] | Kegiatan: Latihan Modul 3 SO Lagi Jalan`.

✅ **Jawaban**

```bash
nano info_saya.sh
```

Isi file `info_saya.sh`:

```bash
#!/bin/bash
echo "Nama: Kim Juun | Kegiatan: Latihan Modul 3 SO Lagi Jalan"
```

Simpan dengan `Ctrl+O` lalu Enter, keluar dengan `Ctrl+X`. Cek isinya dengan `cat info_saya.sh`.

⚠️ Shebang wajib di **baris paling atas**. Kalau ada baris kosong atau teks lain sebelumnya, shebang tidak berfungsi.

---

### Soal 3 — Memberi izin eksekusi dan menjalankan script

> 📝 **Soal:** Beri izin eksekusi pada `info_saya.sh` memakai `chmod`, lalu jalankan script untuk menguji hasil.

✅ **Jawaban**

```bash
chmod u+x info_saya.sh
./info_saya.sh
```

Hasil: `Nama: Kim Juun | Kegiatan: Latihan Modul 3 SO Lagi Jalan`.

⚠️ `chmod +x` juga diterima (izin execute ke semua pengguna), sedangkan `u+x` hanya untuk pemilik file. Tanpa `chmod`, muncul `Permission denied`.

---

### Soal 4 — Mendaftarkan folder ke PATH

> 📝 **Soal:** Daftarkan path absolut direktori `latihan_os` ke variabel lingkungan `$PATH` memakai `export`.

✅ **Jawaban**

```bash
pwd
export PATH="$PATH:/home/magang/latihan_os"
echo $PATH
```

Hasil `echo $PATH`: isi PATH lama, lalu `:/home/magang/latihan_os` di ujung.

⚠️ Kalau lupa `$PATH:` di dalam tanda kutip, isi PATH lama **tertimpa** dan semua perintah (`ls`, `sed`, dan lain-lain) menjadi `command not found`. Alamat juga harus diawali `/`. Kalau sudah terlanjur rusak, buka tab terminal baru, atau isi ulang PATH dengan folder bawaan Ubuntu:

```bash
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
```

Kalau tanda kutip lupa ditutup, prompt berubah menjadi `>`, keluar dengan `Ctrl+C`.

---

### Soal 5 — Memanggil script dari mana saja

> 📝 **Soal:** Pindah ke direktori home, lalu buktikan bahwa `info_saya.sh` bisa dipanggil langsung tanpa `./`.

✅ **Jawaban**

```bash
cd
info_saya.sh
```

Hasil: `Nama: Kim Juun | Kegiatan: Latihan Modul 3 SO Lagi Jalan`.

💡 Bisa jalan dari folder mana pun karena shell mencari file di semua folder yang ada di PATH, dan `latihan_os` sudah didaftarkan di Soal 4.

---

### Soal 6 — Mengalihkan stdout ke file

> 📝 **Soal:** Kembali ke `latihan_os`, lalu alihkan keluaran dari eksekusi `info_saya.sh` ke file `hasil.txt` dan tampilkan isi file-nya.

✅ **Jawaban**

```bash
cd latihan_os
info_saya.sh > hasil.txt
cat hasil.txt
```

Hasil `cat hasil.txt`: satu baris `Nama: Kim Juun | Kegiatan: Latihan Modul 3 SO Lagi Jalan`.

⚠️ `cat info_saya.sh > hasil.txt` **salah**, karena itu menyalin isi kode script (ada `#!/bin/bash` dan `echo`), bukan hasil eksekusinya. Yang di kiri `>` harus perintah yang **menjalankan** script. Mengetik `hasil.txt` saja menghasilkan `Permission denied`, gunakan `cat`.

---

### Soal 7 — Mengalihkan stderr ke file

> 📝 **Soal:** Coba baca file yang tidak ada bernama `file_hilang.txt`, lalu alihkan pesan error-nya ke file `log_error.txt` dan tampilkan isinya.

✅ **Jawaban**

```bash
cat file_hilang.txt 2> log_error.txt
cat log_error.txt
```

Hasil `cat log_error.txt`: `cat: file_hilang.txt: No such file or directory`.

💡 `>` hanya untuk stdout, pesan error lewat jalur stderr sehingga butuh `2>`.

---

### Soal 8 — Pipeline ke `grep`

> 📝 **Soal:** Sambungkan eksekusi `info_saya.sh` ke `grep` memakai pipe, supaya hanya baris yang memuat kata "Kegiatan" yang tampil.

✅ **Jawaban**

```bash
info_saya.sh | grep "Kegiatan"
```

Hasil: `Nama: Kim Juun | Kegiatan: Latihan Modul 3 SO Lagi Jalan`.

⚠️ `echo info_saya.sh` salah karena hanya mencetak tulisan nama file, bukan menjalankan script. `wc -w` tidak dipakai di soal ini. Flag `-i` pada `grep` membuat pencarian tidak membedakan huruf besar dan kecil.

---

### Soal 9 — Memeriksa exit code

> 📝 **Soal:** Jalankan perintah yang sukses lalu periksa exit code-nya. Jalankan perintah yang sengaja salah lalu periksa lagi. Sebutkan angka dan artinya.

✅ **Jawaban**

```bash
ls
echo $?
hello world
echo $?
```

Hasil: `echo $?` pertama menampilkan `0`, artinya proses terakhir **sukses**. `echo $?` kedua menampilkan `127`, artinya perintah **tidak ditemukan** (`command not found`).

💡 Aturannya `0` sukses, angka selain `0` error. Kode `126` muncul untuk `Permission denied`.

⚠️ Spasi di `echo $?` wajib ada, karena `echo$?` dibaca sebagai satu nama perintah yang tidak ada.

---

### Soal 10 — Menjalankan proses di background

> 📝 **Soal:** Jalankan proses simulasi di latar belakang memakai `sleep 6000 &`, lalu catat nomor PID yang tampil.

✅ **Jawaban**

```bash
sleep 6000 &
```

Hasil: `[1] 4710`. Nomor PID adalah angka kedua, yaitu `4710`.

⚠️ Angka di dalam kurung siku (`[1]`) itu **nomor job**, bukan PID. Tanda `&` membuat terminal tetap bisa dipakai.

---

### Soal 11 — Membuktikan proses aktif dan membaca STAT

> 📝 **Soal:** Buktikan proses tiruan aktif di RAM dengan `ps aux` dan `grep` melalui pipeline, lalu sebutkan statusnya (STAT).

✅ **Jawaban**

```bash
ps aux | grep sleep
```

Hasil: baris `magang 4710 ... S ... sleep 6000`, dan satu baris lain `grep --color=auto sleep`. STAT-nya `S`, artinya *Interruptible Sleep* (tidur menunggu).

⚠️ Baris `grep --color=auto sleep` itu proses `grep` sendiri yang ikut tertangkap karena perintahnya memuat kata "sleep", jadi bukan proses `sleep` kamu.

---

### Soal 12 — Menghentikan proses dengan `kill`

> 📝 **Soal:** Hentikan paksa proses tersebut berdasarkan PID-nya, lalu verifikasi dengan `ps aux | grep sleep` bahwa proses sudah hilang.

✅ **Jawaban**

```bash
kill 4710
ps aux | grep sleep
```

Hasil: muncul pesan `Terminated`, dan `ps aux | grep sleep` hanya menyisakan baris `grep` sendiri.

⚠️ Kalau tersisa baris `grep` saja, berarti proses `sleep` asli sudah mati. Pastikan PID yang dimasukkan sesuai dengan yang tampil di Soal 10.

---

### Soal 13 — Membuka dan mencari di manual

> 📝 **Soal:** Buka buku manual perintah `ps`, cari kata kunci `aux` di dalamnya, lalu keluar.

✅ **Jawaban**

```bash
man ps
```

Di dalam manual: ketik `/aux` lalu Enter untuk mencari, tekan `q` untuk keluar.

💡 `/` untuk mencari, `q` untuk keluar. Tombol keluar yang sama dipakai di `top`.

---

### Soal 14 — Menampilkan teks otomatis lewat `.bashrc`

> 📝 **Soal:** Buat supaya setiap terminal baru dibuka, otomatis muncul teks `Halo Junnie, selamat belajar SO!`, lalu buktikan berhasil.

✅ **Jawaban**

```bash
ls -a ~
nano ~/.bashrc
```

Tambahkan satu baris di paling bawah file:

```bash
echo "Halo Junnie, selamat belajar SO!"
```

Simpan dengan `Ctrl+O` lalu Enter, keluar dengan `Ctrl+X`. Buktikan dengan menutup terminal lalu membuka yang baru, teks muncul di baris paling atas (alternatifnya `source ~/.bashrc`). Setelah itu **hapus lagi** baris `echo` tadi.

⚠️ Tulisan tanpa `echo` dibaca bash sebagai nama perintah, hasilnya `command not found`. Cocokkan ejaan teks dengan soal huruf per huruf.

---

### Soal 15 — Script Python dengan shebang

> 📝 **Soal:** Buat script Python `halo.py` yang mencetak `Halo dari Python!` dan bisa dijalankan langsung dengan `./halo.py`.

✅ **Jawaban**

```bash
nano halo.py
```

Isi file `halo.py`:

```python
#!/usr/bin/python3
print("Halo dari Python!")
```

```bash
chmod u+x halo.py
./halo.py
```

Hasil: `Halo dari Python!`.

⚠️ Shebang Python berbeda dari Bash (`/usr/bin/python3`, bukan `/bin/bash`). Tanpa `chmod`, muncul `Permission denied`.

---

### Soal 16 — Memantau CPU dan RAM dengan `top`

> 📝 **Soal:** Pantau penggunaan CPU dan RAM secara langsung, urutkan berdasarkan pemakaian RAM, lalu keluar. Tulis perintah dan tombolnya.

✅ **Jawaban**

```bash
top
```

Di dalam `top`: tekan `Shift + M` (huruf besar M) untuk mengurutkan berdasarkan RAM, lalu tekan `q` untuk keluar.

⚠️ Urutan bawaan `top` adalah berdasarkan CPU. Huruf besar dan kecil berbeda fungsi di `top`, dan tidak memakai tombol `Ctrl`.

---

### Soal 17 — Interpreted vs compiled (penjelasan)

> 📝 **Soal:** Jelaskan (a) beda interpreted dan compiled program beserta contoh, dan (b) kenapa `cat /bin/sh` menampilkan simbol aneh sedangkan `cat info_saya.sh` terbaca.

✅ **Jawaban**

**(a)** *Interpreted* program isinya teks biasa yang dibaca baris demi baris oleh program lain bernama interpreter, contohnya file Python (`.py`) dan Bash (`.sh`). *Compiled* program sudah diubah total menjadi kode mesin (biner) yang langsung dijalankan CPU tanpa penerjemah, contohnya hasil C, C++, Go, Rust.

**(b)** `/bin/sh` itu compiled executable berisi kode mesin untuk CPU, bukan teks, sehingga terminal menampilkannya sebagai simbol aneh. `info_saya.sh` hanya file teks biasa berisi perintah yang nanti dibaca interpreter, jadi `cat` menampilkannya sebagai tulisan terbaca.

💡 Kunci jawabannya ada pada **siapa yang membaca file**: interpreter (baris demi baris) atau langsung CPU.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="contekan-modul-3"></a>

## 📌 Contekan Modul 3

### Script dan environment

| Konsep / perintah | Fungsi |
|---|---|
| `which sh` | lokasi program CLI |
| `cat /usr/bin/sh` | isinya simbol aneh karena **compiled** (`reset` untuk memulihkan terminal) |
| `#!/bin/bash` / `#!/usr/bin/python3` | **shebang**, baris pertama script, menentukan penerjemah |
| `chmod u+x` + `./nama.sh` | beri izin eksekusi dan jalankan script di folder sendiri |
| `ls -a ~` | lihat file tersembunyi (flag `-a` = all) |
| `~/.bashrc` | file aturan terminal, dibaca tiap terminal baru |
| `source ~/.bashrc` | baca ulang di sesi aktif |
| `echo $PATH` | daftar folder pencarian perintah, dipisah `:` |
| `export PATH="$PATH:/folder"` | tambah folder ke PATH (sementara). **`$PATH:` wajib ada**, kalau tidak PATH tertimpa |
| `export PATH=""` | kosongkan PATH, perintah jadi `command not found` (hanya di tab itu) |
| `export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"` | pulihkan PATH bawaan Ubuntu |

### Aliran data dan proses

| Konsep / perintah | Fungsi |
|---|---|
| `>` | alihkan hasil sukses (stdout) ke file |
| `2>` | alihkan pesan error (stderr) ke file |
| `\|` | sambung hasil perintah kiri jadi masukan perintah kanan |
| `script.sh \| grep "kata"` | jalankan script, saring hasilnya (bukan `cat script \| ...`) |
| `wc -w` / `wc -l` | hitung kata / hitung baris |
| `ps aux` | daftar semua proses (USER, PID, %CPU, %MEM, STAT) |
| `top` | pantau langsung. `M` urut RAM, `q` keluar |
| `sleep 9000 &` | proses di background (`&`), keluar `[nomor job] PID` |
| `kill PID` | bunuh proses |
| `Ctrl + C` | hentikan proses di foreground (**SIGINT**) |
| `echo $?` | exit code perintah terakhir. `0` sukses, `126` tidak boleh dieksekusi, `127` tidak ditemukan |
| `man ps` | buku panduan. `/kata` cari, `n` berikutnya, `q` keluar |

STAT pada `ps`: `S` = *interruptible sleep* (tidur menunggu), `T` = stopped, `Z` = zombie.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-4"></a>

# 🔒 Modul 4 · Sinkronisasi Proses

8 soal (6 latihan + 2 posttest), dikerjakan dengan **Python** (`threading`) di folder home dan `posttest4`. Editor yang dipakai di sesi ini: `micro` (simpan `Ctrl+S`, keluar `Ctrl+Q`). Di `nano`: simpan `Ctrl+O` lalu Enter, keluar `Ctrl+X`.

### Teori inti

| Konsep | Ingat ini |
|---|---|
| **Race condition** | hasil bergantung urutan eksekusi thread yang tidak bisa diprediksi. Syarat (**K-S-M-A**): **K**onkurensi, **S**umber daya bersama, **M**odifikasi, operasi **bukan A**tomik |
| **Critical section** | 4 segmen: **Entry, Critical, Exit, Remainder** |
| **3 syarat solusi** | Mutual Exclusion, Progress, Bounded Waiting |
| **Mutex** (`threading.Lock()`) | 1 thread, punya *ownership*, untuk melindungi **1 data** |
| **Semaphore** (`threading.Semaphore(N)`) | N thread, tanpa ownership, untuk **membatasi kapasitas**. Jika N > 1 dipakai melindungi 1 variabel, race condition tetap bisa terjadi |
| **Metode eksplisit** | `acquire()` **sebelum** `try`, `release()` di `finally` |
| **Metode implisit** | `with kunci:` (otomatis acquire/release, aman walau terjadi error) |
| **Masalah lain** | Deadlock, Starvation, Priority Inversion |

---

### Soal 1 — Race condition (teori)

> 📝 **Soal:** Jelaskan apa itu race condition dan sebutkan empat syarat terjadinya.

✅ **Jawaban**

Race condition = beberapa thread mengubah data bersama secara bersamaan sehingga hasil tidak dapat diprediksi. Empat syaratnya: **Konkurensi**, **Sumber daya bersama**, **Modifikasi**, dan operasi **non-atomik** (K-S-M-A).

📌 Skor: 10/10.

---

### Soal 2 — Segmen eksekusi dan 3 syarat solusi (teori)

> 📝 **Soal:** Sebutkan empat segmen eksekusi pada critical section beserta fungsinya, dan tiga syarat sebuah solusi dianggap benar.

✅ **Jawaban**

- **Entry**: minta izin masuk.
- **Critical**: mengubah data bersama (hanya 1 thread).
- **Exit**: melepas izin.
- **Remainder**: kode biasa di luar critical section.

Tiga syarat solusi: **Mutual Exclusion**, **Progress**, **Bounded Waiting**.

📌 Skor: 10/10.

---

### Soal 3 — Command + Mutex eksplisit (`kasir.py`)

> 📝 **Soal:** Program kasir memakai 4 thread, masing-masing melakukan 50 penjualan. Tanpa Lock hasil total kas hanya **50**, seharusnya **200**. Jalankan `kasir.py` tiga kali untuk membuktikan hasilnya salah, salin menjadi `kasir_aman.py`, lalu perbaiki dengan **Mutex eksplisit** (`acquire` dan `release`) dan buktikan hasilnya 200.

✅ **Jawaban**

```bash
micro kasir.py
python3 kasir.py          # 3x, hasil 50
cp kasir.py kasir_aman.py
micro kasir_aman.py
python3 kasir_aman.py     # hasil 200
```

```python
kunci = threading.Lock()
def jual(id_kasir):
    global total_kas
    for i in range(50):
        kunci.acquire()
        try:
            sementara = total_kas
            time.sleep(0.0001)
            total_kas = sementara + 1
        finally:
            kunci.release()
```

💡 Tiga baris yang dilindungi adalah **baca, sleep, tulis**. Selama satu thread di dalam blok itu, thread lain menunggu di `acquire()`.

📌 Skor: 15/15.

---

### Soal 4 — Mutex implisit (`kasir_with.py`)

> 📝 **Soal:** Salin `kasir.py` menjadi `kasir_with.py`, lalu amankan dengan **Mutex implisit** (`with`). Jalankan 3 kali, hasil harus 200.

✅ **Jawaban**

```bash
cp kasir.py kasir_with.py
micro kasir_with.py
python3 kasir_with.py     # 3x, hasil 200
```

```python
with kunci:
    sementara = total_kas
    time.sleep(0.0001)
    total_kas = sementara + 1
```

📌 Skor: 20/20.

---

### Soal 5 — Semaphore implisit (`loket.py`, `loket_batas.py`)

> 📝 **Soal:** Ada 5 pembeli dan 2 petugas loket. Buat `loket.py` tanpa pembatas (semua dilayani sekaligus), lalu salin menjadi `loket_batas.py` dan batasi dengan **Semaphore implisit** supaya maksimal 2 pembeli dilayani sekaligus.

✅ **Jawaban**

```bash
micro loket.py
python3 loket.py           # semua dilayani sekaligus
cp loket.py loket_batas.py
micro loket_batas.py
python3 loket_batas.py     # maksimal 2 sekaligus
```

```python
layanan = threading.Semaphore(2)
def beli_tiket(id_p):
    print(f"[ANTRE] Pembeli-{id_p} datang...")
    with layanan:
        print(f"[DILAYANI] Pembeli-{id_p} sedang dilayani.")
        time.sleep(2)
        print(f"[SELESAI] Pembeli-{id_p} selesai.")
```

📌 Skor: 20/20.

---

### Soal 6 — Analisis dan perbandingan (teori)

> 📝 **Soal:** Bandingkan Mutex dan Semaphore, jelaskan kenapa Semaphore N > 1 tidak aman untuk melindungi satu variabel, jelaskan Deadlock, Starvation, dan Priority Inversion, serta bandingkan Binary Semaphore dengan Mutex.

✅ **Jawaban**

- **Mutex**: 1 thread, ada ownership, untuk 1 data. **Semaphore**: N thread, tanpa ownership, untuk kapasitas.
- Semaphore N > 1 tidak aman untuk 1 variabel karena beberapa thread masuk bersamaan dan bisa saling menimpa.
- **Deadlock**: saling menunggu selamanya. **Starvation**: thread tidak pernah kebagian giliran. **Priority Inversion**: thread prioritas tinggi tertunda oleh thread prioritas rendah yang terhambat thread menengah.
- **Binary Semaphore** (value=1) mirip Mutex tapi tanpa ownership, jadi **Mutex lebih aman**.

📌 Skor: 25/25.

---

### Posttest 4 Bagian A — Flash Sale Tiket (Mutex implisit)

> 📝 **Soal:** Di folder `posttest4`, buat `tiket_konser.py`: `sisa_tiket = 100`, 100 thread, `time.sleep(0.001)`, tiap thread membaca sisa tiket lalu menguranginya 1. Jalankan minimal 3 kali tanpa Lock (hasil bukan 0), lalu amankan dengan **Mutex implisit** sampai hasil selalu 0. Jelaskan cara kerja dan segmen critical section-nya.

✅ **Jawaban**

```bash
mkdir posttest4
cd posttest4
micro tiket_konser.py
python3 tiket_konser.py   # minimal 3x, hasil 95-97 (bukan 0)
```

Setelah diberi Lock implisit (`with kunci:` membungkus 3 baris: baca, sleep, kurangi), hasil selalu **0**.

💡 **Penjelasan:**
- Mutex menjamin *mutual exclusion* lewat penguncian. `with` memakai *Context Manager*: acquire saat masuk, release saat keluar (termasuk saat error).
- Segmen: **Entry** = `with kunci:`, **Critical** = baca/sleep/kurangi, **Exit** = keluar blok `with`, **Remainder** = kode di luar `with`.
- Dipakai Mutex, bukan Semaphore N > 1, karena `sisa_tiket` adalah satu data yang harus eksklusif.
- Implisit lebih aman karena `release` tetap terpanggil saat *exception*.

📌 Skor: 35/35.

---

### Posttest 4 Bagian B — Kuota Payment Gateway (Semaphore eksplisit)

> 📝 **Soal:** (Versi diubah: loket pembayaran, 6 thread, kapasitas 2, file `loket_bayar.py`.) Di folder `posttest4`, buat program yang membatasi maksimal 2 pembayaran diproses bersamaan memakai **Semaphore eksplisit**. Tampilkan hasil tanpa pembatas (6 `[PROSES]` serentak) lalu dengan pembatas, dan jelaskan peran `release()` di `finally`.

✅ **Jawaban**

```bash
cd
cd posttest4
pwd
micro loket_bayar.py
ls -l
python3 loket_bayar.py    # 6 [PROSES] serentak (overload) sebelum diberi pembatas
```

```python
MAX_SLOT = 2
slot = threading.Semaphore(MAX_SLOT)

def proses_bayar(id_bayar):
    slot.acquire()                 # sebelum try
    try:
        print(f"[PROSES] Pembayaran-{id_bayar} sedang diproses...")
        time.sleep(2)
        print(f"[SELESAI] Pembayaran-{id_bayar} selesai.")
    finally:
        slot.release()             # satu-satunya isi finally

for i in range(1, JUMLAH_THREAD + 1):   # ID 1 sampai 6
    ...
```

💡 **Penjelasan:**
- Semaphore = *counter*: `acquire` mengurangi 1 (antre jika 0), `release` menambah 1 dan memberi sinyal.
- `release()` wajib di `finally` agar selalu terpanggil. Jika gagal, slot hilang permanen, thread lain menunggu selamanya (mirip deadlock) dan bisa terjadi starvation.
- Dipakai Semaphore karena tujuannya **membatasi kapasitas**, bukan eksklusif 1 thread. Semaphore N > 1 untuk 1 variabel saldo: race condition masih bisa terjadi.

📌 Skor: 35/35.

### Ringkasan skor Modul 4

| Bagian | Skor |
|---|:---:|
| Latihan (Soal 1-6) | 100/100 |
| Posttest A | 35/35 |
| Posttest B | 35/35 |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

## 📌 Contekan Modul 4

| Konsep / perintah | Fungsi |
|---|---|
| `kunci = threading.Lock()` | buat Mutex |
| `with kunci:` | Mutex **implisit** (otomatis acquire/release) |
| `kunci.acquire()` → `try:` → `finally: kunci.release()` | Mutex **eksplisit** |
| `threading.Semaphore(N)` | batasi N thread sekaligus (kapasitas) |
| `slot.acquire()` sebelum `try`, `slot.release()` di `finally` | Semaphore eksplisit |
| `range(1, N + 1)` | ID 1 sampai N |
| K-S-M-A | syarat race condition |
| Entry · Critical · Exit · Remainder | 4 segmen critical section |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-5"></a>

# 🧩 Modul 5 · Deadlock

5 soal latihan (skor 98/100), dikerjakan dengan Python. Contoh tema: dua koki berebut pisau dan talenan.

### Teori inti

| Konsep | Ingat ini |
|---|---|
| **Deadlock** | dua proses atau lebih saling menunggu selamanya (CPU mendekati 0%) |
| **4 syarat (M-H-N-C)** | **M**utual Exclusion, **H**old and Wait, **N**o Preemption, **C**ircular Wait. **Semua** harus terpenuhi |
| **4 penanganan** | Prevention, Avoidance (Algoritma Banker), Detection and Recovery (Wait-For Graph), Ignorance |
| **Livelock** | tidak diam, tapi tidak ada kemajuan (dicegah dengan jeda acak) |
| **Banker** | Available, Max, Allocation, **Need = Max − Allocation**. **DITUNDA** = resource belum ada. **DITOLAK** = ada tapi berbahaya (tidak aman) |

---

### Soal 1 — Simulasi deadlock (`dapur.py`)

> 📝 **Soal:** Koki A mengambil pisau lalu talenan, Koki B mengambil talenan lalu pisau. Jalankan `dapur.py` di latar belakang, tunggu 5 detik, lihat status prosesnya (PID, STAT, %CPU), hentikan prosesnya, lalu cek bahwa sudah bersih. Berapa %CPU-nya dan apakah "Semua koki selesai" muncul?

✅ **Jawaban**

```bash
python3 dapur.py &
sleep 5
ps -o pid,stat,pcpu,cmd -C python3
kill <PID>          # atau kill %nomor_job
ps -o pid,stat,pcpu,cmd -C python3   # cek bersih
```

💡 %CPU mendekati **0.0** (proses hanya menunggu). "Semua koki selesai" **tidak muncul** karena kedua koki saling menunggu selamanya.

⚠️ `Ctrl+C` tidak mematikan job background, gunakan `kill`.

📌 Skor: 15/15.

---

### Soal 2 — Urutan kunci konsisten (`dapur_urut.py`)

> 📝 **Soal:** Salin `dapur.py` menjadi `dapur_urut.py`. Ubah supaya kedua koki mengambil kunci dengan urutan yang sama, lalu jalankan dan jelaskan syarat deadlock mana yang diputus.

✅ **Jawaban**

```bash
cp dapur.py dapur_urut.py
micro dapur_urut.py
cat dapur_urut.py
python3 dapur_urut.py
```

`koki_b` diubah menjadi **pisau dulu, lalu talenan** (sama dengan `koki_a`). Hasil: "Semua koki selesai" muncul.

💡 Urutan yang konsisten memutus **Circular Wait**.

⚠️ Skor 18/20: tampilkan `cp`, `cat`, dan `python3` di log supaya penilaian lengkap.

---

### Soal 3 — Timeout dan mundur (`dapur_mundur.py`)

> 📝 **Soal:** Salin `dapur.py` menjadi `dapur_mundur.py`. Ubah `koki_b` supaya mencoba mengambil pisau dengan `timeout`. Jika gagal, lepas talenan yang dipegang lalu coba lagi setelah jeda acak. Jelaskan syarat deadlock yang diputus dan kenapa jeda acak dipakai.

✅ **Jawaban**

```bash
cp dapur.py dapur_mundur.py
micro dapur_mundur.py
cat dapur_mundur.py
python3 dapur_mundur.py
```

```python
def koki_b():
    while True:
        print("[Koki B] ambil talenan")
        talenan.acquire()
        print("[Koki B] DAPAT talenan")
        time.sleep(1)
        print("[Koki B] mau ambil pisau...")
        if pisau.acquire(timeout=1):
            print("[Koki B] DAPAT pisau, mulai masak")
            pisau.release()
            talenan.release()
            break
        print("[Koki B] GAGAL, lepas talenan lalu coba lagi")
        talenan.release()
        time.sleep(random.uniform(0.1, 0.5))
```

💡 Memutus **No Preemption** (kunci yang dipegang dilepas paksa). Jeda acak mencegah **livelock** (dua koki mundur dan mencoba lagi bersamaan terus-menerus).

⚠️ Di jalur gagal yang dilepas adalah **talenan** (yang benar-benar dipegang). Jangan lupa `break` di jalur berhasil.

📌 Skor: 20/20.

---

### Soal 4 — Algoritma Banker (`bankir.py`, `bankir2.py`)

> 📝 **Soal:** Lengkapi `bankir.py` (Algoritma Banker), jalankan, lalu salin menjadi `bankir2.py` dan ubah permintaan `minta("P2", [6,0,0])` menjadi `[1,0,0]`. Jelaskan beda hasil **DITUNDA** dan **DITOLAK**.

✅ **Jawaban**

```bash
micro bankir.py
cat bankir.py
python3 bankir.py
cp bankir.py bankir2.py
micro bankir2.py     # ubah minta("P2", [6,0,0]) jadi [1,0,0]
cat bankir2.py
python3 bankir2.py
```

Hasil: P1 dan P0 **DITOLAK** (tidak aman). P2 `[6,0,0]` = **DITUNDA** (melebihi Available `[3,3,2]`), P2 `[1,0,0]` = **DITOLAK** (resource ada tetapi tidak aman).

💡 DITUNDA = resource memang **belum ada**. DITOLAK = resource **ada, tetapi** memberikannya membuat sistem masuk keadaan tidak aman.

⚠️ Perhatikan `a = b[0]`: variabel yang diisi ada di **kiri** `=`. Jangan menyalin nama fungsi/variabel dari modul, pakai nama dari soal.

📌 Skor: 20/20.

---

### Soal 5 — Deteksi dan pemulihan (`kantor.py`, `kantor_pulih.py`)

> 📝 **Soal:** Jalankan `kantor.py` untuk mendeteksi deadlock memakai Wait-For Graph, salin menjadi `kantor_pulih.py`, lalu tambahkan pemulihan dengan menghentikan satu proses korban dan tunjukkan sistem menjadi aman.

✅ **Jawaban**

```bash
micro kantor.py
python3 kantor.py
cp kantor.py kantor_pulih.py
micro kantor_pulih.py
cat kantor_pulih.py
python3 kantor_pulih.py
```

```python
def hentikan(memegang, menunggu, korban):
    memegang_baru = {r: p for r, p in memegang.items() if p != korban}
    menunggu_baru = {p: r for p, r in menunggu.items() if p != korban}
    return memegang_baru, menunggu_baru

if siklus:
    korban = siklus[0]
    print(f"\n[Recovery] Menghentikan {korban}")
    memegang, menunggu = hentikan(memegang, menunggu, korban)
    laporan("Setelah recovery", memegang, menunggu)
```

Hasil: sebelum recovery `DEADLOCK! siklus: Andi -> Budi -> Citra -> Andi`, korban Andi dihentikan, setelah recovery `Aman, tidak ada siklus`.

💡 **Wait-For Graph:** proses = node, menunggu = panah, **siklus = deadlock**. Ini contoh *process termination*.

⚠️ Perhatikan indent: kode setelah `return` tidak pernah jalan.

📌 Skor: 25/25.

### Ringkasan skor Modul 5

| Soal | Skor |
|---|:---:|
| 1 | 15/15 |
| 2 | 18/20 |
| 3 | 20/20 |
| 4 | 20/20 |
| 5 | 25/25 |
| **Total** | **98/100** |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

## 📌 Contekan Modul 5

| Konsep | Ingat ini |
|---|---|
| **M-H-N-C** | Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait |
| Urutan kunci sama | memutus **Circular Wait** |
| `acquire(timeout=...)` + lepas + jeda acak | memutus **No Preemption**, jeda acak mencegah **livelock** |
| Banker | Need = Max − Allocation. DITUNDA (belum ada) vs DITOLAK (tidak aman) |
| Wait-For Graph | siklus = deadlock. Recovery = hentikan proses korban |
| `ps -o pid,stat,pcpu,cmd -C python3` | cek status dan %CPU proses Python |
| `python3 x.py &` → `kill PID` | jalankan di background, matikan dengan `kill` (bukan `Ctrl+C`) |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-6"></a>

# 🧠 Modul 6 · Manajemen Memori

Dua set latihan: **Set 1** (Memori 1, 7 soal praktik) dan **Set 2** (Memori 2, 11 soal: paging, swap, page replacement, segmentasi).

<a id="modul-6-set-1"></a>

## Latihan Set 1 · Memori 1 (7 soal)

7 soal latihan, semuanya mengikuti praktik di modul. Soal 8, 9, dan 10 yang sempat direncanakan dibatalkan karena di luar modul.

> 🛠️ **Koreksi modul** (supaya tidak tersangkut saat praktik):
> - `curl -o -L segfault.cpp ...` urutannya keliru. Yang benar: `curl -L -o segfault.cpp bit.ly/segfaultcpp`.
> - `rm /dev/shm/test_ram.img /tmp/test_disk.img` menunjuk lokasi salah. Berkas disk ada di home: `rm /dev/shm/test_ram.img ~/test_disk.img`.
> - Contoh PID di bagian `pmap` (10548, 10558, 10588) hanya contoh, PID milikmu pasti lain.

### Soal 1 — Uji kecepatan tulis RAM vs disk

> 📝 **Soal:** Dari folder home-mu (ketik `cd` dulu), tulis berkas berisi data nol berukuran 200 MiB ke dua tempat. Pertama ke RAM Disk dengan nama `uji_ram.img`, kedua ke disk fisik di folder home dengan nama `uji_disk.img` memakai penulisan langsung tanpa lewat page cache. Keduanya harus menampilkan kemajuan dan ringkasan kecepatan. Setelah itu hapus kedua berkas ujinya.

✅ **Jawaban**

```bash
cd
dd if=/dev/zero of=/dev/shm/uji_ram.img bs=1M count=200 status=progress
dd if=/dev/zero of=~/uji_disk.img bs=1M count=200 oflag=direct status=progress
rm /dev/shm/uji_ram.img ~/uji_disk.img
```

Hasil milikmu (baris ringkasan terakhir):

```text
209715200 bytes (210 MB, 200 MiB) copied, 2.15772 s, 97 MB/s     <- RAM Disk
209715200 bytes (210 MB, 200 MiB) copied, 2.88188 s, 73 MB/s     <- disk fisik
```

💡 **Penjelasan:** throughput = byte ÷ waktu. 209.715.200 ÷ 2,158 ≈ 97 MB/s dan ÷ 2,882 ≈ 73 MB/s. RAM lebih cepat, sesuai arah di modul bahwa **RAM tidak lebih lambat dari disk**. Selisihnya kecil dan angka RAM jauh di bawah contoh modul (1,1 GB/s), karena di mesin virtual `/dev/shm` dan disk sama-sama lewat lapisan virtualisasi, dan `dd` sendiri memakai sebagian waktu. Selisih lebar terutama terlihat di HDD.

| Bagian perintah | Arti |
|---|---|
| `dd` | penyalin data blok demi blok, dipakai sebagai alat uji tulis |
| `if=/dev/zero` | sumber data, terus menghasilkan byte 0 (kecepatan baca tidak ikut terukur) |
| `of=/dev/shm/...` | tujuan di `/dev/shm`, berada di **RAM** |
| `of=~/...` | tujuan di home, berada di **disk fisik** |
| `bs=1M` · `count=200` | blok 1 MiB × 200 = 200 MiB |
| `status=progress` | tampilkan kemajuan dan ringkasan kecepatan |
| `oflag=direct` | tulis langsung ke perangkat tanpa page cache (hanya untuk disk) |

⚠️ Kamu sempat salah ketik `uji_ram/img` (seharusnya `uji_ram.img`), dan `bs=` sempat terpotong ke baris baru. Tulis perintah dalam **satu baris utuh**.

---

### Soal 2 — Mengintip peta memori dengan `pmap`

> 📝 **Soal:** Dari folder home, unduh `mmu.cpp` dari `bit.ly/mmucpp`, kompilasi menjadi program `mmu`, dan jalankan di latar belakang supaya terminalmu tetap bisa dipakai. Catat PID yang dicetak program, lalu tampilkan peta memorinya dengan `pmap` dalam format lengkap (ada kolom RSS dan Dirty). Setelah itu, saring hasil `pmap` itu supaya hanya baris yang berisi kata `anon` yang muncul. Terakhir, hentikan proses `mmu` memakai PID-nya.

✅ **Jawaban**

```bash
cd
curl -L -o mmu.cpp bit.ly/mmucpp
g++ mmu.cpp -o mmu && ./mmu &
pmap -x 1577
pmap -x 1577 | grep "anon"
kill -9 1577
ps aux | grep mmu
```

Ganti `1577` dengan PID milikmu. Kalau `g++` belum ada: `sudo apt install g++`.

Potongan hasil `pmap -x 1577`:

```text
1577:   ./mmu
Address           Kbytes     RSS   Dirty Mode  Mapping
00005cf1db8ec000       4       4       0 r---- mmu
00005cf1db8ed000       4       4       0 r-x-- mmu
00005cf1db8ee000       4       4       0 r---- mmu
00005cf1db8ef000       4       4       4 r---- mmu
00005cf1db8f0000       4       4       4 rw--- mmu
00005cf217bec000     204       8       8 rw---   [ anon ]
...
00007ffee4f0b000     132      12      12 rw---   [ stack ]
ffffffffff600000       4       0       0 --x--   [ anon ]
---------------- ------- ------- -------
total kB            6900    3944     216
```

Hasil `pmap -x 1577 | grep "anon"`:

```text
00005cf217bec000     204       8       8 rw---   [ anon ]
000070d53e814000      52      20      20 rw---   [ anon ]
000070d53ec9c000      16      12      12 rw---   [ anon ]
000070d53ecb9000      20      20      20 rw---   [ anon ]
000070d53ee18000       8       8       8 rw---   [ anon ]
000070d53ee1a000      16       0       0 r----   [ anon ]
000070d53ee1e000       8       0       0 r----   [ anon ]
000070d53ee20000       8       8       0 r-x--   [ anon ]
000070d53ee60000       4       4       4 rw---   [ anon ]
ffffffffff600000       4       0       0 --x--   [ anon ]
```

Hasil setelah `kill -9`:

```text
magang      1577  0.0  0.0      0     0 pts/0    Z    01:35   0:00 [mmu] <defunct>
magang      1946  0.0  0.0   6716  2676 pts/0    S+   01:49   0:00 grep --color=auto mmu
```

💡 **Penjelasan:** heap ada di baris `00005cf217bec000 204 8 8 rw--- [ anon ]`: area virtual 204 KB, hanya 8 KB yang benar-benar di RAM (RSS), izin `rw---`. Segmen kode `mmu` berizin `r-x--`, stack ada di baris `[ stack ]` 132 KB `rw---`. Dari total 6900 KB ruang virtual, hanya 3944 KB di RAM dan 216 KB Dirty, artinya memori dimuat sesuai kebutuhan.

Kolom `pmap -x`:

| Kolom | Arti |
|---|---|
| Address | alamat virtual awal area |
| Kbytes | ukuran area di ruang alamat virtual |
| RSS | bagian yang benar-benar di RAM sekarang |
| Dirty | bagian yang sudah diubah dan belum disimpan kembali |
| Mode | r baca, w tulis, x eksekusi |
| Mapping | nama berkas, `[ anon ]` (memori anonim seperti heap), atau `[ stack ]` |

**Membuktikan alamat berada di sebuah area:** `awal ≤ alamat < awal + (Kbytes × 1024)`. Contoh heap `0x59059ba41020` pada area `0x59059ba2f000`, 204 KB: akhir = `0x59059ba2f000` + `0x33000` = `0x59059ba62000`, dan alamatnya memang di antara keduanya.

⚠️ Status proses sebelum dihentikan adalah `T` (stopped), karena program di background menunggu ENTER. `kill` biasa (SIGTERM) tidak bisa diterima proses yang beku, sedangkan `kill -9` (SIGKILL) tidak bisa ditolak. Setelah itu status `Z` dan memori `0 0` berarti proses sudah **mati**. Yang tersisa catatan **zombie** (`<defunct>`) karena induknya (shell lama) sudah ditutup. Zombie tidak memakai RAM dan hilang sendiri. `exit 1577` **bukan** perintah menghentikan proses, melainkan menutup sesi shell. Menjalankan dari terminal baru tidak masalah, yang penting PID-nya benar.

---

### Soal 3 — Segmentation fault dan exit code

> 📝 **Soal:** Dari folder home, unduh `segfault.cpp` dari `bit.ly/segfaultcpp`, kompilasi menjadi program `segfault`, dan jalankan. Programnya sengaja mengakses alamat memori ilegal. Langsung setelah program berhenti, tampilkan exit code-nya. Setelah itu tampilkan tiga baris terakhir catatan kernel (ring buffer) memakai hak akses administrator.

✅ **Jawaban**

```bash
cd
curl -L -o segfault.cpp bit.ly/segfaultcpp
g++ segfault.cpp -o segfault && ./segfault
echo $?
sudo dmesg | tail -n 3
```

Hasil milikmu:

```text
Memaksa akses alamat memori ilegal (0x0)...
Segmentation fault         (core dumped) ./segfault
139
[ 1658.786464] segfault[2051]: segfault at 0 ip 000065319d02117a sp 00007ffe3ee21810 error 6 in segfault[117a,65319d021000+1000] likely on CPU 0 (core 0, socket 0)
[ 1658.786637] Code: e5 48 83 ec 10 ...
```

💡 **Penjelasan:** exit code **139 = 128 + 11**, yaitu 128 ditambah nomor sinyal **SIGSEGV** (11). Program menulis ke alamat `0x0` (NULL) yang sengaja tidak dipetakan kernel. MMU tidak menemukan terjemahan valid, terjadi page fault yang tidak bisa diselesaikan, lalu kernel mengirim SIGSEGV. Dampaknya hanya ke proses `segfault`, shell dan sistem tetap normal.

Arti baris `dmesg`:

| Bagian | Arti |
|---|---|
| `at 0` | alamat yang diakses adalah `0x0` (NULL) |
| `ip` | instruction pointer, alamat instruksi penyebab pelanggaran |
| `sp` | stack pointer, posisi stack saat itu |
| `error 6` | kode page fault (lihat tabel di bawah) |

Kode `error N` adalah gabungan tiga bit (ubah ke biner, baca dari kanan):

| Bit | Jika 0 | Jika 1 |
|---|---|---|
| Bit 0 | halaman belum ada (alamat belum dipetakan) | halaman ada, tetapi aksesnya melanggar izin |
| Bit 1 | operasi baca | operasi tulis |
| Bit 2 | mode kernel | mode user (program biasa) |

| Kode | Biner | Artinya |
|:---:|:---:|---|
| 4 | `100` | membaca alamat yang belum dipetakan |
| **6** | `110` | menulis ke alamat yang belum dipetakan (**kasus ini**) |
| 7 | `111` | menulis ke area yang ada tetapi tidak boleh ditulis (misalnya area kode `r-x`) |

Tiga bukti untuk satu kejadian: pesan di terminal (dicatat **shell**), baris `dmesg` (dicatat **kernel**), dan angka 139 (dihitung **shell**).

⚠️ **Jangan** menambah `&` di ujung `./segfault`: `echo $?` lalu membaca status peluncurannya (`0`), bukan `139`, dan angka aslinya hanya muncul di laporan job `Exit 139`. Kalau `dmesg` tidak menampilkan baris segfault, ulangi `./segfault` lalu langsung `dmesg` lagi (pesan lama bisa tertimpa). Baris `workqueue: e1000_watchdog ...` di atasnya adalah catatan driver jaringan virtual, tidak berhubungan.

---

### Soal 4 — Simulasi partisi fixed vs dynamic

> 📝 **Soal:** Dari folder home, unduh `partitioning.cpp` dari `bit.ly/partitioningcpp`, kompilasi menjadi program `partitioning`, dan jalankan. Simpan seluruh keluarannya ke file `hasil_partisi.txt` (jangan tampil di layar). Setelah itu, tampilkan dari file tersebut hanya baris yang mengandung kata `TOTAL`.

✅ **Jawaban**

```bash
cd
curl -L -o partitioning.cpp bit.ly/partitioningcpp
g++ partitioning.cpp -o partitioning && ./partitioning > hasil_partisi.txt
grep "TOTAL" hasil_partisi.txt
```

Hasil milikmu:

```text
TOTAL FRAGMENTASI INTERNAL = 470 KB
TOTAL FRAGMENTASI INTERNAL = 0 KB (Bebas Pemborosan Dalam)
```

Isi lengkap `hasil_partisi.txt`:

```text
--- 1. SIMULASI FIXED PARTITIONING (Partisi Tetap 400 KB) ---
Proses 1 (150 KB) -> Partisi 1 (400 KB) | Frag. Internal: 250 KB
Proses 2 (380 KB) -> Partisi 2 (400 KB) | Frag. Internal: 20 KB
Proses 3 (200 KB) -> Partisi 3 (400 KB) | Frag. Internal: 200 KB
TOTAL FRAGMENTASI INTERNAL = 470 KB

--- 2. SIMULASI DYNAMIC PARTITIONING (Partisi Presisi Dinamis) ---
Proses 1 (150 KB) -> Partisi Dibuat Presisi 150 KB
Proses 2 (380 KB) -> Partisi Dibuat Presisi 380 KB
Proses 3 (200 KB) -> Partisi Dibuat Presisi 200 KB
Sisa Memori Kontigu Bebas = 470 KB
TOTAL FRAGMENTASI INTERNAL = 0 KB (Bebas Pemborosan Dalam)
```

💡 **Penjelasan:** pada **fixed**, tiap proses menempati satu partisi 400 KB utuh, jadi ruang yang terbuang di dalam partisi 250 + 20 + 200 = **470 KB** (fragmentasi internal) dan terkunci, tidak bisa dipakai proses lain. Pada **dynamic**, partisi dibuat sebesar kebutuhan proses sehingga fragmentasi internalnya **0 KB**, dan sisa **470 KB tetap satu blok kontigu** yang masih bebas. Jumlah ruang tak terpakai sama-sama 470 KB, tetapi di fixed ia terkunci dan di dynamic ia masih utuh. Akibatnya proses baru 450 KB **gagal di fixed** (lebih besar dari partisi 400 KB) tetapi **berhasil di dynamic**. Kelemahan dynamic: setelah proses datang dan pergi, ruang bebas terpecah jadi lubang kecil, yaitu fragmentasi **eksternal**.

| Aspek | Fixed | Dynamic |
|---|---|---|
| Ukuran partisi | tetap, ditentukan di awal | menyesuaikan ukuran proses |
| Jumlah partisi | tetap (membatasi jumlah proses) | berubah sesuai jumlah proses |
| Fragmentasi | **internal** | **eksternal** |
| Implementasi | sederhana | lebih rumit (mencatat daftar lubang bebas) |
| Proses lebih besar dari partisi | tidak bisa dimuat | bisa, selama ada blok bebas cukup |

⚠️ `>` mengalihkan hasil ke file sehingga tidak tampil di layar. Tulis `>` dan nama file dalam satu baris, jangan terpotong Enter. Kata `TOTAL` ditulis huruf besar sama seperti di keluaran program.

---

### Soal 5 — Algoritma penempatan memori

> 📝 **Soal:** Dari folder home, unduh `placement.cpp` dari `bit.ly/placementcpp`, kompilasi menjadi program `placement`, dan jalankan. Simpan seluruh keluarannya ke file `hasil_placement.txt`. Setelah itu, tampilkan dari file tersebut hanya baris yang mengandung kata `GAGAL`, lalu hitung jumlah baris yang mengandung kata itu dengan menyambung perintah pencarian ke perintah penghitung baris.

✅ **Jawaban**

```bash
cd
curl -L -o placement.cpp bit.ly/placementcpp
g++ placement.cpp -o placement && ./placement > hasil_placement.txt
grep "GAGAL" hasil_placement.txt
grep "GAGAL" hasil_placement.txt | wc -l
```

Hasil milikmu:

```text
  Proses 4 (426 KB) -> GAGAL (tidak ada blok >= 426 KB)
  Proses 4 (426 KB) -> GAGAL (tidak ada blok >= 426 KB)
  Proses 4 (426 KB) -> GAGAL (tidak ada blok >= 426 KB)
3
```

💡 **Penjelasan:** data awal lima blok bebas **100, 500, 200, 300, 600 KB** dan empat proses **212, 417, 112, 426 KB**. Tiga baris `GAGAL` semuanya **Proses 4 (426 KB)**, dari **First-Fit, Worst-Fit, dan Next-Fit**. Hanya **Best-Fit** yang berhasil menempatkan keempat proses.

| Algoritma | Cara kerja | P1 (212) | P2 (417) | P3 (112) | P4 (426) |
|---|---|:---:|:---:|:---:|:---:|
| **First-Fit** | hole pertama dari awal yang cukup | Blok 2 (sisa 288) | Blok 5 (sisa 183) | Blok 2 (sisa 176) | ❌ GAGAL |
| **Best-Fit** | hole dengan sisa terkecil yang cukup | Blok 4 (sisa 88) | Blok 2 (sisa 83) | Blok 3 (sisa 88) | ✅ Blok 5 (sisa 174) |
| **Worst-Fit** | hole terbesar | Blok 5 (sisa 388) | Blok 2 (sisa 83) | Blok 5 (sisa 276) | ❌ GAGAL |
| **Next-Fit** | lanjut dari posisi alokasi terakhir | Blok 2 (sisa 288) | Blok 5 (sisa 183) | Blok 5 (sisa 71) | ❌ GAGAL |

Kegagalan itu adalah **fragmentasi eksternal**: pada ketiga algoritma tadi total ruang bebas masih **959 KB**, jauh lebih besar dari 426 KB, tetapi terpecah di lima blok dan blok terbesarnya hanya **300 KB**. Best-Fit berhasil karena menaruh Proses 1 di blok 300 KB yang paling pas, Proses 2 di blok 500 KB, dan Proses 3 di blok 200 KB, sehingga **Blok 5 (600 KB) tetap utuh** untuk Proses 4. Worst-Fit justru memecah Blok 5. Beda First-Fit dan Next-Fit terlihat di Proses 3: First-Fit kembali ke Blok 2, Next-Fit melanjutkan dari posisi terakhir sehingga memilih Blok 5. Jadi tidak ada algoritma yang selalu terbaik, hasilnya bergantung urutan dan ukuran proses.

Cara membaca satu baris, misalnya `Proses 3 (112 KB) -> Blok 2 (tersedia 288 KB, sisa 176 KB)`: `Blok 2` nomor blok di DATA AWAL, `tersedia` ukuran blok saat diperiksa, `sisa` = tersedia − ukuran proses (288 − 112 = 176) yang diteruskan ke proses berikutnya, `GAGAL` berarti tidak ada blok yang cukup.

---

### Soal 6 — Kompaksi memori

> 📝 **Soal:** Dari folder home, unduh `compaction.cpp` dari `bit.ly/compactioncpp`, kompilasi menjadi program `compaction`, dan jalankan. Simpan seluruh keluarannya ke file `hasil_kompaksi.txt`. Setelah itu, kerjakan dua hal dari file tersebut: tampilkan hanya baris yang mengandung kata `Status` lengkap dengan nomor barisnya, lalu tampilkan tiga baris terakhir file itu.

✅ **Jawaban**

```bash
cd
curl -L -o compaction.cpp bit.ly/compactioncpp
g++ compaction.cpp -o compaction && ./compaction > hasil_kompaksi.txt
grep -n "Status" hasil_kompaksi.txt
tail -n 3 hasil_kompaksi.txt
```

Hasil milikmu:

```text
7:Status Alokasi Kontigu     : GAGAL! (Tidak ada satu blok yang cukup >= 180 KB)
13:Status Alokasi Kontigu     : BERHASIL! (Proses 180 KB berhasil dimuat)
```

```text
Status Alokasi Kontigu     : BERHASIL! (Proses 180 KB berhasil dimuat)
Sisa Memori Setelah Dimuat : 20 KB
=================================================
```

💡 **Penjelasan:** di baris 7 statusnya **GAGAL**: total memori bebas 200 KB sebenarnya cukup untuk proses 180 KB, tetapi terpecah menjadi blok 150 KB dan 50 KB (Blok 1 = 0), jadi tidak ada satu blok pun yang cukup besar. Itulah **fragmentasi eksternal**. Di baris 13 statusnya **BERHASIL** karena sudah dikompaksi: blok-blok bebas disatukan menjadi satu blok kontigu 200 KB, proses 180 KB dimuat, tersisa 20 KB. Total memori bebas **tidak berubah** (tetap 200 KB), karena kompaksi tidak menambah memori, hanya menata ulang letaknya.

| Kondisi | Blok bebas | Total bebas | Blok terbesar | Alokasi 180 KB |
|---|---|:---:|:---:|:---:|
| Sebelum kompaksi | 0, 150, 50 KB | 200 KB | 150 KB | ❌ GAGAL |
| Sesudah kompaksi | satu blok kontigu | 200 KB | 200 KB | ✅ BERHASIL |

Kompaksi tidak gratis: memindahkan proses berarti menyalin isi memorinya, proses harus dihentikan sementara, dan hanya mungkin kalau alamat proses bisa berubah saat berjalan (*execution-time binding*). Karena mahal, sistem modern lebih memilih **paging** (dibahas di Set 2).

⚠️ Flag `grep -n` menampilkan nomor baris (huruf **n**, bukan `-i`). Pada `tail -n 3`, angka 3 adalah jumlah baris terakhir.

---

### Soal 7 — Membuktikan ASLR

> 📝 **Soal:** Dari folder home, jalankan program `mmu` dua kali berturut-turut di layar utama (tanpa simbol latar belakang). Pada setiap percobaan, catat alamat virtual segmen Data, Heap, dan Stack yang dicetak, lalu tekan ENTER supaya programnya selesai sebelum kamu menjalankannya lagi.

✅ **Jawaban**

```bash
cd
./mmu
```

Catat tiga alamat, lalu tekan `ENTER`. Ulangi:

```bash
./mmu
```

Kalau `./mmu` tidak ditemukan, kompilasi ulang dengan `g++ mmu.cpp -o mmu`. Bentuk keluarannya:

```text
INSPEKSI MEMORI VIRTUAL PROSES (PID: ...)
Alamat Virtual Data Segment  : 0x...
Alamat Virtual Heap Segment  : 0x...
Alamat Virtual Stack Segment : 0x...
```

💡 **Penjelasan:** tiga alamat di percobaan kedua **berbeda** dengan percobaan pertama, karena **ASLR** (*Address Space Layout Randomization*) mengacak letak segmen setiap program dijalankan, supaya serangan sulit dilakukan. Polanya tetap: kode dan data di area bawah, heap di atasnya, pustaka bersama di tengah, stack di area atas. Alamat yang dicetak adalah alamat **virtual**, yang diterjemahkan MMU ke alamat fisik.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-6-set-2"></a>

## Latihan Set 2 · Memori 2 (11 soal)

Topik: translasi alamat paging dan segmentasi, swap, `vmstat`, simulasi page replacement, dan memicu swap sungguhan.

> 💡 **Catatan unduhan:** alamat `bit.ly` harus **persis** seperti di modul. Perhatikan `bit.ly/translation_cpp` (**dengan garis bawah**), sedangkan `bit.ly/replacementcpp` dan `bit.ly/memhogcpp` **tanpa** garis bawah.

### Soal 1 — Translasi alamat paging

> 📝 **Soal:** Ukuran page 4096 byte. Page 0 ke frame 5, page 1 ke frame 2, page 2 ke frame 9, page 3 ke frame 4. Alamat logis 13000, tentukan nomor page, offset, frame, dan alamat fisik.

✅ **Jawaban**

- Nomor page = 13000 ÷ 4096, hasil bagi bulat **3** (3 × 4096 = 12288, sedangkan 4 × 4096 = 16384 melebihi 13000).
- Offset = 13000 − 12288 = **712** byte.
- Frame dibaca dari page table, page 3 ke **frame 4**.
- Alamat fisik = (4 × 4096) + 712 = **17096**.

💡 Rumus: `page = alamat ÷ ukuran page` (bagi bulat), `offset = alamat mod ukuran page`, `fisik = frame × ukuran page + offset`.

⚠️ Urutannya page, offset, frame, alamat fisik. Frame **dibaca dari tabel**, bukan dihitung.

---

### Soal 2 — Membuat dan mengaktifkan swap file

> 📝 **Soal:** Buat swap file 512 MB bernama `/swapku`, atur izin hanya untuk root, jadikan area swap, aktifkan, lalu buktikan aktif.

✅ **Jawaban**

```bash
sudo fallocate -l 512M /swapku
sudo chmod 600 /swapku
sudo mkswap /swapku
sudo swapon /swapku
sudo swapon --show
sudo free -h
```

Hasil: `swapon --show` menampilkan `/swapku` ukuran `512M`, dan `free -h` baris Swap `511Mi`.

⚠️ Urutan wajib `fallocate`, `chmod 600`, `mkswap`, baru `swapon`. Kalau `swapon` dijalankan sebelum `mkswap`, muncul `read swap header failed`. Salin angka ukuran dari soal persis (512M, bukan 520M atau 1G). Opsi `-h` itu *human-readable*, bukan `-l`.

---

### Soal 3 — Mengecek dan mengubah swappiness

> 📝 **Soal:** Periksa swappiness, ubah sementara menjadi 20, lalu buktikan.

✅ **Jawaban**

```bash
sysctl vm.swappiness
sudo sysctl vm.swappiness=20
sysctl vm.swappiness
```

Hasil: awalnya `vm.swappiness = 60`, sesudah diubah `vm.swappiness = 20`.

⚠️ Perubahan ini **sementara** dan kembali ke 60 setelah reboot. Tulis tanpa spasi di sekitar tanda sama dengan.

---

### Soal 4 — Memantau swap dengan `vmstat`

> 📝 **Soal:** Tampilkan statistik swap sejak sistem menyala (hanya baris yang memuat "swap", tanpa membedakan huruf besar kecil), lalu pantau real-time satu baris per detik dan hentikan.

✅ **Jawaban**

```bash
vmstat -s | grep -i "swap"
vmstat 1
```

Hentikan dengan `Ctrl+C`. Hasil statistik: `total swap`, `used swap`, `free swap`, `pages swapped in`, `pages swapped out`.

💡 Kolom `si` adalah *swap-in* dan `so` *swap-out* (KB/detik). Nilai 0 artinya RAM masih lega, tidak ada page yang dipindahkan.

⚠️ Opsi `-s` untuk statistik, bukan `-n`.

---

### Soal 5 — Menghapus swap file

> 📝 **Soal:** Bersihkan `/swapku`: nonaktifkan, hapus berkas, lalu buktikan.

✅ **Jawaban**

```bash
sudo swapoff -v /swapku
sudo rm /swapku
sudo swapon --show
sudo free -h
ls -lh /swapku
```

Hasil: `swapon --show` kosong, baris Swap di `free -h` menunjukkan `0B`, dan `ls` menjawab `No such file or directory`.

⚠️ `swapoff` harus **sebelum** `rm`. Pembuktian memakai `swapon --show`, `free -h`, dan `ls`, bukan `ps aux`, karena swap bukan proses. Kalau sebelumnya menambah baris di `/etc/fstab`, hapus juga.

---

### Soal 6 — Cek ukuran page dan simulasi page replacement

> 📝 **Soal:** Tampilkan ukuran page, unduh `bit.ly/replacementcpp` sebagai `simulasi.cpp`, kompilasi jadi `simulasi`, jalankan dalam satu baris, sebutkan total fault FIFO dan LRU.

✅ **Jawaban**

```bash
getconf PAGESIZE
curl -L -o simulasi.cpp bit.ly/replacementcpp
head simulasi.cpp
g++ simulasi.cpp -o simulasi && ./simulasi
```

Hasil: `4096`, lalu `Total Page Faults (FIFO) = 9` dan `Total Page Faults (LRU) = 8`.

⚠️ Nama setelah `-o` untuk `curl` adalah nama berkas hasil, urutannya nama dulu baru alamat. Jangan pakai `>` bersama `-o`, karena membuat berkas kosong dan `g++` menolak dengan `undefined reference to main`. Cek isi dengan `head` sebelum kompilasi.

---

### Soal 7 — Simulasi translasi paging dan segmentasi

> 📝 **Soal:** Unduh kode translasi dari modul sebagai `terjemah.cpp`, kompilasi jadi `terjemah`, jalankan dalam satu baris, sebutkan hasil bagian A dan B.

✅ **Jawaban**

```bash
curl -L -o terjemah.cpp bit.ly/translation_cpp
head terjemah.cpp
g++ terjemah.cpp -o terjemah && ./terjemah
```

Hasil bagian A (paging): alamat logis 9500, Page 2, Offset 1308 byte, Frame 8, alamat fisik 34076. Bagian B (segmentasi): Segmen 1 Offset 250, Valid Access, alamat fisik 6550.

⚠️ Alamat unduhannya `bit.ly/translation_cpp` dengan garis bawah, beda dari alamat lain di modul yang tanpa garis bawah. Salin dari modul, jangan mengetik dari ingatan. Kalau isi berkas `404: Not Found`, berarti alamat salah.

---

### Soal 8 — Memicu swap-out dan swap-in sungguhan dengan `memhog`

> 📝 **Soal:** Pastikan swap aktif (buat `/swapku` 1G). Unduh `memhog` dari modul sebagai `hog.cpp`, kompilasi jadi `hog`. Jalankan `hog` meminta 200 MB dengan jatah RAM 80M dan swap 200M, sambil memantau swap dalam satu terminal.

✅ **Jawaban**

```bash
sudo fallocate -l 1G /swapku
sudo chmod 600 /swapku
sudo mkswap /swapku
sudo swapon /swapku
curl -L -o hog.cpp bit.ly/memhogcpp
g++ hog.cpp -o hog
sudo -v
```

Lalu perintah utamanya:

```bash
sudo systemd-run --scope -p MemoryMax=80M -p MemorySwapMax=200M ./hog 200 & \
vmstat 1 8 & \
sleep 8 && swapon --show && free -h && \
vmstat 1 10 && \
wait
```

Hasil yang diharapkan: program meminta 200 MB tapi RAM-nya dibatasi 80 MB, jadi sekitar 120 MB dipaksa ke swap. Di fase pertama kolom `so` pada `vmstat` naik dan `USED` di `swapon --show` naik dari `0B`. Di fase kedua (program membaca ulang semua page) kolom `si` naik karena page dimuat kembali dari disk. Setelah itu bersihkan dengan `sudo swapoff /swapku` lalu `sudo rm /swapku`.

⚠️ Setelah `&` tidak boleh ada `&&`. `sudo` di background butuh password, jadi jalankan dulu satu perintah `sudo` (misalnya `sudo -v`) sebelum perintah panjang, kalau tidak prosesnya `Stopped` dan hasilnya kosong. `swapon --show` ditulis tanpa nama berkas. Nama setelah `-o` menentukan nama program (`hog`), kalau salah nama maka `./hog` tidak ditemukan. Alamat unduhan `memhogcpp` tanpa garis bawah.

---

### Soal 9 — Translasi segmentasi dan cek limit

> 📝 **Soal:** Segment table: segmen 0 base 1000 limit 400, segmen 1 base 6300 limit 400, segmen 2 base 3000 limit 200. Tentukan hasil alamat logis (segmen 1, offset 250) dan (segmen 2, offset 250).

✅ **Jawaban**

- **Segmen 1, offset 250:** 250 lebih kecil dari limit 400, maka *Valid Access*. Alamat fisik = 6300 + 250 = **6550**.
- **Segmen 2, offset 250:** 250 tidak lebih kecil dari limit 200, maka akses **ditolak lewat trap**. Alamat fisik tidak dihitung.

💡 Pada segmentasi **cek limit dulu**, baru hitung `base + offset`. Pada paging tidak perlu cek limit karena offset pasti muat di satu page.

---

### Soal 10 — Simulasi FIFO vs LRU

> 📝 **Soal:** Reference string 7, 0, 1, 2, 0, 3, 0, 4, 2, 3 dengan 3 frame. Hitung total page fault FIFO dan LRU.

✅ **Jawaban**

- **FIFO:** 7 fault, 0 fault, 1 fault, 2 fault (korban 7), 0 hit, 3 fault (korban 0), 0 fault (korban 1), 4 fault (korban 2), 2 fault (korban 3), 3 fault (korban 0). Total **9 fault**.
- **LRU:** 7 fault, 0 fault, 1 fault, 2 fault (korban 7), 0 hit, 3 fault (korban 1), 0 hit, 4 fault (korban 2), 2 fault (korban 3), 3 fault (korban 0). Total **8 fault**.

💡 Titik pisah di akses ke-6, saat page 3 diminta. FIFO membuang page 0 (paling awal masuk) padahal baru dipakai di akses ke-5, sedangkan LRU membuang page 1 (paling lama tidak dipakai). Hasilnya cocok dengan program: FIFO 9 dan LRU 8.

---

### Soal 11 — Belady's anomaly dan istilah penting

> 📝 **Soal:** Jelaskan Belady's anomaly beserta contoh angkanya, dan bedakan page fault dengan SIGSEGV serta apa itu thrashing.

✅ **Jawaban**

- **Belady's anomaly** adalah keanehan di FIFO: jumlah frame ditambah tetapi jumlah page fault justru naik. Contoh string 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5: FIFO menghasilkan **9 fault pada 3 frame** tetapi **10 fault pada 4 frame**. LRU tidak mengalaminya (10 fault pada 3 frame, turun jadi 8 pada 4 frame) karena LRU termasuk *stack algorithm*.
- **Page fault** adalah kejadian normal saat proses mengakses page yang belum ada di RAM, lalu kernel memuatnya dari disk. **SIGSEGV** adalah akses ilegal ke alamat yang bukan haknya, dan prosesnya dihentikan.
- **Thrashing** adalah kondisi sistem terlalu sering memindahkan page antara RAM dan disk sampai hampir tidak sempat bekerja, sehingga kinerja turun drastis.

💡 Pada OS sungguhan, LRU murni terlalu mahal dicatat, jadi dipakai pendekatannya yaitu *Clock / second chance*.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="contekan-modul-6"></a>

## 📌 Contekan Modul 6

### Konsep inti

| Konsep | Ingat ini |
|---|---|
| **Hirarki memori** | register (<1 ns) → cache (1-10 ns) → RAM (~50-100 ns) → SSD/HDD (µs-ms). Makin dekat CPU: cepat, kecil, mahal |
| **RAM vs disk** | RAM *volatile*, disk *non-volatile*. RAM tidak lebih lambat dari disk |
| **Alamat virtual → fisik** | diterjemahkan **MMU** (pakai page table + TLB) |
| **Segmen** | Code `r-x`, Data `rw-`, Heap `rw-` (naik), Stack `rw-` (turun) |
| **ASLR** | letak segmen diacak, alamat berubah tiap dijalankan |
| **Base / Limit** | sah jika **L < Limit**, alamat fisik = **Base + L** (contoh: Base 300.000, Limit 120.000, L 50.000 → 350.000, L 130.000 → TRAP) |
| **Segfault** | trap → kernel kirim **SIGSEGV (11)** → exit code **139 = 128 + 11** |
| **Page fault** | bisa normal (kernel menyediakan page, program tak sadar) atau ilegal (SIGSEGV). *Segfault = page fault yang tidak bisa diselesaikan kernel* |
| **Fragmentasi internal** | ruang terbuang **di dalam** partisi (fixed: 250+20+200 = 470 KB) |
| **Fragmentasi eksternal** | ruang bebas terpecah **di luar** partisi (bebas 959 KB tapi blok terbesar 300 KB) |
| **Kompaksi** | geser proses, hole menyatu (150+50 → 200 KB). Total bebas tidak berubah, tapi mahal |
| **Paging** | `page = alamat ÷ ukuran page`, `offset = alamat mod ukuran page`, `fisik = frame × ukuran page + offset`. Frame dibaca dari page table |
| **Segmentasi** | cek **limit dulu**, baru `base + offset`. Offset ≥ limit → trap |
| **FIFO vs LRU** | FIFO buang yang paling awal masuk, LRU buang yang paling lama tidak dipakai. Contoh 7,0,1,2,0,3,0,4,2,3 (3 frame): FIFO 9, LRU 8 |
| **Belady's anomaly** | hanya di FIFO: frame bertambah, fault naik (9 → 10). LRU kebal (*stack algorithm*) |
| **Thrashing** | terlalu sering bolak-balik page RAM ↔ disk, kinerja anjlok |

### Perintah praktik

| Perintah | Fungsi |
|---|---|
| `dd if=/dev/zero of=... bs=1M count=N status=progress` | uji kecepatan tulis (`oflag=direct` untuk disk) |
| `curl -L -o nama.cpp bit.ly/...` | unduh kode (urutan: `-L -o nama alamat`) |
| `g++ x.cpp -o x && ./x` | kompilasi dan jalankan |
| `pmap -x PID` | peta memori proses (Address, Kbytes, RSS, Dirty, Mode, Mapping) |
| `sudo dmesg \| tail -n 3` | tiga baris terakhir catatan kernel |
| `echo $?` | exit code (139 untuk segfault) |
| `kill -9 PID` | bunuh paksa, termasuk proses berstatus `T` |
| `getconf PAGESIZE` | ukuran page (4096) |
| `sudo fallocate -l 512M /swapku` → `chmod 600` → `mkswap` → `swapon` | buat dan aktifkan swap file (**urutan wajib**) |
| `swapon --show` / `free -h` | bukti swap aktif |
| `sudo swapoff -v /swapku` lalu `rm /swapku` | matikan swap, baru hapus berkas |
| `sysctl vm.swappiness` / `sudo sysctl vm.swappiness=20` | lihat / ubah (sementara) swappiness, default 60 |
| `vmstat -s \| grep -i "swap"` | statistik swap sejak menyala |
| `vmstat 1` | pantau tiap detik. `si` = swap-in, `so` = swap-out |
| `sudo -v` | isi cache password `sudo` sebelum menjalankan `sudo` di background |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-7"></a>

# 💾 Modul 7 · Manajemen Penyimpanan

5 soal latihan, dikerjakan di Ubuntu VM (disk VirtualBox). Soal 5 (disk scheduling) dijawab langsung dengan Python.

### Teori inti

| Konsep | Ingat ini |
|---|---|
| **4 lapisan** | Aplikasi, Logical File System, Virtual File System (VFS), Physical File System |
| **Alur disk** | disk → partisi (`fdisk`) → format (`mkfs.ext4`) → mount → pakai → unmount (`umount`). Mount **tidak permanen** kecuali ditulis di `/etc/fstab` |
| **`df` vs `du`** | `df` mengukur dari sisi **filesystem**, `du` dari sisi **berkas** |
| **Inode** | nama berkas **bukan** bagian inode |
| **Hard link** | inode **sama**, tetap hidup saat asli dihapus |
| **Soft link** | inode **beda**, jadi *broken link* saat asli dihapus |
| **Buffering / Caching / Spooling** | penampung / salinan cepat / antrean (misalnya printer) |
| **Disk scheduling** | FCFS, SSTF (risiko starvation), SCAN (seperti lift), C-SCAN (lompat ke awal, tunggu merata) |

---

### Soal 1 — Mengenal perangkat

> 📝 **Soal:** Tampilkan daftar perangkat blok beserta filesystem-nya, tabel partisi, dan UUID. Periksa jenis berkas `/dev/sda`, `/dev/tty`, dan `/dev/urandom`, lalu cek apakah `sda` berupa HDD atau SSD.

✅ **Jawaban**

```bash
lsblk
lsblk -f
sudo fdisk -l
sudo blkid
ls -l /dev/sda /dev/tty /dev/urandom
cat /sys/block/sda/queue/rotational
```

Hasil: `/dev/sda` = **b** (block), `/dev/tty` dan `/dev/urandom` = **c** (character). Rotational = `1` (terbaca HDD, karena disk VirtualBox).

💡 Huruf pertama pada `ls -l`: `b` perangkat blok (disk), `c` perangkat karakter (terminal, generator acak). `rotational` `1` = HDD, `0` = SSD.

⚠️ Perhatikan ejaan jalur: `cat /sys/block/sda/queue/rotational`.

📌 Skor: 15/15.

---

### Soal 2 — Mount, chown, `tune2fs`, umount

> 📝 **Soal:** Buat titik mount `/mnt/latihan`, mount `/dev/sdb1` ke sana, buktikan dengan `df` dan `findmnt`. Ubah pemilik titik mount ke user saat ini, tulis `Latihan modul tujuh` ke `catatan.txt` di dalamnya, lalu tampilkan. Lihat Block size, Inode count, dan features filesystem dengan `tune2fs`, kemudian unmount.

✅ **Jawaban**

```bash
sudo mkdir -p /mnt/latihan
sudo mount /dev/sdb1 /mnt/latihan
df -h /mnt/latihan
findmnt /mnt/latihan
sudo chown $USER:$USER /mnt/latihan
echo "Latihan modul tujuh" > /mnt/latihan/catatan.txt
cat /mnt/latihan/catatan.txt
sudo tune2fs -l /dev/sdb1 | grep -E "Block size|Inode count|features"
sudo umount /mnt/latihan
```

Hasil: Block size **4096**, Inode count **131072**, features antara lain *journaling* dan *extents*.

⚠️ `umount` ditulis dengan **satu n**. Perhatikan spasi pada pola `"Block size"`.

📌 Skor: 20/20.

---

### Soal 3 — Inode, hard link, soft link

> 📝 **Soal:** Mount `/dev/sdb1` lagi, masuk ke `/mnt/latihan`, buat folder `arsip` berisi `laporan.txt` (isi `versi pertama`). Buat hard link `keras.txt` dan soft link `lunak.txt` ke `laporan.txt`, tampilkan nomor inode-nya, hapus file asli, lalu cek isi kedua link.

✅ **Jawaban**

```bash
sudo mount /dev/sdb1 /mnt/latihan
cd /mnt/latihan
mkdir arsip
echo "versi pertama" > arsip/laporan.txt
ln arsip/laporan.txt arsip/keras.txt
ln -s arsip/laporan.txt arsip/lunak.txt
ls -li arsip
rm arsip/laporan.txt
cat arsip/keras.txt
cat arsip/lunak.txt
```

Hasil: inode `keras.txt` = `laporan.txt` = **19**, `lunak.txt` = **20**. Setelah asli dihapus: `keras.txt` masih berisi `versi pertama`, `lunak.txt` **error** (broken link).

💡 Hard link berbagi inode yang sama sehingga data tetap ada selama masih ada satu nama. Soft link hanya menyimpan **jalur** ke berkas asli, jadi putus saat asli hilang. `ln` tanpa flag = hard link, `ln -s` = soft link.

📌 Skor: 20/20.

---

### Soal 4 — Ruang disk, buffering, `sync`

> 📝 **Soal:** Bandingkan ruang disk sebelum dan sesudah membuat berkas 50M di `/mnt/latihan` (`df` dan `du`), lihat tipe filesystem dan pemakaian inode, lalu tunjukkan efek *buffering*: tulis 200 MiB dengan `dd`, amati `Dirty` dan `Writeback` di `/proc/meminfo` sebelum dan sesudah `sync`, dan bandingkan waktu tulis dengan `conv=fsync`. Bersihkan berkas ujinya.

✅ **Jawaban**

```bash
cd ~
df -h /mnt/latihan
fallocate -l 50M /mnt/latihan/blok.bin
df -h /mnt/latihan
sudo du -sh /mnt/latihan
df -hT
df -i /mnt/latihan
grep -E "^(Dirty|Writeback):" /proc/meminfo
time dd if=/dev/zero of=/mnt/latihan/uji.img bs=1M count=200 status=none
grep -E "^(Dirty|Writeback):" /proc/meminfo
sync
grep -E "^(Dirty|Writeback):" /proc/meminfo
rm /mnt/latihan/uji.img
time dd if=/dev/zero of=/mnt/latihan/uji.img bs=1M count=200 conv=fsync status=none
rm /mnt/latihan/uji.img /mnt/latihan/blok.bin
df -h /mnt/latihan
```

💡 `Dirty` **naik** setelah `dd` biasa (data masih di RAM), **turun** setelah `sync` (dipaksa ke disk). `conv=fsync` menunggu data benar-benar tertulis, jadi biasanya **lebih lambat**.

⚠️ `count=200M` salah (membuat disk penuh), yang benar `count=200`. Total = `bs` × `count`.

📌 Skor: 18/20 (diselesaikan dengan jawaban langsung).

---

### Soal 5 — Disk scheduling (`kepala.py`)

> 📝 **Soal:** Jalankan `kepala.py` yang membandingkan FCFS dan SSTF dengan posisi awal kepala 50 dan antrian `[95, 180, 34, 119, 11, 123, 62, 64]`. Salin menjadi `kepala2.py`, ubah `posisi_awal = 50` menjadi `100`, lalu bandingkan hasilnya dan analisis.

✅ **Jawaban**

```bash
micro kepala.py
cat kepala.py
python3 kepala.py
cp kepala.py kepala2.py
micro kepala2.py      # ubah posisi_awal = 50 menjadi 100
cat kepala2.py
python3 kepala2.py
```

Hasil dengan `posisi_awal = 50`:

```text
FCFS: 50 -> 95 -> 180 -> 34 -> 119 -> 11 -> 123 -> 62 -> 64
  Total: 644
SSTF: 50 -> 62 -> 64 -> 34 -> 11 -> 95 -> 119 -> 123 -> 180
  Total: 236
```

Hasil dengan `posisi_awal = 100`:

```text
FCFS: 100 -> 95 -> 180 -> 34 -> 119 -> 11 -> 123 -> 62 -> 64
  Total: 604
SSTF: 100 -> 95 -> 119 -> 123 -> 180 -> 64 -> 62 -> 34 -> 11
  Total: 259
```

💡 **Analisis:** total = jumlah **selisih mutlak** antar silinder berurutan. SSTF jauh lebih kecil dari FCFS pada kedua kasus karena selalu melayani yang **terdekat**. Kelemahan SSTF: permintaan yang jauh bisa **starvation**. Posisi awal berbeda mengubah total kedua algoritma (FCFS 644 jadi 604, SSTF 236 jadi 259), jadi SSTF tidak selalu turun saat posisi awal berubah, tetapi tetap lebih kecil dari FCFS.

### Ringkasan skor Modul 7

| Soal | Skor |
|---|:---:|
| 1 | 15/15 |
| 2 | 20/20 |
| 3 | 20/20 |
| 4 | 18/20 |
| 5 | dijawab langsung |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

## 📌 Contekan Modul 7

| Perintah / konsep | Fungsi |
|---|---|
| `lsblk` / `lsblk -f` | daftar perangkat blok / plus filesystem |
| `sudo fdisk -l` / `sudo blkid` | tabel partisi / UUID |
| `ls -l /dev/...` | huruf pertama: `b` block, `c` character |
| `cat /sys/block/sda/queue/rotational` | `1` HDD, `0` SSD |
| `sudo mount /dev/sdb1 /mnt/latihan` | pasang filesystem (tidak permanen tanpa `/etc/fstab`) |
| `df -h` / `df -hT` / `df -i` | ruang disk / plus tipe / pemakaian inode |
| `du -sh folder` | ukuran folder |
| `findmnt` | lihat titik mount |
| `sudo tune2fs -l /dev/sdb1` | info ext4 (Block size, Inode count, features) |
| `sudo umount /mnt/latihan` | lepas mount (**satu n**) |
| `ln a b` / `ln -s a b` | hard link / soft link. `ls -li` untuk melihat inode |
| `fallocate -l 50M file` | buat berkas ukuran tertentu |
| `dd ... count=200` | `bs` × `count`, bukan `200M` |
| `sync` / `conv=fsync` | paksa data dari RAM ke disk |
| FCFS / SSTF / SCAN / C-SCAN | urut datang / terdekat (risiko starvation) / seperti lift / lompat ke awal |

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="modul-8"></a>

# 🛡️ Modul 8 · Keamanan Komputer

> ℹ️ Berikut ringkasan konsep, 8 soal latihan beserta jawabannya, lalu contekan command kunci untuk dihafal.

### Konsep inti

| Konsep | Ingat ini |
|---|---|
| **CIA Triad** | **C**onfidentiality (hanya yang berhak boleh membaca), **I**ntegrity (data tidak diubah diam-diam), **A**vailability (data tetap bisa dipakai saat dibutuhkan) |
| **AAA** | **A**uthentication (kamu siapa), **A**uthorization (boleh apa), **A**ccounting (apa yang sudah dilakukan) |
| **DAC** | pemilik file yang menentukan akses (rwx, ACL, sudo). Root bisa melewatinya |
| **MAC** | aturan per program yang berlaku bahkan untuk root (**AppArmor** di Ubuntu, **SELinux** di Red Hat) |
| **Least privilege** | setiap user dan program hanya diberi hak seminimal yang cukup |

<a id="modul-8-latihan"></a>

## Latihan (8 soal)

Dikerjakan di akun `magang`. Memakai user uji **`tamu`** supaya akun `magang` tidak ikut terkunci atau berubah.

> ⚠️ **Jangan** mengunci akun `magang` atau mengubah SSH dan firewall tanpa aturan `allow` SSH. Itu bisa mengunci dirimu sendiri dari VM.

### Soal 1 — Kunci dan buka akun

> 📝 **Soal:** Buat user `tamu` lengkap dengan home dan password. Tampilkan status akunnya, kunci akun itu, lalu tampilkan status dan baris `tamu` di `/etc/shadow` untuk membuktikan terkunci. Terakhir buka kuncinya dan tampilkan statusnya lagi.

✅ **Jawaban**

```bash
sudo useradd -m tamu
sudo passwd tamu
sudo passwd -S tamu
sudo passwd -l tamu
sudo passwd -S tamu
sudo grep tamu /etc/shadow
sudo passwd -u tamu
sudo passwd -S tamu
```

Hasil status berurutan: `tamu P ...` (aktif), `tamu L ...` (terkunci), lalu `tamu P ...` lagi. Pada `/etc/shadow`, hash password diawali tanda `!` (contoh `tamu:!$y$...`).

💡 `passwd -l` tidak menghapus password, hanya menambah `!` di depan hash sehingga password tidak cocok lagi. `-u` menghapus tanda itu. `-S` (besar) menampilkan status, `-l` dan `-u` (kecil) mengubahnya.

⚠️ Akun tanpa password tidak bisa dibuka kuncinya dengan `-u`, jadi isi password dulu.

---

### Soal 2 — Aturan sudo minimal (*least privilege*)

> 📝 **Soal:** Beri user `tamu` hak sudo yang **hanya** boleh menjalankan `/usr/bin/apt update`, lewat file aturan khusus `/etc/sudoers.d/tamu` yang diperiksa sintaksnya. Buktikan dengan melihat hak sudo `tamu`, lalu hapus aturannya.

✅ **Jawaban**

```bash
sudo visudo -f /etc/sudoers.d/tamu
```

Isi file (satu baris):

```text
tamu ALL=(ALL) /usr/bin/apt update
```

Simpan lalu:

```bash
sudo -l -U tamu
sudo rm /etc/sudoers.d/tamu
sudo -l -U tamu
```

Hasil `sudo -l -U tamu` pertama memuat `(ALL) /usr/bin/apt update`. Setelah dihapus, hasilnya `User tamu is not allowed to run sudo`.

💡 Prinsip *least privilege*: hanya diberi hak seminimal yang cukup, bukan `ALL`. `visudo -f` memeriksa sintaks sebelum menyimpan, sehingga file yang salah tidak merusak sudo.

⚠️ Kalau `visudo` bertanya "What now?", tekan `e` untuk mengedit ulang, bukan `Q`.

---

### Soal 3 — ACL

> 📝 **Soal:** Buat `/tmp/laporan.txt` berisi `data rahasia` yang hanya bisa dibaca pemiliknya. Beri user `tamu` hak baca **saja** lewat ACL, tampilkan ACL-nya, buktikan `tamu` bisa membaca, lalu cabut entri ACL `tamu` dan buktikan `tamu` ditolak lagi.

✅ **Jawaban**

```bash
echo "data rahasia" > /tmp/laporan.txt
chmod 600 /tmp/laporan.txt
setfacl -m u:tamu:r /tmp/laporan.txt
getfacl /tmp/laporan.txt
sudo -u tamu cat /tmp/laporan.txt
setfacl -x u:tamu /tmp/laporan.txt
sudo -u tamu cat /tmp/laporan.txt
```

Hasil: `getfacl` memuat baris `user:tamu:r--`, `cat` pertama menampilkan `data rahasia`, dan `cat` kedua `Permission denied`.

💡 ACL menambah hak untuk user tertentu tanpa mengubah pemilik atau grup (ini contoh **DAC**: pemilik file yang menentukan akses). Pada `ls -l`, file ber-ACL ditandai `+` di akhir izin. `-m` mengubah/menambah entri, `-x` menghapus entri.

---

### Soal 4 — Mode AppArmor

> 📝 **Soal:** Tampilkan status AppArmor. Untuk program contoh modul `/usr/local/bin/kucing` (profilnya sudah dibuat di praktik modul), ubah ke mode *complain*, buktikan, kembalikan ke mode *enforce*, buktikan, lalu muat ulang profilnya.

✅ **Jawaban**

```bash
sudo aa-status
sudo aa-complain /usr/local/bin/kucing
sudo aa-status | grep kucing
sudo aa-enforce /usr/local/bin/kucing
sudo aa-status | grep kucing
sudo apparmor_parser -r /etc/apparmor.d/usr.local.bin.kucing
```

Setelah `aa-complain`, `kucing` muncul di daftar profil mode *complain*. Setelah `aa-enforce`, pindah ke daftar profil mode *enforce*.

💡 AppArmor adalah **MAC**: aturan per program yang berlaku bahkan untuk root. *Complain* hanya mencatat pelanggaran (untuk menguji profil), *enforce* benar-benar menolaknya.

---

### Soal 5 — Log (*Accounting*)

> 📝 **Soal:** Jalankan satu perintah `sudo` apa saja, lalu tampilkan 20 log terakhir penggunaan sudo dan 20 log terakhir service SSH tanpa pager.

✅ **Jawaban**

```bash
sudo whoami
sudo journalctl -t sudo -n 20 --no-pager
sudo journalctl -u ssh -n 20 --no-pager
```

Hasil pertama memuat baris dengan `COMMAND=/usr/bin/whoami` milik `magang`. Hasil kedua memuat catatan login SSH (`Accepted password for ...`).

💡 Ini contoh **Accounting** pada AAA: mencatat siapa melakukan apa. `-t` memilih berdasarkan tag, `-u` berdasarkan service, `-n 20` 20 baris terakhir, `--no-pager` mencetak langsung tanpa `less`.

---

### Soal 6 — Firewall `ufw`

> 📝 **Soal:** Atur firewall: tutup semua koneksi masuk secara default, izinkan SSH (port 22/tcp), aktifkan firewall, lalu tampilkan status lengkapnya.

✅ **Jawaban**

```bash
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw enable
sudo ufw status verbose
```

Hasil: `Status: active`, `Default: deny (incoming)`, dan aturan `22/tcp ALLOW IN Anywhere`.

💡 Urutannya penting: aturan SSH harus ada **sebelum** `enable`, supaya firewall tidak memutus sesi SSH-mu sendiri.

⚠️ Jangan menjalankan `ufw enable` sebelum `ufw allow` port SSH.

---

### Soal 7 — SSH hardening

> 📝 **Soal:** Cadangkan `/etc/ssh/sshd_config`, lalu tolak login SSH sebagai root (`PermitRootLogin no`). Periksa sintaksnya, terapkan perubahan, dan buktikan nilainya aktif tanpa menutup sesi yang sedang berjalan.

✅ **Jawaban**

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
sudo nano /etc/ssh/sshd_config
```

Ubah (atau tambahkan) baris:

```text
PermitRootLogin no
```

Lalu:

```bash
sudo sshd -t
sudo systemctl restart ssh
sudo sshd -T | grep -i permitrootlogin
```

`sshd -t` tidak menampilkan apa pun (berarti sintaks aman), dan `sshd -T` menampilkan `permitrootlogin no`.

💡 Mengganti `Port` ke port lain hanya lapisan tambahan, bukan pengaman utama. Kalau port diganti, buka dulu di `ufw` (`sudo ufw allow <port>/tcp`) dan uji login lewat **terminal baru** sebelum menutup sesi lama. Di Ubuntu 24.04 perubahan port bisa memerlukan `ssh.socket` (`systemctl daemon-reload`).

⚠️ Jangan tutup sesi aktif sebelum login lewat konfigurasi baru terbukti berhasil. Jika ada masalah, kembalikan dengan `sudo cp /etc/ssh/sshd_config.bak /etc/ssh/sshd_config`.

---

### Soal 8 — Konsep (penjelasan)

> 📝 **Soal:** (a) Sebutkan tiga komponen CIA Triad dan beri satu contoh pelanggaran untuk masing-masing. (b) Sebutkan komponen AAA dan perintah di soal sebelumnya yang mewakili masing-masing. (c) Bedakan DAC dan MAC. (d) Apa itu *least privilege* dan di soal mana kamu menerapkannya?

✅ **Jawaban**

**(a)** *Confidentiality*: file rahasia terbaca orang yang tidak berhak (misalnya ACL terlalu longgar). *Integrity*: data diubah diam-diam (misalnya file dimodifikasi tanpa jejak). *Availability*: data tidak bisa dipakai saat dibutuhkan (misalnya akun terkunci atau firewall memutus SSH).

**(b)** *Authentication* (kamu siapa): login dengan password, status akun `passwd -S`. *Authorization* (boleh apa): izin file, ACL, aturan `sudoers`. *Accounting* (apa yang sudah dilakukan): `journalctl`.

**(c)** **DAC**: pemilik file yang menentukan akses (rwx, ACL, sudo), dan root bisa melewatinya. **MAC**: aturan per program yang dipaksakan sistem, berlaku bahkan untuk root (AppArmor di Ubuntu, SELinux di Red Hat).

**(d)** *Least privilege* = setiap user dan program hanya diberi hak seminimal yang cukup. Diterapkan di Soal 2 (sudo hanya untuk `apt update`) dan Soal 3 (ACL hanya hak baca).

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="contekan-modul-8"></a>

## 📌 Contekan Modul 8

### Command kunci

**Akun dan sudo**

| Perintah | Fungsi |
|---|---|
| `sudo passwd -S magang` | status akun (`P` aktif, `L` terkunci) |
| `sudo passwd -l magang` | kunci akun (menambah `!` di depan hash di `/etc/shadow`) |
| `sudo passwd -u magang` | buka kunci akun |
| `sudo visudo -f /etc/sudoers.d/magang` | buat aturan sudo khusus user dengan pengecekan sintaks |
| `sudo -l -U magang` | lihat hak sudo milik user |

**ACL dan AppArmor**

| Perintah | Fungsi |
|---|---|
| `setfacl -m u:magang:r laporan.txt` | beri user `magang` hak baca lewat ACL |
| `getfacl laporan.txt` | lihat isi ACL |
| `setfacl -x u:magang laporan.txt` | hapus entri ACL user `magang` |
| `sudo aa-status` | status AppArmor dan profil aktif |
| `sudo apparmor_parser -r /etc/apparmor.d/usr.local.bin.kucing` | muat ulang profil |
| `sudo aa-complain /usr/local/bin/kucing` | mode *complain* (pelanggaran dicatat, tidak ditolak) |
| `sudo aa-enforce /usr/local/bin/kucing` | mode *enforce* (pelanggaran ditolak) |

**Log, firewall, dan SSH**

| Perintah | Fungsi |
|---|---|
| `sudo journalctl -t sudo -n 20 --no-pager` | 20 log terakhir penggunaan sudo |
| `sudo journalctl -u ssh -n 20 --no-pager` | log service SSH |
| `sudo ufw default deny incoming` | tutup semua koneksi masuk |
| `sudo ufw allow 22/tcp` | izinkan SSH **sebelum** firewall diaktifkan |
| `sudo ufw enable` | aktifkan firewall |
| `sudo ufw status verbose` | status dan aturan firewall |
| `sudo sshd -t` | cek sintaks `sshd_config` (tidak ada output berarti aman) |
| `sudo systemctl restart ssh` | terapkan perubahan SSH (Ubuntu 24.04 memakai `ssh.socket` setelah `daemon-reload`) |

**Pengaturan SSH hardening** di `/etc/ssh/sshd_config`: ubah `Port` ke port lain (lapisan tambahan saja) dan `PermitRootLogin no`.

⚠️ Buka port SSH baru di `ufw` **sebelum** restart SSH, dan jangan tutup sesi aktif sebelum login lewat port baru berhasil. Saat memakai `visudo`, kalau muncul "What now?", tekan `e` untuk mengedit ulang, bukan `Q`.

<p align="right"><a href="#top">⬆️ kembali ke atas</a></p>

---

<a id="kesalahan"></a>

# ⚠️ Kesalahan Paling Sering Terulang

### Modul 2

| ❌ Salah | ✅ Benar |
|---|---|
| `find . -name *.txt` | `find . -name "*.txt"` (pakai tanda kutip) |
| `usermod -aG user grup` | `usermod -aG` **grup dulu**, baru user |
| `usermod -l ren/ray ...` | nama baru tanpa `/`, pola `-l baru -d /home/baru -m lama` |
| `chmod 421 file` (menjumlah salah posisi) | jumlahkan **per kelompok** (owner, group, others): `750`, `640` |
| `chown -M ...` | flag rekursif `chown -R`, format `user:grup`, urutan flag, pemilik, target |
| `chmod` pada file milik user lain tanpa `sudo` | tambah `sudo` (`Operation not permitted`) |
| `passwd -s` / `-P` / `-U` | `-S` besar untuk status, `-l` dan `-u` kecil |
| `passwd -u` sesudah mengunci | jangan dijalankan jika akhir soal meminta akun terkunci |
| `ls -d kirana` untuk bukti home | `ls -l /home` |

### Modul 3

| ❌ Salah | ✅ Benar |
|---|---|
| `sapa.sh` di folder sendiri | `./sapa.sh` (atau daftarkan foldernya ke PATH) |
| `chmod u+w` agar bisa dijalankan | izin eksekusi itu `x` (`chmod u+x`) |
| `export PATH="$PATH:/home/latihan_modul3"` | alamat **lengkap**: `/home/magang/latihan_modul3` |
| `export PATH="/home/magang/latihan_os"` (tanpa `$PATH:`) | selalu tulis `$PATH:` di dalam kutip, kalau tidak PATH tertimpa dan semua perintah hilang |
| `export PATH` di terminal untuk "permanen" | tulis di `~/.bashrc`, lalu `source ~/.bashrc` |
| `echo halo.py` untuk melihat PATH | `echo $PATH` |
| shebang tidak di baris 1, atau lupa `chmod` | shebang **baris pertama**, lalu `chmod u+x` |
| `ps aux \| 3198 sleep` | setelah pipe harus **nama perintah** (`grep`) |
| `cat script.sh > hasil.txt` untuk menyimpan hasil script | `script.sh > hasil.txt` (yang di kiri `>` harus perintah yang **menjalankan** script) |
| `cat file_hilang.txt > log.txt` untuk menyimpan error | `2>` untuk stderr |
| `echo "Kode keluar: echo$?"` | `echo "Kode keluar: $?"` (`echo` sekali, di luar kutip). Spasi di `echo $?` wajib |
| `Ctrl + S` untuk menghentikan proses | `Ctrl + C` (SIGINT). `Ctrl + S` membekukan layar, `Ctrl + Q` melanjutkan |
| menekan `M` di dalam `man` | `M` hanya di dalam `top` |

### Modul 4 dan 5

| ❌ Salah | ✅ Benar |
|---|---|
| tidak menampilkan `cp`, `cat`, `python3` di log | tampilkan semuanya sebagai bukti |
| menjalankan sebelum menyimpan editan | simpan dulu, cek dengan `cat`, baru jalankan |
| menyalin nama fungsi/variabel dari modul | pakai nama dari soal |
| kode setelah `return` | tidak pernah jalan, perhatikan indent |
| `b[0] = a` (terbalik) | `a = b[0]`: variabel yang diisi ada di kiri `=` |
| `range(1, N)` untuk ID 1 sampai N | `range(1, N + 1)` |
| `acquire()` di dalam `try`, atau `finally` berisi hal lain | `acquire()` **sebelum** `try`, `finally` hanya berisi `release()` |
| di jalur gagal melepas alat yang tidak dipegang | lepas yang **benar-benar dipegang**, dan jangan lupa `break` di jalur berhasil |
| mematikan program background dengan `Ctrl+C` | `kill PID` atau `kill %nomor_job` |

### Modul 6

| ❌ Salah | ✅ Benar |
|---|---|
| `curl -o -L segfault.cpp ...` | `curl -L -o segfault.cpp ...` |
| `curl -L -o x.cpp ... > x.cpp` | jangan pakai `>` bersama `-o` (berkas kosong, `undefined reference to main`) |
| alamat unduhan diketik dari ingatan | salin persis dari modul, `translation_cpp` pakai garis bawah, `memhogcpp` tidak |
| `./segfault &` lalu `echo $?` (hasil `0`) | jalankan di foreground, hasil `139` |
| `kill PID` pada proses berstatus `T` | `kill -9 PID` |
| `exit PID` untuk menghentikan proses | `kill PID` (`exit` menutup sesi shell) |
| `rm ... /tmp/test_disk.img` | berkas disk ada di `~/test_disk.img` |
| `oflag=direct` pada RAM Disk | hanya untuk disk fisik |
| menganggap `<defunct>` masih hidup | zombie (`Z`) sudah mati, tidak memakai RAM |
| `swapon` sebelum `mkswap` | urutan: `fallocate`, `chmod 600`, `mkswap`, `swapon` |
| `rm /swapku` sebelum `swapoff` | `swapoff` dulu, baru `rm` |
| `& &&` setelah proses background | setelah `&` tidak boleh ada `&&` |
| `sudo` di background berstatus `Stopped` | jalankan `sudo -v` dulu |
| frame page paging "dihitung" | frame **dibaca dari page table**; offset = alamat mod ukuran page |
| segmentasi: langsung `base + offset` | **cek limit dulu** (offset harus < limit) |

### Modul 7

| ❌ Salah | ✅ Benar |
|---|---|
| `dd ... count=200M` | `count=200` (total = `bs` × `count`) |
| `unmount` | `umount` (satu n) |
| `"Blocksize"` pada `grep` | `"Block size"` (ada spasi) |
| menganggap soft link tetap hidup saat asli dihapus | hard link tetap hidup, soft link jadi broken link |

### Modul 8

| ❌ Salah | ✅ Benar |
|---|---|
| `ufw enable` sebelum mengizinkan SSH | `ufw allow` port SSH **dulu**, baru `ufw enable` (kalau tidak, koneksi SSH sendiri tertutup) |
| menutup sesi SSH sebelum login port baru berhasil | tes login lewat port baru dulu |
| menekan `Q` saat `visudo` bertanya "What now?" | tekan `e` untuk mengedit ulang |
| `passwd -u` pada akun tanpa password | isi password dulu, baru kunci dan buka |
| mengunci akun `magang` saat latihan | pakai user uji (`tamu`) |

### Semua modul

- Satu baris perintah harus **utuh**, jangan terpotong Enter di tengah (`bs=`, `>`).
- Cek posisi dengan `pwd`, atau tulis jalur lengkap dengan awalan `~/`. Path diawali `/` = absolut, tanpa `/` = relatif.
- `echo $?` selalu milik perintah **terakhir**, tulis tepat setelah perintah yang diperiksa.
- Buktikan hasil dengan perintah pengecekan (`id`, `ls -l`, `tail`, `grep`, `cat`) yang diminta soal.
- Cocokkan teks, nama file, dan angka dengan soal **karakter demi karakter**.

---

<a id="checklist"></a>

# ✅ Checklist Sebelum Ujian

**Modul 2**

- [ ] Hafal pola **`usermod -l baru -d /home/baru -m lama`**
- [ ] Hafal **r=4, w=2, x=1** dan hitung per kelompok (owner, group, others)
- [ ] Bedakan `usermod -aG grup user` dan `gpasswd -a user grup`
- [ ] Bedakan `passwd -l` / `-u` (kecil) dan `-S` (besar)

**Modul 3**

- [ ] Ingat `./script.sh`, shebang `#!/bin/bash` / `#!/usr/bin/python3`, dan `chmod u+x`
- [ ] Tahu beda `export` sementara dan `~/.bashrc` permanen, dan selalu tulis `$PATH:`
- [ ] Bedakan `>` (hasil), `2>` (error), dan `|` (pipe)
- [ ] Hafal `Ctrl + C` (SIGINT), `kill PID`, dan `kill -9 PID`
- [ ] Baca `echo $?`: `0` sukses, `126` tidak boleh dieksekusi, `127` tidak ditemukan, `139` segfault
- [ ] Bedakan interpreted dan compiled, dan tahu kenapa `cat /usr/bin/sh` berantakan

**Modul 4 dan 5**

- [ ] Hafal K-S-M-A (race condition) dan 4 segmen critical section
- [ ] Bisa menulis Mutex eksplisit (`acquire` sebelum `try`, `release` di `finally`) dan implisit (`with`)
- [ ] Bedakan Mutex (1 data) dan Semaphore (kapasitas N)
- [ ] Hafal M-H-N-C dan syarat mana yang diputus tiap solusi (urutan sama = Circular Wait, timeout = No Preemption)
- [ ] Bedakan DITUNDA dan DITOLAK pada Algoritma Banker, dan hitung Need = Max − Allocation

**Modul 6**

- [ ] Ingat `curl -L -o nama alamat` (urutan flag) dan salin alamat `bit.ly` persis
- [ ] Bisa membaca `pmap -x` dan baris `dmesg` (`error 4`, `6`, `7`)
- [ ] Bisa menelusuri First-Fit, Best-Fit, Worst-Fit, dan Next-Fit di atas kertas
- [ ] Bisa menghitung translasi paging (page, offset, frame, fisik) dan segmentasi (cek limit)
- [ ] Hafal urutan swap file: `fallocate`, `chmod 600`, `mkswap`, `swapon` (dan `swapoff` sebelum `rm`)
- [ ] Bisa menelusuri FIFO vs LRU, dan jelaskan Belady's anomaly

**Modul 7 dan 8**

- [ ] Bisa alur disk: `lsblk` → `mount` → `df` → `umount`, dan beda hard link vs soft link (`ls -li`)
- [ ] Bedakan `df` dan `du`, `dd count=200` (bukan `200M`), dan efek `sync`
- [ ] Bisa menghitung total FCFS dan SSTF (jumlah selisih mutlak)
- [ ] Hafal CIA, AAA, DAC vs MAC, dan least privilege
- [ ] Hafal urutan aman `ufw allow` → `ufw enable`, dan `sshd -t` sebelum restart SSH
- [ ] Bisa `setfacl -m` / `-x` + `getfacl`, `aa-complain` vs `aa-enforce`, dan `visudo -f` + `sudo -l -U`

**Umum**

- [ ] Selalu cek posisi dengan `pwd` dan buktikan hasil dengan perintah pengecekan

---

<div align="center">

**Semangat untuk pengujian akhirnya! 🚀**

<sub>Semua modul (2 sampai 8) sudah tercakup.</sub>

</div>