# TECHNOVA-ID-LOGIN

---

#  Implementasi Hill Cipher - Login System TechNova ID


## 📘 Deskripsi Singkat

Proyek ini mengimplementasikan **Hill Cipher** untuk mengamankan sistem login internal startup **TechNova ID**.
Metode ini mengenkripsi **username** dan **password** menggunakan operasi matriks dalam **modulo 36**, dengan dukungan huruf **A–Z** dan angka **0–9**.

Tujuan:

> Melindungi kredensial login dari pencurian data dan memastikan autentikasi yang aman.

---

## ⚙️ Fitur Utama

* Pilihan ukuran matriks **2x2 / 3x3**
* **Generate Key otomatis** dengan validasi invertibilitas
* Enkripsi & dekripsi otomatis untuk username dan password
* Mendukung huruf dan angka
* Informasi lengkap matriks (determinant, inverse mod, GCD)
* Verifikasi hasil dekripsi otomatis

---

## 🧠 Konsep Dasar

* **Enkripsi:** `C = (K × P) mod 36`
* **Dekripsi:** `P = (K⁻¹ × C) mod 36`
* **Valid key:** `GCD(det mod 36, 36) = 1`

---

## 💻 Hasil Uji Singkat

### 🔹 Matriks 2x2

```
[5 8]
[17 3]
```

* Username : FAKHRIAFIF → LWZDXWLZNL ✅
* Password : CIHUY123 → ESDKKY7UP1 ✅

**Status:** Matriks VALID ✅ (invertible mod 36)

---

### 🔹 Matriks 3x3

```
[1 2 3]
[0 1 4]
[5 6 0]
```

* Username : FAKHRI123 → PXDKZI0KB ✅
* Password : TECHNOVA99 → 4LDJVYCA88 ✅

**Status:** Matriks VALID ✅ (invertible mod 36)

---

## 🖥️ Contoh Output Terminal

```bash
=========================================
HILL CIPHER - LOGIN SYSTEM TECHNOVA ID
=========================================

Pilih ukuran matriks:
1. 2x2
2. 3x3
Masukkan pilihan: 1

Matriks kunci:
[ 5  8 ]
[ 17 3 ]

Determinan: -121
Determinan mod 36: 7
Invers determinan: 31
Status: VALID ✅

Masukkan username: fakhriAfif
Masukkan password: cihuy123

--- HASIL ENKRIPSI ---
Username terenkripsi : LWZDXWLZNL
Password terenkripsi : ESDKKY7UP1

--- HASIL DEKRIPSI ---
Username asli : FAKHRIAFIF
Password asli : CIHUY123
Status: Dekripsi berhasil ✅
```

---

## ⚙️ Cara Instalasi & Menjalankan Program

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/implementasi-hill-cipher-technova.git
cd implementasi-hill-cipher-technova
```

### 2️⃣ Install Dependensi

Pastikan **Python 3** sudah terpasang, lalu jalankan:

```bash
pip install numpy
```

### 3️⃣ Jalankan Program

```bash
python hill_cipher.py
```

### 4️⃣ Ikuti Instruksi di Terminal

* Pilih ukuran matriks (2x2 / 3x3)
* Generate key otomatis atau gunakan kunci manual
* Masukkan username dan password
* Lihat hasil **enkripsi & dekripsi** langsung di terminal

---

## 🔍 Analisis Singkat

**Kelebihan:**

* Edukatif dan mudah dipahami
* Menggunakan konsep aljabar linear
* Dapat dikembangkan untuk karakter tambahan

**Kelemahan:**

* Tidak cocok untuk sistem modern
* Rentan terhadap *known-plaintext attack*
* Membutuhkan matriks invertible

---

## 🚀 Saran Pengembangan

* Gunakan **AES / RSA / bcrypt** untuk sistem produksi
* Tambahkan **GUI (Graphical User Interface)**
* Implementasikan **2FA, hashing, rate limiting**
* Tambahkan dukungan karakter spesial dan ekspor/impor kunci

---

## ⚠️ Catatan Keamanan

> ⚠️ Hill Cipher pada proyek ini hanya digunakan untuk **tujuan edukatif**.
> Untuk keamanan nyata, gunakan algoritma modern seperti:
>
> * AES (Advanced Encryption Standard)
> * RSA (Public-Key Cryptography)
> * bcrypt atau Argon2 untuk password hashing

---


