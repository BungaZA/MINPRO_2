# MINPRO_2
Nama: Bunga Zulfa Aqila NIM: 2509116024 Sistem Informasi A 2025

# Deskripsi

Program ini merupakan implementasi sederhana sistem pendaftaran acara berbasis Python dengan menerapkan konsep CRUD (Create, Read, Update, Delete).\
Program ini juga sudah dilengkapi dengan:

- Sistem login dengan 2 role pengguna (Karyawan & Peserta).
- Hak akses berbeda sesuai role.
- Error Handling untuk mengantisipasi input tidak valid.
- PrettyTable untuk menampilkan data dengan rapi.
- pwinput untuk menyembunyikan input password.

  # Alur Program

<img width="1210" height="1918" alt="MINPRO 2 drawio" src="https://github.com/user-attachments/assets/e26ae955-e37b-4851-b778-43a91a29bf66" />

# Fitur Utama

**Login Sistem**

- Username & password harus sesuai.
- Role ditentukan dari akun login (Karyawan atau Peserta).
  
**CRUD (Create, Read, Update, Delete) – khusus Karyawan**
- Create : Menambahkan peserta baru ke dalam daftar.
- Read : Melihat daftar peserta yang sudah terdaftar.
- Update : Mengubah data peserta (id, nama, email).
- Delete : Menghapus data peserta dari daftar.

**READ - Khusus Peserta**

- Hanya bisa melihat daftar peserta atau keluar dari program.

# Alur Program

**Login**

- User memasukkan username & password.
- Jika valid, diarahkan ke menu sesuai role.

jika username/password salah akan menampilkan:\
<img width="362" height="95" alt="Screenshot 2025-09-29 000220" src="https://github.com/user-attachments/assets/4c07984e-c535-431f-b4d5-d18764fbf890" />

**Login sebagai Karyawan**

- Tampilan Karyawan apabila berhasil melakukan login\
<img width="335" height="206" alt="Screenshot 2025-09-29 000500" src="https://github.com/user-attachments/assets/758be132-f7bd-454a-9804-b57947954539" />

ada beberapa pilihan yang bisa karyawan lakukan, yang pertama adalah melihat daftar, menambah daftar, mengubah daftar, membatalkan daftar, lalu keluar dari grogramnya.

-melihat daftar\
<img width="344" height="133" alt="Screenshot 2025-09-29 000709" src="https://github.com/user-attachments/assets/00502a55-34c6-4e0a-bb8a-6c95e8abc541" />

apabila tidak ada peserta yang terdaftar maka akan ada pemberitahuan bahwa peserta tidak tersedia!

-menambahkan peserta\
<img width="280" height="288" alt="Screenshot 2025-09-29 001021" src="https://github.com/user-attachments/assets/4c6c4fed-dbee-4660-893e-be69532d6033" />

Proses penambahan peserta dilakukan dengan memasukkan ID, nama dan email.

-mengubah peserta\
<img width="428" height="491" alt="Screenshot 2025-09-29 001300" src="https://github.com/user-attachments/assets/6a970b9c-a290-4127-b627-7a4b0804985a" />

Memilih peserta yang ingin diubah, lalu mulai memasukkan ID, nama, dan email baru.\
jika saat memilih peserta, nomor yang dipilih tidak ada maka akan muncul pemberitahuan bahwa peserta tidak tersedia.

-membatalkan peserta\
<img width="424" height="401" alt="image" src="https://github.com/user-attachments/assets/d1edfaf2-4baf-4a67-b541-98c258b72533" />

melakukan pemilihan peserta yang akan dihapus.\
jika saat memilih peserta, nomor yang dipilih tidak ada maka akan muncul pemberitahuan bahwa peserta tidak tersedia.

-keluar\
<img width="182" height="48" alt="image" src="https://github.com/user-attachments/assets/c89e2c2f-1ded-4c9c-9504-533f79f2aefb" />


**Login sebagai Peserta**

- Tampilan Peserta apabila berhasil melakukan login\
<img width="303" height="101" alt="Screenshot 2025-09-29 002345" src="https://github.com/user-attachments/assets/c68325dc-6fca-4f9a-8402-44fe2e5491b7" />

- melihat daftar\
<img width="275" height="120" alt="Screenshot 2025-09-29 002257" src="https://github.com/user-attachments/assets/53d7ce2e-7767-4383-9311-d36667c2bcca" />
apabila tidak ada peserta yang terdaftar maka akan ada pemberitahuan bahwa peserta tidak tersedia!

- Keluar
<img width="184" height="50" alt="Screenshot 2025-09-29 002308" src="https://github.com/user-attachments/assets/6f87fbbf-a0ac-467c-91f7-b314d299e231" />

