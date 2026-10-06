import math
import random
import os
import time
from prettytable import PrettyTable
import pwinput

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"},
}
tabungan = {}

def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def kata_motivasi():
    kutipan = [
        "Sedikit demi sedikit, lama-lama menjadi bukit.",
        "Jangan menyerah, karena kegagalan adalah bagian dari kesuksesan.",
        "Kesuksesan bukanlah kunci kebahagiaan. Kebahagiaan adalah kunci kesuksesan."
    ]
    nomor = random.randint(0, len(kutipan) - 1)
    return kutipan[nomor]


def input_teks(pesan):
    teks = input(pesan)
    while teks == "":
        print("Input tidak boleh kosong. Silakan coba lagi.")
        teks = input(pesan)
        return teks

def input_angka(pesan, minimal):
    angka_ok = False
    while angka_ok == False:
        angka = input(pesan)
        if angka.isdigit() == False:
            print("Input harus berupa angka. Silakan coba lagi.")
        elif int(angka) < minimal:
            print("Angka Minimal", str(minimal))
        else:
            angka_ok = True
    return int(angka)

def input_pilihan(pesan, maksimal):
    pilih_ok = False
    while pilih_ok == False:
        pilihan = input(pesan)
        if pilihan.isdigit() == False:
            print("Input harus berupa angka. Silakan coba lagi.")
        elif int(pilihan) < 1 or int(pilihan) > maksimal:
            print("Pilihan hanya dari 1 sampai " + str(maksimal))
        else:
            pilih_ok = True
    return int(pilihan)


def pilih_id(data, pesan):
    id_pilih = input_angka(pesan + " (0 = batal): ", 0)
    while id_pilih != 0 and (id_pilih in data) == False:
        print("ID tidak ada di daftar!")
        id_pilih = input_angka(pesan + " (0 = batal): ", 0)
    return id_pilih


def login():
    percobaan = 0
    while percobaan < 3:
        username = input("Username: ")
        password = pwinput.pwinput(prompt="Password: ", mask="*")
        if username in users and users[username]["password"] == password:
            print("Login berhasil! Selamat datang, " + username)
            time.sleep(1)
            return username
        percobaan = percobaan + 1
        print("Username atau password salah! Sisa percobaan: " + str(3 - percobaan))
    return ""

def register():
    print("=== REGISTER AKUN BARU ===")
    username = input("Username (min 3 karakter): ")
    while len(username) < 3 or username in users:
        if len(username) < 3:
            print("Username minimal 3 karakter!")
        else:
            print("Username sudah dipakai!")
        username = input("Username (min 3 karakter): ")
    password = pwinput.pwinput(prompt="Password (min 6 karakter): ", mask="*")
    while len(password) < 6:
        print("Password minimal 6 karakter!")
        password = pwinput.pwinput(prompt="Password (min 6 karakter): ", mask="*")
    ulang = pwinput.pwinput(prompt="Ulangi password: ", mask="*")
    while ulang != password:
        print("Password tidak sama!")
        ulang = pwinput.pwinput(prompt="Ulangi password: ", mask="*")

    users[username] = {"password": password, "role": "user"}
    print("Akun berhasil dibuat, silakan login!")

def ambil_data(username, role):
    hasil = {}
    for id_data in tabungan:
        if role == "admin" or tabungan[id_data]["pemilik"] == username:
            hasil[id_data] = tabungan[id_data]
    return hasil



def tampilkan_tabel(data):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Pemilik", "Target", "Terkumpul", "Progress"]
    for id_data in data:
        nama = data[id_data]["nama"]
        pemilik = data[id_data]["pemilik"]
        target = data[id_data]["target"]
        terkumpul = data[id_data]["terkumpul"]
        persen = math.floor(terkumpul / target * 100)
        tabel.add_row([id_data, nama, pemilik, "Rp" + str(target), "Rp" + str(terkumpul), str(persen) + "%"])
    print(tabel)

def tambah_tabungan(username, role):
    print("=== TAMBAH DATA TABUNGAN ===")
    pemilik = username
    if role == "admin":
        print("Daftar username:")
        for nama_user in users:
            print("- " + nama_user)
        pemilik = input_teks("Username pemilik tabungan: ")
        while (pemilik in users) == False:
            print("Username tidak ditemukan!")
            pemilik = input_teks("Username pemilik tabungan: ")
    nama = input_teks("Nama tujuan tabungan: ")
    target = input_angka("Target nabung (Rp): ", 1)
    terkumpul = input_angka("Sudah terkumpul (Rp): ", 0)
    if terkumpul > target:
        print("Terkumpul tidak boleh lebih dari target, disamakan dengan target")
        terkumpul = target

    id_baru = 1
    for id_lama in tabungan:
        if id_lama >= id_baru:
            id_baru = id_lama + 1
    tabungan[id_baru] = {"nama": nama, "target": target, "terkumpul": terkumpul, "pemilik": pemilik}
    print("Data berhasil ditambahkan!")

def lihat_tabungan(username, role):
    print("=== DAFTAR TABUNGAN IMPIAN ===")
    data = ambil_data(username, role)
    if len(data) == 0:
        print("Belum ada data.")
    else:
        tampilkan_tabel(data)


def ubah_tabungan(username, role):
    print("=== UBAH DATA TABUNGAN ===")
    data = ambil_data(username, role)
    if len(data) == 0:
        print("Belum ada data untuk diubah.")
        return
    tampilkan_tabel(data)
    id_pilih = pilih_id(data, "ID yang mau diubah")
    if id_pilih == 0:
        print("Ubah data dibatalkan.")
        return
    print("1. Ubah nama")
    print("2. Ubah target")
    print("3. Ubah uang terkumpul")
    pilihan = input_pilihan("Mau ubah apa (1-3): ", 3)
    if pilihan == 1:
        tabungan[id_pilih]["nama"] = input_teks("Nama baru: ")
    elif pilihan == 2:
        tabungan[id_pilih]["target"] = input_angka("Target baru (Rp): ", 1)
    else:
        tabungan[id_pilih]["terkumpul"] = input_angka("Terkumpul baru (Rp): ", 0)

    if tabungan[id_pilih]["terkumpul"] > tabungan[id_pilih]["target"]:
        print("Terkumpul tidak boleh lebih dari target, disamakan dengan target")
        tabungan[id_pilih]["terkumpul"] = tabungan[id_pilih]["target"]
    print("Data berhasil diubah!")


def hapus_tabungan(username, role):
    print("=== HAPUS DATA TABUNGAN ===")
    data = ambil_data(username, role)
    if len(data) == 0:
        print("Belum ada data untuk dihapus.")
        return

    tampilkan_tabel(data)
    id_pilih = pilih_id(data, "ID yang mau dihapus")
    if id_pilih == 0:
        print("Hapus data dibatalkan.")
        return

    nama_hapus = tabungan[id_pilih]["nama"]
    yakin = input("Yakin mau hapus " + nama_hapus + "? (y/n): ")
    while yakin != "y" and yakin != "n":
        print("Ketik y atau n saja!")
        yakin = input("Yakin mau hapus " + nama_hapus + "? (y/n): ")

    if yakin == "y":
        del tabungan[id_pilih]
        print("Data " + nama_hapus + " berhasil dihapus!")
    else:
        print("Hapus data dibatalkan.")


def setor_tabungan(username, role):
    print("=== MENABUNG (SETOR UANG) ===")
    data = ambil_data(username, role)
    if len(data) == 0:
        print("Belum ada tabungan, tambah dulu lewat menu 1.")
        return

    tampilkan_tabel(data)
    id_pilih = pilih_id(data, "ID tabungan yang mau disetor")
    if id_pilih == 0:
        print("Setor uang dibatalkan.")
        return

    target = tabungan[id_pilih]["target"]
    terkumpul = tabungan[id_pilih]["terkumpul"]
    sisa = target - terkumpul
    if sisa == 0:
        print("Target tabungan ini sudah tercapai!")
        return

    print("Sisa yang dibutuhkan: Rp" + str(sisa))
    jumlah = input_angka("Jumlah setoran (Rp): ", 1)
    if jumlah > sisa:
        print("Setoran melebihi sisa, disesuaikan jadi Rp" + str(sisa))
        jumlah = sisa
    tabungan[id_pilih]["terkumpul"] = terkumpul + jumlah
    print("Setoran berhasil!")
    if terkumpul + jumlah == target:
        print("Selamat, tabungan impianmu sudah tercapai!")


def lihat_pengguna():
    print("=== DAFTAR PENGGUNA ===")
    tabel = PrettyTable()
    tabel.field_names = ["Username", "Role", "Jumlah Tabungan"]
    for nama_user in users:
        jumlah = 0
        for id_data in tabungan:
            if tabungan[id_data]["pemilik"] == nama_user:
                jumlah = jumlah + 1
        tabel.add_row([nama_user, users[nama_user]["role"], jumlah])
    print(tabel)

def menu_admin(username):
    while True:
        bersihkan_layar()
        print("=== MENU ADMIN ===")
        print("Login sebagai: " + username)
        print(kata_motivasi())
        print("")
        print("1. Tambah Data Tabungan")
        print("2. Tampilkan Semua Data")
        print("3. Ubah Data Tabungan")
        print("4. Hapus Data Tabungan")
        print("5. Lihat Daftar Pengguna")
        print("6. Logout")

        pilihan = input_pilihan("Pilih menu (1-6): ", 6)
        print("")

        if pilihan == 1:
            tambah_tabungan(username, "admin")
        elif pilihan == 2:
            lihat_tabungan(username, "admin")
        elif pilihan == 3:
            ubah_tabungan(username, "admin")
        elif pilihan == 4:
            hapus_tabungan(username, "admin")
        elif pilihan == 5:
            lihat_pengguna()
        else:
            print("Logout berhasil!")
            time.sleep(1)
            break

        input("\nTekan Enter untuk lanjut...")

def menu_user(username):
    while True:
        bersihkan_layar()
        print("=== MENU USER ===")
        print("Login sebagai: " + username)
        print(kata_motivasi())
        print("")
        print("1. Tambah Tabungan Impian")
        print("2. Lihat Tabungan Saya")
        print("3. Menabung (Setor Uang)")
        print("4. Logout")

        pilihan = input_pilihan("Pilih menu (1-4): ", 4)
        print("")

        if pilihan == 1:
            tambah_tabungan(username, "user")
        elif pilihan == 2:
            lihat_tabungan(username, "user")
        elif pilihan == 3:
            setor_tabungan(username, "user")
        else:
            print("Logout berhasil!")
            time.sleep(1)
            break

        input("\nTekan Enter untuk lanjut...")

while True:
    bersihkan_layar()
    print("=== TABUNGAN IMPIAN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input_pilihan("Pilih menu (1-3): ", 3)
    print("")

    if pilihan == 1:
        username_login = login()
        if username_login == "":
            print("Gagal login 3 kali, kembali ke menu awal.")
            input("\nTekan Enter untuk lanjut...")
        elif users[username_login]["role"] == "admin":
            menu_admin(username_login)
        else:
            menu_user(username_login)
    elif pilihan == 2:
        register()
        time.sleep(1)
    else:
        print("oke bai")
        break