import numpy as np
from math import gcd
import random

class HillCipher:
    def __init__(self, key_matrix):
        """
        Inisialisasi Hill Cipher dengan matriks kunci
        key_matrix: list 2D untuk matriks kunci
        """
        self.key_matrix = np.array(key_matrix)
        self.n = len(key_matrix)
        self.mod = 36  # 26 huruf + 10 angka
        
        # Validasi matriks
        if not self.is_valid_key():
            raise ValueError("Matriks kunci tidak valid! Determinan harus relatif prima dengan 36.")
    
    def is_valid_key(self):
        """Mengecek apakah matriks kunci valid (dapat di-invers mod 36)"""
        det = int(round(np.linalg.det(self.key_matrix)))
        det_mod = det % self.mod
        return gcd(det_mod, self.mod) == 1
    
    def mod_inverse(self, a, m):
        """Menghitung invers modular dari a mod m"""
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    
    def matrix_mod_inv(self, matrix):
        """Menghitung invers matriks mod 36"""
        det = int(round(np.linalg.det(matrix)))
        det_mod = det % self.mod
        det_inv = self.mod_inverse(det_mod, self.mod)
        
        if det_inv is None:
            return None
        
        # Menghitung adjugate matrix
        matrix_inv = np.round(det * np.linalg.inv(matrix)).astype(int)
        matrix_inv = (det_inv * matrix_inv) % self.mod
        
        return matrix_inv
    
    def clean_text(self, text):
        """Membersihkan teks, mempertahankan huruf dan angka"""
        result = ""
        for char in text.upper():
            if char.isalpha() or char.isdigit():
                result += char
        return result
    
    def text_to_numbers(self, text):
        """
        Mengkonversi teks menjadi angka
        A-Z = 0-25
        0-9 = 26-35
        """
        text = self.clean_text(text)
        numbers = []
        for c in text:
            if c.isalpha():
                numbers.append(ord(c) - ord('A'))
            elif c.isdigit():
                numbers.append(int(c) + 26)
        return numbers
    
    def numbers_to_text(self, numbers):
        """
        Mengkonversi angka menjadi teks
        0-25 = A-Z
        26-35 = 0-9
        """
        result = ""
        for num in numbers:
            num = int(num) % self.mod
            if num < 26:
                result += chr(num + ord('A'))
            else:
                result += str(num - 26)
        return result
    
    def pad_text(self, text):
        """Menambahkan padding jika panjang teks tidak sesuai ukuran matriks"""
        while len(text) % self.n != 0:
            text += 'X'
        return text
    
    def encrypt(self, plaintext):
        """Enkripsi plaintext menggunakan Hill Cipher"""
        cleaned = self.clean_text(plaintext)
        cleaned = self.pad_text(cleaned)
        numbers = self.text_to_numbers(cleaned)
        
        ciphertext_numbers = []
        for i in range(0, len(numbers), self.n):
            block = np.array(numbers[i:i+self.n])
            encrypted_block = np.dot(self.key_matrix, block) % self.mod
            ciphertext_numbers.extend(encrypted_block.tolist())
        
        return self.numbers_to_text(ciphertext_numbers)
    
    def decrypt(self, ciphertext):
        """Dekripsi ciphertext menggunakan Hill Cipher"""
        inv_matrix = self.matrix_mod_inv(self.key_matrix)
        
        if inv_matrix is None:
            raise ValueError("Tidak dapat melakukan dekripsi! Matriks tidak memiliki invers.")
        
        numbers = self.text_to_numbers(ciphertext)
        
        plaintext_numbers = []
        for i in range(0, len(numbers), self.n):
            block = np.array(numbers[i:i+self.n])
            decrypted_block = np.dot(inv_matrix, block) % self.mod
            plaintext_numbers.extend(decrypted_block.tolist())
        
        return self.numbers_to_text(plaintext_numbers)
    
    def get_determinant(self):
        """Mendapatkan determinan dari matriks kunci"""
        det = int(round(np.linalg.det(self.key_matrix)))
        det_mod = det % self.mod
        det_inv = self.mod_inverse(det_mod, self.mod)
        return det, det_mod, det_inv


def verify_matrix_validity(matrix, mod=36):
    """Memverifikasi apakah matriks valid untuk Hill Cipher"""
    det = int(round(np.linalg.det(np.array(matrix))))
    det_mod = det % mod
    is_valid = gcd(det_mod, mod) == 1
    return is_valid, det, det_mod


def generate_random_key(n):
    """Membuat matriks acak yang invertible mod 36"""
    max_attempts = 1000
    attempts = 0
    
    while attempts < max_attempts:
        matrix = np.random.randint(0, 36, size=(n, n))
        det = int(round(np.linalg.det(matrix)))
        if gcd(det % 36, 36) == 1:
            return matrix.tolist()
        attempts += 1
    
    # Fallback ke matriks default yang valid
    print("\n⚠ Kesulitan generate key, menggunakan key default yang valid...")
    if n == 2:
        return [[5, 8], [17, 3]]
    else:
        # Matriks 3x3 yang sudah diverifikasi VALID
        return [[1, 2, 3], [0, 1, 4], [5, 6, 0]]


def print_matrix(matrix, title="Matriks"):
    """Mencetak matriks dengan format rapi"""
    print(f"\n{title}:")
    print("-" * 40)
    for row in matrix:
        print("  ", end="")
        for val in row:
            print(f"{val:3d}", end="  ")
        print()
    print("-" * 40)


def main():
    print("=" * 70)
    print("    HILL CIPHER - SISTEM LOGIN TECHNOVA ID (ENHANCED)")
    print("    Implementasi Enkripsi untuk Keamanan Kredensial Login")
    print("    ✨ Mendukung Huruf & Angka (A-Z, 0-9)")
    print("=" * 70)
    print()
    
    print("PILIH UKURAN MATRIKS KUNCI:")
    print("1. Matriks 2x2")
    print("2. Matriks 3x3")
    
    choice = input("\nPilihan Anda (1/2): ").strip()
    size = 2 if choice == '1' else 3
    
    print("\nPilih metode kunci:")
    print("1. Gunakan kunci default")
    print("2. Generate key otomatis")
    method = input("Pilihan Anda (1/2): ").strip()
    
    if method == '1':
        # Key default yang VALID untuk mod 36
        if size == 2:
            key_matrix = [[5, 8], [17, 3]]
            print("\n✓ Menggunakan matriks 2x2 default yang valid.")
        else:
            # Matriks 3x3 yang SUDAH DIVERIFIKASI VALID
            key_matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
            print("\n✓ Menggunakan matriks 3x3 default yang valid.")
            
        # Verifikasi validitas
        is_valid, det, det_mod = verify_matrix_validity(key_matrix)
        if not is_valid:
            print(f"\n⚠ PERINGATAN: Matriks tidak valid! (det={det}, det mod 36={det_mod})")
            print("Mencoba generate matriks baru yang valid...")
            key_matrix = generate_random_key(size)
    else:
        key_matrix = generate_random_key(size)
        print("\n✓ Kunci acak berhasil dibuat secara otomatis.")
    
    try:
        cipher = HillCipher(key_matrix)
        print_matrix(cipher.key_matrix, "Matriks Kunci Aktif")
        
        det, det_mod, det_inv = cipher.get_determinant()
        print(f"\nInformasi Matriks:")
        print(f"  Determinan           : {det}")
        print(f"  Determinan mod 36    : {det_mod}")
        print(f"  Invers det mod 36    : {det_inv}")
        print(f"  GCD(det mod 36, 36)  : {gcd(det_mod, 36)}")
        print(f"  Status               : VALID ✅")
        
        print("\n" + "=" * 70)
        print("PEMETAAN KARAKTER:")
        print("  Huruf: A-Z = 0-25")
        print("  Angka: 0-9 = 26-35")
        print("  Total karakter yang didukung: 36")
        print("=" * 70)
        
        print("\nINPUT KREDENSIAL LOGIN")
        username = input("Masukkan Username (huruf & angka): ").strip()
        password = input("Masukkan Password (huruf & angka): ").strip()
        
        if not username or not password:
            print("\n✗ Username dan password tidak boleh kosong!")
            return
        
        print("\n" + "=" * 70)
        print("HASIL ENKRIPSI DAN DEKRIPSI")
        print("=" * 70)
        
        encrypted_username = cipher.encrypt(username)
        decrypted_username = cipher.decrypt(encrypted_username)
        encrypted_password = cipher.encrypt(password)
        decrypted_password = cipher.decrypt(encrypted_password)
        
        print_matrix(cipher.key_matrix, "Matriks Kunci Final")
        
        print(f"\n📝 USERNAME:")
        print(f"  Asli      : {username}")
        print(f"  Enkripsi  : {encrypted_username}")
        print(f"  Dekripsi  : {decrypted_username}")
        print(f"  Status    : {'✅ COCOK' if username.upper().replace(' ', '') == decrypted_username.replace('X', '')[:len(username)] else '❌ TIDAK COCOK'}")
        
        print(f"\n🔐 PASSWORD:")
        print(f"  Asli      : {password}")
        print(f"  Enkripsi  : {encrypted_password}")
        print(f"  Dekripsi  : {decrypted_password}")
        print(f"  Status    : {'✅ COCOK' if password.upper().replace(' ', '') == decrypted_password.replace('X', '')[:len(password)] else '❌ TIDAK COCOK'}")
        
        print("\n" + "=" * 70)
        print("✓ Proses enkripsi dan dekripsi berhasil dilakukan!")
        print("✓ Angka berhasil dienkripsi tanpa dikonversi ke kata!")
        print("=" * 70)
        
    except ValueError as e:
        print(f"\n❌ ERROR: {e}")
        print("Matriks yang digunakan tidak valid untuk Hill Cipher mod 36.")
        print("Silakan coba lagi dengan generate key otomatis.")


if __name__ == "__main__":
    main()