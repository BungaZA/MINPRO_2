# Mini Project: Sistem Pendaftaran Acara

from prettytable import PrettyTable
import pwinput

users = {
    "Karyawan": {"password": "123", "role": "Karyawan"},
    "Peserta": {"password": "234", "role": "Peserta"}
}

# Daftar peserta(id, nama, email)

peserta = [
("A001", "Paimon", "Paimon@gmail.com"),
("A002", "Lumine", "Lumine@gmail.com"),
("A003", "Aether", "Aether@gmail.com")
]


#login


def login():
    print(" LOGIN SISTEM PENDAFTARAN ACARA ")
    while True:
        username = input("username: ")
        password = pwinput.pwinput("password: ")

        if username in users and users[username]["password"] == password:
            print(f"\nLogin berhasil sebagai {users[username]['role']}\n")
            return users[username]["role"]
        else:
            print("\nLogin gagal. Username atau password salah!\n")

# Pilihan

def lihat():
    print("\n DAFTAR PESERTA TERDAFTAR ")
    if len(peserta) == 0:
        print("Tidak ada peserta terdaftar")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "NAMA", "EMAIL"]

        for p in peserta:
            tabel.add_row(p)
        
        print(tabel)

def daftarkan():
    try:
        print("\n DAFTARKAN PESERTA BARU ")
        ID = input("Masukkan ID peserta:")
        Nama = input("Masukkan Nama peserta:")
        Email = input("Masukkan Email Peserta:")
        peserta_baru = (ID, Nama, Email)
        peserta.append(peserta_baru)
        print("\nPeserta berhasil didaftarkan:")
        print(peserta_baru)
        print("\nDaftar Peserta Saat ini:")
        lihat()
    except Exception as e:
        print("Terjadi error:", e)
    except KeyboardInterrupt:
        print("tidak boleh CRTL + C")


def ubah():
    try:
        print("\n UBAH DATA PESERTA ")
        if len(peserta) == 0:
            print("Tidak ada peserta yang bisa diubah")
        else:
            print("daftar peserta saat ini:")
            lihat()
            nomor = int(input("\nMasukkan Urutan peserta yang ingin diubah (dimulai dari angka 0):"))
            if nomor < 0 or nomor >= len(peserta):
                print("Urutan melebihi peserta yang ada. Silahkan Ulangi Lagi")
            else:
                print("Data peserta yang dipilih:", peserta[nomor])
                ID_update = input("Masukkan ID peserta:")
                Nama_update = input("Masukkan Nama peserta:")
                Email_update = input("Masukkan Email Peserta:")
                peserta_update = (ID_update, Nama_update, Email_update)
                print("\nData peserta yang di perbaharui:")
                print(peserta_update)
                peserta[nomor] = peserta_update
                print("\nDaftar peserta saat ini:")
                lihat()
    except Exception as e:
        print("Terjadi error:", e)
    except ValueError:
        print("Harus memasukkan angka")
    except KeyboardInterrupt:
        print("tidak boleh CRTL + C")

def batalkan():
    try:
        print("\n BATALKAN PENDAFTARAN ")
        if len(peserta) == 0:
            print("Tidak ada peserta yang bisa dihapus")
        else:
            print("Daftar peserta saat ini:")
            lihat()
            nomor = int(input("\nMasukkan Urutan peserta yang ingin dihapus (dimulai dari angka 0):"))
            if nomor < 0 or nomor >= len(peserta):
                print("Urutan melebihi peserta yang ada. Silahkan Ulangi Lagi")
            else:
                terhapus = peserta.pop(nomor)
                print("\nPendaftaran berhasil dibatalkan untuk peserta:")
                print(terhapus)
                print("\nDaftar peserta sekarang:")
                if len(peserta) == 0:
                    print("Tidak ada peserta terdaftar")
                else:
                    lihat()
    except Exception as e:
        print("Terjadi error:", e)
    except ValueError:
        print("Harus memasukkan angka")
    except KeyboardInterrupt:
        print("tidak boleh CRTL + C")

def keluar():
    print("\nKeluar")
    print(" PROGRAM SELESAI")
    print(" TERIMAKASIH ❤️")



def menu(role):
    if role == "Karyawan":
        print("=== SISTEM PENDAFTARAN ACARA (Karyawan) ===")
        print("1. Tampilkan daftar peserta")
        print("2. Daftarkan peserta")
        print("3. Ubah data peserta")
        print("4. Batalkan pendaftaran")
        print("5. Keluar")
    elif role == "Peserta":
        print("=== SISTEM PENDAFTARAN ACARA (Peserta) ===")
        print("1. Tampilkan daftar peserta")
        print("2. Keluar") 

role = login()
if role:
    while True:
        menu(role)
        try:
            pilihan = int(input("Pilih menu: "))
            if role == "Karyawan":
                if pilihan == 1:
                    lihat()
                elif pilihan == 2:
                    daftarkan()
                elif pilihan == 3:
                    ubah()
                elif pilihan == 4:
                    batalkan()
                elif pilihan == 5:
                    keluar()
                    break
                else:
                    print("Pilihan tidak tersedia. Silahkan pilih 1-5")
            elif role == "Peserta":
                if pilihan == 1:
                    lihat()
                elif pilihan == 2:
                    keluar()
                    break
                else:
                    print("Pilihan tidak tersedia. Silahkan pilih 1-2")
        except ValueError:
            print("Pilihan harus berupa angka!")
        except KeyboardInterrupt:
            print("Tidak boleh CTRL + C")