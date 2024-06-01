import pandas as pd
import os
import getpass
from tabulate import tabulate
import random

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def baca_csv (nama_file):
    df = pd.read_csv(nama_file, index_col="id")
    return df

def tulis_csv (df, nama_file):
    df.to_csv(nama_file)

def get_last_id(df):
    if len(df.index) > 0:
        return df.index[-1]
    else:
        return 0

# _______________________________________________________________ADMIN_____________________________________________
def autentikasi_admin(username, password):
    df = baca_csv('admin.csv')

    admin = df.values.tolist()
    for i in admin:
        if i[0] == username and i[1] == password:
            return True
    return False

def tambah_produk_food():
    os.system('cls')
    df = baca_csv('Food.csv')
    merk =      input('Masukkan merk makanan yang ingin anda tambahkan         : ')
    netto = int(input('Masukkan netto barang anda(gram)                        : '))
    jumlah =int(input('Masukkan jumlah barang anda                             : '))
    harga = int(input('Masukkan harga barang anda(tanpa titik atau apapun)     : '))

    df = baca_csv('Food.csv')

    while True:
        df.loc[get_last_id(df) + 1] = [merk, netto, jumlah, harga]
        tulis_csv(df, 'Food.csv')
        break
    input('Produk telah berhasil ditambahkan. Tekan enter untuk melanjutkan')

def tambah_produk_drink():
    os.system('cls')
    df = baca_csv('drink.csv')
    merk =      input('Masukkan merk minuman yang ingin anda tambahkan         : ')
    netto = int(input('Masukkan netto barang anda(ml)                          : '))
    jumlah =int(input('Masukkan jumlah barang anda                             : '))
    harga = int(input('Masukkan harga barang anda(tanpa titik atau apapun)     : '))

    df = baca_csv('drink.csv')

    while True:
        df.loc[get_last_id(df) + 1] = [merk, netto, jumlah, harga]
        tulis_csv(df, 'drink.csv')
        break
    input('Produk telah berhasil ditambahkan. Tekan enter untuk melanjutkan')

def tambah_produk_cosmetik():
    os.system('cls')
    df = baca_csv('cosmetik.csv')
    merk =      input('Masukkan merk barang kosmetik yang ingin anda tambahkan : ')
    netto = int(input('Masukkan netto barang anda(gram)                        : '))
    jumlah =int(input('Masukkan jumlah barang anda                             : '))
    harga = int(input('Masukkan harga barang anda(tanpa titik atau apapun)     : '))

    df = baca_csv('cosmetik.csv')

    while True:
        df.loc[get_last_id(df) + 1] = [merk, netto, jumlah, harga]
        tulis_csv(df, 'cosmetik.csv')
        break
    input('Produk telah berhasil ditambahkan. Tekan enter untuk melanjutkan')

def tambah_produk_shampoo():
    os.system('cls')
    df = baca_csv('Shampoo.csv')
    merk =      input('Masukkan merk sampo yang ingin anda tambahkan           : ')
    netto = int(input('Masukkan netto barang anda(ml)                          : '))
    jumlah =int(input('Masukkan jumlah barang anda                             : '))
    harga = int(input('Masukkan harga barang anda(tanpa titik atau apapun)     : '))

    df = baca_csv('Shampoo.csv')

    while True:
        df.loc[get_last_id(df) + 1] = [merk, netto, jumlah, harga]
        tulis_csv(df, 'Shampoo.csv')
        break
    input('Produk telah berhasil ditambahkan. Tekan enter untuk melanjutkan')

def tambah_produk_soap():
    os.system('cls')
    df = baca_csv('Soap.csv')
    merk =      input('Masukkan merk sabun yang ingin anda tambahkan           : ')
    netto = int(input('Masukkan netto barang anda(gram)                        : '))
    jumlah =int(input('Masukkan jumlah barang anda                             : '))
    harga = int(input('Masukkan harga barang anda(tanpa titik atau apapun)     : '))

    df = baca_csv('Soap.csv')

    while True:
        df.loc[get_last_id(df) + 1] = [merk, netto, jumlah, harga]
        tulis_csv(df, 'Soap.csv')
        break
    input('Produk telah berhasil ditambahkan. Tekan enter untuk melanjutkan')

def ubah_harga_food():
    os.system('cls')
    df = baca_csv('Food.csv')
    print("Daftar semua Makanan:")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin diubah harganya (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi ubah harga.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return

    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan! Tekan Enter untuk melanjutkan.')
        return
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return

    os.system('cls')
    print('Mengubah Harga')
    print('[1] Merk         : ' + df.loc[id, 'MEREK'])
    print('[2] Berat (gram) : ' + str(df.loc[id, 'NETTO']))
    print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
    print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

    harga_baru = float(input('Masukkan harga baru: '))
    df.loc[id, 'HARGA'] = harga_baru

    tulis_csv(df, 'Food.csv')
    input('Harga berhasil diubah. Tekan enter untuk melanjutkan.')


def ubah_harga_drink():
    os.system('cls')
    df = baca_csv('drink.csv')
    print("Daftar semua Minuman:")
    tabel = [["ID", "Merk", "Netto(ml)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin diubah harganya (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi ubah harga.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return

    os.system('cls')
    print('Mengubah Harga')
    print('[1] Merk         : ' + df.loc[id, 'MEREK'])
    print('[2] Berat (ml)   : ' + str(df.loc[id, 'NETTO']))
    print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
    print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

    harga_baru = float(input('Masukkan harga baru: '))
    df.loc[id, 'HARGA'] = harga_baru

    tulis_csv(df, 'drink.csv')
    input('Harga berhasil diubah. Tekan enter untuk melanjutkan.')


def ubah_harga_cosmetik():
    os.system('cls')
    df = baca_csv('cosmetik.csv')
    print("Daftar semua Kosmetik:")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin diubah harganya (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi ubah harga.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return

    os.system('cls')
    print('Mengubah Harga')
    print('[1] Merk         : ' + df.loc[id, 'MEREK'])
    print('[2] Berat        : ' + str(df.loc[id, 'NETTO']))
    print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
    print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

    harga_baru = float(input('Masukkan harga baru: '))
    df.loc[id, 'HARGA'] = harga_baru

    tulis_csv(df, 'cosmetik.csv')
    input('Harga berhasil diubah. Tekan enter untuk melanjutkan.')


def ubah_harga_shampoo():
    os.system('cls')
    df = baca_csv('Shampoo.csv')
    print("Daftar semua Shampoo:")
    tabel = [["ID", "Merk", "Netto(ml)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin diubah harganya (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi ubah harga.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return

    os.system('cls')
    print('Mengubah Harga')
    print('[1] Merk         : ' + df.loc[id, 'MEREK'])
    print('[2] Berat (ml)   : ' + str(df.loc[id, 'NETTO']))
    print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
    print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

    harga_baru = float(input('Masukkan harga baru: '))
    df.loc[id, 'HARGA'] = harga_baru

    tulis_csv(df, 'Shampoo.csv')
    input('Harga berhasil diubah. Tekan enter untuk melanjutkan.')


def ubah_harga_soap():
    os.system('cls')
    df = baca_csv('Soap.csv')
    print("Daftar semua Sabun:")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin diubah harganya (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi ubah harga.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return

    os.system('cls')
    print('Mengubah Harga')
    print('[1] Merk         : ' + df.loc[id, 'MEREK'])
    print('[2] Berat (gram) : ' + str(df.loc[id, 'NETTO']))
    print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
    print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

    harga_baru = float(input('Masukkan harga baru: '))
    df.loc[id, 'HARGA'] = harga_baru

    tulis_csv(df, 'Soap.csv')
    input('Harga berhasil diubah. Tekan enter untuk melanjutkan.')


def home_ubah_harga():
    while True:
        os.system('cls')
        print(f'''
    ||=====================================||
    ||     SELAMAT DATANG SANG PEGAWAI     ||
    ||                                     ||
    ||        Kategori barang Yang         ||
    ||         Hendak Diubah               ||
    ||              Harganya :             ||
    ||                                     ||
    ||  1. Makanan/Snack                   ||
    ||  2. Minuman                         ||
    ||  3. Kecantikan/Kosmetik             ||
    ||  4. Sabun                           ||
    ||  5. Sampo                           ||
    ||  6. Kembali ke Home Page            ||
    ||                                     ||
    ||=====================================||            
    ''')
        pilih = input('Masukkan opsi yang ingin anda pilih: ')
        match pilih:
            case '1':
                ubah_harga_food()
            case '2':
                ubah_harga_drink()
            case '3':
                ubah_harga_cosmetik()
            case '4':
                ubah_harga_soap()
            case '5':
                ubah_harga_shampoo()
            case '6':
                break
            case _:
                input('Pilih opsi yang telah disediakan. Tekan enter untuk melanjutkan')

def hapus_produk_food():
    os.system('cls')
    df = baca_csv('Food.csv')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))  # Tampilkan data menggunakan tabulate
    id_input = input('Masukkan id barang yang ingin dihapus (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan penghapusan barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        index = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    

    if index in df.index:
        df = df.drop(index)
        tulis_csv(df, 'Food.csv')
        print(f'Produk pada index {index} telah berhasil dihapus.')
    else:
        print(f'Index {index} tidak ditemukan.')

    input('Tekan enter untuk melanjutkan')

def hapus_produk_drink():
    os.system('cls')
    df = baca_csv('drink.csv')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))  # Tampilkan data menggunakan tabulate
    id_input = input('Masukkan id barang yang ingin dihapus (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan penghapusan barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        index = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    

    if index in df.index:
        df = df.drop(index)
        tulis_csv(df, 'drink.csv')
        print(f'Produk pada index {index} telah berhasil dihapus.')
    else:
        print(f'Index {index} tidak ditemukan.')

    input('Tekan enter untuk melanjutkan')

def hapus_produk_cosmetik():
    os.system('cls')
    df = baca_csv('cosmetik.csv')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))  # Tampilkan data menggunakan tabulate
    id_input = input('Masukkan id barang yang ingin dihapus (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan penghapusan barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        index = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return

    if index in df.index:
        df = df.drop(index)
        tulis_csv(df, 'cosmetik.csv')
        print(f'Produk pada index {index} telah berhasil dihapus.')
    else:
        print(f'Index {index} tidak ditemukan.')

    input('Tekan enter untuk melanjutkan')

def hapus_produk_shampoo():
    os.system('cls')
    df = baca_csv('Shampoo.csv')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))  # Tampilkan data menggunakan tabulate
    id_input = input('Masukkan id barang yang ingin dihapus (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan penghapusan barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        index = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return

    if index in df.index:
        df = df.drop(index)
        tulis_csv(df, 'Shampoo.csv')
        print(f'Produk pada index {index} telah berhasil dihapus.')
    else:
        print(f'Index {index} tidak ditemukan.')

    input('Tekan enter untuk melanjutkan')

def hapus_produk_Soap():
    os.system('cls')
    df = baca_csv('Soap.csv')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))  # Tampilkan data menggunakan tabulate
    id_input = input('Masukkan id barang yang ingin dihapus (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi penghapusan barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        index = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return

    if index in df.index:
        df = df.drop(index)
        tulis_csv(df, 'Soap.csv')
        print(f'Produk pada index {index} telah berhasil dihapus.')
    else:
        print(f'Index {index} tidak ditemukan.')

    input('Tekan enter untuk melanjutkan')

def hapus_pegawai():
    os.system('cls')
    df = baca_csv('Pegawai.csv')

    df_display = df.drop(columns=['password'], errors='ignore')
    
    print(tabulate(df_display, headers='keys', tablefmt='fancy_grid'))
    id_input = input('Masukkan id akun pegawai yang ingin dihapus (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan operasi Penghapusan Akun Pegawai.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        index = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    

    while True:
        if index in df.index:
            print('''
    ||==================================||
    ||  Anda Yakin Ingin Menghapus      ||
    ||        Akun Pegawai ??           ||
    ||        [1] Yakin                 ||
    ||        [2] Tidak                 ||
    ||==================================||
    ''')
            pilih = input('Masukkan pilihan anda : ')

            match pilih:
                case '1':
                    df = df.drop(index)
                    tulis_csv(df, 'Pegawai.csv')
                    print(f'Akun pegawai pada index {index} telah berhasil dihapus.')
                    input('Tekan enter untuk melanjutkan')
                    break

                case '2':
                    break
                
                case _:
                    input('Masukkan pilihan sesuai dengan yang telah disediakan. Tekan enter untuk melanjutkan')
        else:
            print(f'Index {index} tidak ditemukan.')
            break

    

def tambah_pegawai ():
    os.system('cls')
    nama_lengkap =  input("Masukkan nama lengkap pegawai     : ")
    username =      input("Masukkan username pegawai         : ")
    password =      getpass.getpass("Masukkan password pegawai         : ") 
    password2 =     getpass.getpass("Masukkan password yang sama       : ")
    alamat =        input("Masukkan alamat lengkap pegawai   : ")
    no_telepon =    (input("Masukkan nomor telepon pegawai    : "))

    df = baca_csv('Pegawai.csv')
    while True:
        os.system('cls')
        if password != password2:
            input("Pastikan password anda telah sama. Tekan enter untuk melanjutkan")
            password =  getpass.getpass("Masukkan password pegawai         : ") 
            password2 = getpass.getpass("Masukkan password yang sama       : ")
            continue
        
        if username in df['username'].values:
            input("Username telah dipakai. Tekan enter untuk melanjutkan.")
            username = input("Masukkan username pegawai         : ")
            continue
        
        df.loc[get_last_id(df) + 1] = [nama_lengkap, username, password, alamat, no_telepon]
        tulis_csv(df, 'Pegawai.csv')
        input("Pegawai telah ditambahkan. Tekan enter untuk melanjutkan")
        break
    # for i in range(len(df)):
    #     print

def cari_pegawai ():
    os.system('cls')
    df = baca_csv('Pegawai.csv')
    
    keyword = input("Masukkan Username Pegawai yang ingin dicari (Kosongkan jika ingin melihat semuanya) : ")

    if keyword == "":
        print("Daftar semua Pegawai:")
        tabel = [["Nama", "Nomor Handphone"]]
        for i in range(len(df)):
            tabel.append([df.loc[i, 'Nama'], df.loc[i, 'nomor_telepon']])
        print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))
        input("Semua data telah ditampilkan. Tekan enter untuk melanjutkan")

    else :
        for i in range(len(df)):
            if df.loc[i, 'username'] == keyword:
                os.system('cls')
                print(f"Username ditemukan : {df.loc[i, 'Nama']} \nNomor Handphone : {df.loc[i, 'nomor_telepon']} \nAlamat : {df.loc[i, 'alamat']} \n")
                print(input('Data telah ditampilkan. Tekan enter untuk melanjutkan'))
        return "kosong"

def edit_pegawai():
    os.system('cls')
    df = baca_csv('Pegawai.csv')

    # Menampilkan semua anggota
    print("Daftar semua Pegawai:")
    tabel = [["ID", "Nama Lengkap", "Username", "Alamat", "Nomor Telepon"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'Nama'], df.loc[i, 'username'], df.loc[i, 'alamat'], df.loc[i, 'nomor_telepon']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id Pegawai yang ingin diedit (angka) atau tekan Enter untuk membatalkan: ')

    if id_input == '':
        print('Membatalkan operasi edit.')
        input('Tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return

    # Memastikan id anggota ada
    if id not in df.index:
        input(f'Pegawai dengan id {id} tidak ditemukan! Tekan Enter untuk melanjutkan.')
        return

    try:
        while True:
            os.system('cls')
            print('Mengedit pegawai')
            print('[1] Nama lengkap: ' + df.loc[id, 'Nama'])
            print('[2] Username: ' + df.loc[id, 'username'])
            print('[3] Alamat: ' + str(df.loc[id, 'alamat']))
            print('[4] Nomor Telepon : ' + str(df.loc[id, 'nomor_telepon']))
            print('[5] Selesai')

            pilihan = input('Masukan: ')
            match pilihan:
                case '1':
                    nama_lengkap_baru = input('Masukkan nama lengkap baru: ')
                    df.loc[id, 'Nama'] = nama_lengkap_baru
                case '2':
                    username = input('Masukkan username baru: ')
                    df.loc[id, 'username'] = username
                case '3':
                    alamat = input('Masukkan alamat baru: ')
                    df.loc[id, 'alamat'] = alamat
                case '4':
                    nomor_telp = input('Masukkan Nomor Telepon baru : ') 
                    df.loc[id, 'nomor_telepon'] = nomor_telp
                case '5':
                    break
                case _:
                    input('Pilihan tidak valid! Tekan enter untuk melanjutkan')
                    continue

            tulis_csv(df, 'Pegawai.csv')
            input('Berhasil! Tekan enter untuk melanjutkan')
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def home_admin():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
||=====================================||
||      SELAMAT DATANG SANG ADMIN      ||
||                                     ||
||        Silahkan Pilih Opsi :        ||
||                                     ||
||      ====== Atur Pegawai =====      ||
||                                     ||
||  1. Tambahkan Pegawai               ||
||  2. Hapus Pegawai                   ||
||  3. Cari Pegawai                    ||
||  4. Edit Pegawai                    ||
||                                     ||
||       ===== Atur Barang =====       ||
||                                     ||
||  5. Tambahkan Barang                ||
||  6. Ubah Harga Barang               ||
||  7. Hapus Barang                    ||
||  8. Lihat Stock                     ||
||  9. Kembali ke Home Page            ||
||                                     ||
||=====================================||            
''')
        pilih = input("Masukkan Opsi Anda : ")
        match pilih :
            case '1' :
                tambah_pegawai()
            case '2' :
                hapus_pegawai()
            case '3' :
                cari_pegawai()
            case '4' :
                edit_pegawai()
            case '5' :
                home_tambah_barang()
            case '6' :
                home_ubah_harga()
            case '7':
                home_hapus_barang()
            case '8':
                home_lihat_stock_admin()
            case '9':
                break
            case _ :
                input("Masukkan opsi sesuai dengan yang telah disediakan. Tekan enter untuk melanjutkan")

def home_hapus_barang ():
    while True:
        os.system('cls')
        print(f'''
    ||=====================================||
    ||      SELAMAT DATANG SANG ADMIN      ||
    ||                                     ||
    ||        Kategori barang Yang         ||
    ||          Hendak Dihapus :           ||
    ||                                     ||
    ||  1. Makanan/Snack                   ||
    ||  2. Minuman                         ||
    ||  3. Kecantikan/Kosmetik             ||
    ||  4. Sabun                           ||
    ||  5. Sampo                           ||
    ||  6. Kembali ke Menu Admin           ||
    ||                                     ||
    ||=====================================||            
    ''')
        pilih = input ('Masukkan opsi yang ingin anda pilih : ')
        match pilih :
            case '1':
                hapus_produk_food()
            case '2':
                hapus_produk_drink()
            case '3':
                hapus_produk_cosmetik()
            case '4':
                hapus_produk_Soap()
            case '5':
                hapus_produk_shampoo()
            case '6':
                break
            case _ :
                input('Masukkan opsi sesuai yang telah disediakan. Tekan enter untuk melanjutkan')

def home_tambah_barang ():
    while True:
        os.system('cls')
        print(f'''
    ||=====================================||
    ||      SELAMAT DATANG SANG ADMIN      ||
    ||                                     ||
    ||        Kategori barang Yang         ||
    ||        Hendak Ditambahkan :         ||
    ||                                     ||
    ||  1. Makanan/Snack                   ||
    ||  2. Minuman                         ||
    ||  3. Kecantikan/Kosmetik             ||
    ||  4. Sabun                           ||
    ||  5. Sampo                           ||
    ||  6. Kembali ke Menu Admin           ||
    ||                                     ||
    ||=====================================||            
    ''')
        pilih = input ('Masukkan opsi yang ingin anda pilih : ')
        match pilih :
            case '1' :
                tambah_produk_food()
            case '2' :
                tambah_produk_drink()
            case '3' :
                tambah_produk_cosmetik()
            case '4' :
                tambah_produk_soap()
            case '5' :
                tambah_produk_shampoo()
            case '6' :
                break
            case _ :
                input ('Pilih opsi yang telah disediakan. Tekan enter untuk melanjutkan')

def home_lihat_stock_admin():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
        ||======================================||
        ||    Pilih Kategori yang diinginkan :  ||  
        ||      [1] Makanan                     ||
        ||      [2] Minuman                     ||
        ||      [3] Kosmetik                    ||
        ||      [4] Sabun                       ||
        ||      [5] Sampo                       ||
        ||      [6] Kembali                     ||
        ||======================================||
        ''')

        pilih = input('Masukkan pilihan: ')
        if pilih == '1':
            lihat_stok_food()
        elif pilih == '2':
            lihat_stok_drink()
        elif pilih == '3':
            lihat_stok_kosmetik()
        elif pilih == '4':
            lihat_stok_sabun()
        elif pilih == '5':
            lihat_stok_shampo()
        elif pilih == '6':
            break
        else:
            input('Masukkan opsi sesuai yang diberikan. Tekan Enter untuk melanjutkan.')


# _____________________________________________________________PEGAWAI___________________________________________
def autentikasi_pegawai(username, password):
    df = baca_csv('Pegawai.csv')

    pegawai = df.values.tolist()
    for i in pegawai:
        if i[1] == username and i[2] == password:
            return True
    return False

def tambah_stock_food():
    os.system('cls')
    df = baca_csv('Food.csv')
    print("Daftar semua Makanan:")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin dirubah stok (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan perubahan stok barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return
    
    while True:
        os.system('cls')
        print('Menambah')
        print('[1] Merk         : ' + df.loc[id, 'MEREK'])
        print('[2] Berat (gram) : ' + str(df.loc[id, 'NETTO']))
        print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
        print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

        stock_tambahan = int(input('Masukkan berapa stok yang ingin ditambahkan(ketik "0" jika ingin membatalkan penambahan stok dan tambahkan tanda min (-) jika \ningin mengurangi stok) : '))
        
        df.loc[id,'JML'] += stock_tambahan

        tulis_csv(df, 'Food.csv')
        os.system('cls')
        print ('''
    ||======================================||
    ||           [1] Tambah lagi            ||
    ||           [2] Kembali                ||
    ||======================================||
''')
        pilih = input("Pilih opsi anda : ")
        match pilih:
            case '1':
                continue
            case '2' :
                break
            case _:
                input('Pilih opsi yang disediakan. Tekan enter untuk melanjutkan')

def tambah_stock_drink():
    os.system('cls')
    df = baca_csv('drink.csv')
    print("Daftar semua Minuman:")
    tabel = [["ID", "Merk", "Netto(ml)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin dirubah stok (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan perubahan stok barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return
    
    while True:
        os.system('cls')
        print('Menambah')
        print('[1] Merk         : ' + df.loc[id, 'MEREK'])
        print('[2] Berat (ml)   : ' + str(df.loc[id, 'NETTO']))
        print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
        print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

        stock_tambahan = int(input('Masukkan berapa stok yang ingin ditambahkan(ketik "0" jika ingin membatalkan penambahan stok dan tambahkan tanda min (-) jika \ningin mengurangi stok) : '))
        df.loc[id,'JML'] += stock_tambahan

        tulis_csv(df, 'drink.csv')
        os.system('cls')
        print ('''
    ||======================================||
    ||           [1] Tambah lagi            ||
    ||           [2] Kembali                ||
    ||======================================||
''')
        pilih = input("Pilih opsi anda : ")
        match pilih:
            case '1':
                continue
            case '2' :
                break
            case _:
                input('Pilih opsi yang disediakan. Tekan enter untuk melanjutkan')


def tambah_stock_cosmetik():
    os.system('cls')
    df = baca_csv('cosmetik.csv')
    print("Daftar semua Cosmetik : ")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin dirubah stok (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan perubahan stok barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return
    
    while True:
        os.system('cls')
        print('Menambah')
        print('[1] Merk         : ' + df.loc[id, 'MEREK'])
        print('[2] Berat        : ' + str(df.loc[id, 'NETTO']))
        print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
        print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

        stock_tambahan = int(input('Masukkan berapa stok yang ingin ditambahkan(ketik "0" jika ingin membatalkan penambahan stok dan tambahkan tanda min (-) jika \ningin mengurangi stok) : '))
        df.loc[id,'JML'] += stock_tambahan

        tulis_csv(df, 'cosmetik.csv')
        os.system('cls')
        print ('''
    ||======================================||
    ||           [1] Tambah lagi            ||
    ||           [2] Kembali                ||
    ||======================================||
''')
        pilih = input("Pilih opsi anda : ")
        match pilih:
            case '1':
                continue
            case '2' :
                break
            case _:
                input('Pilih opsi yang disediakan. Tekan enter untuk melanjutkan')

def tambah_stock_shampoo():
    os.system('cls')
    df = baca_csv('Shampoo.csv')
    print("Daftar semua Shampoo :")
    tabel = [["ID", "Merk", "Netto(ml)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin dirubah stok (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan perubahan stok barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return
    
    while True:
        os.system('cls')
        print('Menambah')
        print('[1] Merk         : ' + df.loc[id, 'MEREK'])
        print('[2] Berat (ml)   : ' + str(df.loc[id, 'NETTO']))
        print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
        print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

        stock_tambahan = int(input('Masukkan berapa stok yang ingin ditambahkan(ketik "0" jika ingin membatalkan penambahan stok dan tambahkan tanda min (-) jika \ningin mengurangi stok) : '))
        df.loc[id,'JML'] += stock_tambahan

        tulis_csv(df, 'Shampoo.csv')
        os.system('cls')
        print ('''
    ||======================================||
    ||           [1] Tambah lagi            ||
    ||           [2] Kembali                ||
    ||======================================||
''')
        pilih = input("Pilih opsi anda : ")
        match pilih:
            case '1':
                continue
            case '2' :
                break
            case _:
                input('Pilih opsi yang disediakan. Tekan enter untuk melanjutkan')

def tambah_stock_soap():
    os.system('cls')
    df = baca_csv('Soap.csv')
    print("Daftar semua Sabun:")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))

    id_input = input('Masukkan id barang yang ingin dirubah stok (atau tekan Enter untuk membatalkan): ')

    if id_input == '':
        print('Membatalkan perubahan stok barang.')
        input('tekan enter untuk melanjutkan')
        return

    try:
        id = int(id_input)
    except ValueError:
        input('ID yang dimasukkan tidak valid! Tekan Enter untuk melanjutkan.')
        return
    
    if id not in df.index:
        input(f'Barang dengan id {id} tidak ditemukan!')
        return
    
    while True:
        os.system('cls')
        print('Menambah')
        print('[1] Merk         : ' + df.loc[id, 'MEREK'])
        print('[2] Berat (ml)   : ' + str(df.loc[id, 'NETTO']))
        print('[3] Stok Barang  : ' + str(df.loc[id, 'JML']))
        print('[4] Harga        : ' + str(df.loc[id, 'HARGA']) + '\n')

        stock_tambahan = int(input('Masukkan berapa stok yang ingin ditambahkan(ketik "0" jika ingin membatalkan penambahan stok dan tambahkan tanda min (-) jika \ningin mengurangi stok) : '))
        df.loc[id,'JML'] += stock_tambahan

        tulis_csv(df, 'Soap.csv')
        os.system('cls')
        print ('''
    ||======================================||
    ||           [1] Tambah lagi            ||
    ||           [2] Kembali                ||
    ||======================================||
''')
        pilih = input("Pilih opsi anda : ")
        match pilih:
            case '1':
                continue
            case '2' :
                break
            case _:
                input('Pilih opsi yang disediakan. Tekan enter untuk melanjutkan')


def home_tambah_stock ():
    while True:
        os.system('cls')
        print(f'''
    ||=====================================||
    ||     SELAMAT DATANG SANG PEGAWAI     ||
    ||                                     ||
    ||        Kategori barang Yang         ||
    ||         Hendak Ditambahkan          ||
    ||              Stocknya :             ||
    ||                                     ||
    ||  1. Makanan/Snack                   ||
    ||  2. Minuman                         ||
    ||  3. Kecantikan/Kosmetik             ||
    ||  4. Sabun                           ||
    ||  5. Sampo                           ||
    ||  6. Kembali ke Home Page            ||
    ||                                     ||
    ||=====================================||            
    ''')
        pilih = input ('Masukkan opsi yang ingin anda pilih : ')
        match pilih :
            case '1' :
                tambah_stock_food()
            case '2' :
                tambah_stock_drink()
            case '3' :
                tambah_stock_cosmetik()
            case '4' :
                tambah_stock_soap()
            case '5' :
                tambah_stock_shampoo()
            case '6' :
                break
            case _ :
                input ('Pilih opsi yang telah disediakan. Tekan enter untuk melanjutkan')


# _____________________________________________________________CUSTOMER__________________________________________
def knapsack_01(items, capacity):
    random.shuffle(items)
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Mengisi tabel dp
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1]["price"] <= w:
                dp[i][w] = max(items[i - 1]["price"] + dp[i - 1][w - items[i - 1]["price"]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Menemukan barang yang dipilih
    res = dp[n][capacity]
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            res -= items[i - 1]["price"]
            w -= items[i - 1]["price"]
            if w < 0:  # Pastikan w tidak negatif
                break

    return dp[n][capacity], selected_items

def update_stock(nama_file, selected_items):
    df = baca_csv(nama_file)
    for item in selected_items:
        index = df[df['MEREK'] == item['name']].index[0]
        df.at[index, 'JML'] = df.at[index, 'JML'] - 1
    tulis_csv(df, nama_file)

def merge_sort(arr, primary_key, secondary_key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, primary_key, secondary_key)
        merge_sort(right_half, primary_key, secondary_key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if (left_half[i][primary_key] > right_half[j][primary_key]) or \
               (left_half[i][primary_key] == right_half[j][primary_key] and left_half[i][secondary_key] > right_half[j][secondary_key]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def rekomendasi_barang(nama_file, jenis_barang):
    os.system('cls')
    df = baca_csv(nama_file)

    if df.empty:
        input("Tidak ada data yang dapat diproses. Tekan Enter untuk kembali.")
        return

    try:
        uang_customer = int(input('Masukkan jumlah uang yang dimiliki customer: '))
    except ValueError:
        input("Input tidak valid. Tekan Enter untuk kembali.")
        return

    items = [{"name": row['MEREK'], "price": row['HARGA'], "weight": row['NETTO']} for index, row in df.iterrows()]
    items = [item for item in items if item["price"] <= uang_customer and not pd.isnull(item["weight"])]

    if not items:
        print("Tidak ada barang yang dapat dibeli dengan uang tersebut.")
        input("Tekan Enter untuk kembali.")
        return

    while True:
        os.system('cls')
        max_weight, selected_items = knapsack_01(items, uang_customer)

        selected_items = merge_sort(selected_items, primary_key="price", secondary_key="weight")

        unit = 'gram' if jenis_barang in ['makanan', 'kosmetik', 'Soap'] else 'ml'  # Penyesuaian unit
        print("Barang yang dipilih:")

        total_price = sum(item["price"] for item in selected_items)  # Menghitung total harga dari semua item yang dipilih
        total_weight = sum(item["weight"] for item in selected_items)  # Menghitung total berat dari semua item yang dipilih

        table = []

        for item in selected_items:
            table.append([item["name"], item["price"], item["weight"]])

        print(tabulate(table, headers=["Barang", "Harga (Rp)", f"Berat ({unit})"], tablefmt="fancy_grid"))
        print(f"Total harga: {total_price} Rupiah")
        print(f"Total berat: {total_weight} {unit}")

        print('''
    ||==================================================||
    ||           [1] Generate Ulang                     ||
    ||           [2] Beli semua produk yang tertera     ||
    ||           [3] Kembali                            ||
    ||==================================================||
''')
        pilih = input('Masukkan opsi anda : ')

        match pilih:
            case '1':
                continue
            case '2':
                update_stock(nama_file, selected_items)
                input("Barang berhasil dibeli. Tekan Enter untuk melanjutkan.")
                break
            case '3':
                break
            case _:
                input('Masukkan pilihan sesuai dengan yang telah disediakan. Tekan enter untuk melanjutkan')

    
def knapsack_makanan():
    rekomendasi_barang('Food.csv', 'makanan')

def knapsack_minuman():
    rekomendasi_barang('Drink.csv', 'minuman')

def knapsack_kosmetik():
    rekomendasi_barang('cosmetik.csv', 'kosmetik')

def knapsack_Soap():
    rekomendasi_barang('Soap.csv', 'Soap')

def knapsack_Shampoo():
    rekomendasi_barang('Shampoo.csv', 'Sampo')

def lihat_stok_food():
    df = baca_csv('Food.csv')
    print("Daftar semua Makanan: ")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))
    input('Stok barang berhasil ditampilkan. Tekan enter untuk lanjut')

def lihat_stok_drink():
    df = baca_csv('drink.csv')
    print("Daftar semua Minuman: ")
    tabel = [["ID", "Merk", "Netto(ml)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))
    input('Stok barang berhasil ditampilkan. Tekan enter untuk lanjut')

def lihat_stok_kosmetik():
    df = baca_csv('cosmetik.csv')
    print("Daftar semua Kosmetik: ")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))
    input('Stok barang berhasil ditampilkan. Tekan enter untuk lanjut')

def lihat_stok_sabun():
    df = baca_csv('Shampoo.csv')
    print("Daftar semua Sabun: ")
    tabel = [["ID", "Merk", "Netto(gram)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))
    input('Stok barang berhasil ditampilkan. Tekan enter untuk lanjut')

def lihat_stok_shampo():
    df = baca_csv('Shampoo.csv')
    print("Daftar semua Sampo:")
    tabel = [["ID", "Merk", "Netto(ml)", "Stock", "Harga"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'MEREK'], df.loc[i, 'NETTO'], df.loc[i, 'JML'], df.loc[i, 'HARGA']])
    print(tabulate(tabel, headers="firstrow", tablefmt="fancy_grid"))
    input('Stok barang berhasil ditampilkan. Tekan enter untuk lanjut')

def home_rekomendasi():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
        ||======================================||
        ||      [1] Rekomendasi Makanan         ||
        ||      [2] Rekomendasi Minuman         ||
        ||      [3] Rekomendasi Kosmetik        ||
        ||      [4] Rekomendasi Sabun           ||
        ||      [5] Rekomendasi Sampo           ||
        ||      [6] Kembali                     ||
        ||======================================||
        ''')

        pilih = input('Masukkan pilihan: ')
        if pilih == '1':
            knapsack_makanan()
        elif pilih == '2':
            knapsack_minuman()
        elif pilih == '3':
            knapsack_kosmetik()
        elif pilih == '4':
            knapsack_Soap()
        elif pilih == '5':
            knapsack_Shampoo()
        elif pilih == '6':
            break
        else:
            input('Masukkan opsi sesuai yang diberikan. Tekan Enter untuk melanjutkan.')

def home_Tampilkan_stock():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
        ||======================================||
        ||    Pilih Kategori yang diinginkan :  ||  
        ||      [1] Makanan                     ||
        ||      [2] Minuman                     ||
        ||      [3] Kosmetik                    ||
        ||      [4] Sabun                       ||
        ||      [5] Sampo                       ||
        ||      [6] Kembali                     ||
        ||======================================||
        ''')

        pilih = input('Masukkan pilihan: ')

        if pilih == '1':
            lihat_stok_food()
        elif pilih == '2':
            lihat_stok_drink()
        elif pilih == '3':
            lihat_stok_kosmetik()
        elif pilih == '4':
            lihat_stok_sabun()
        elif pilih == '5':
            lihat_stok_shampo()
        elif pilih == '6':
            break
        else:
            input('Masukkan opsi sesuai yang diberikan. Tekan Enter untuk melanjutkan.')

def home_customer():
    while True :
        os.system('cls')
        print('''
    ||======================================||
    ||       Selamat datang Pelanggan       ||
    ||  Silahkan pilih penggunaan aplikasi: ||
    ||                                      ||
    ||        [1] Lihat Stock Toko          ||
    ||        [2] Rekomendasi               ||
    ||                                      ||
    ||======================================||
    ''')
        pilih = input("Masukkan pilihan anda : ")

        match pilih :
            case '1' :
                home_Tampilkan_stock()
            case '2' :
                home_rekomendasi()
            case '4' :
                break
            case _ :
                input('Masukkan sesuai dengan opsi yang telah disediakan. Tekan enter untuk melanjutkan.')

                
# ____________________________________________________________HOME PAGE_________________________________________

while True :
    os.system('cls')
    print('''
    ||======================================||
    ||      Selamat datang di CekakArta     ||
    ||  Silahkan pilih penggunaan aplikasi: ||
    ||                                      ||
    ||           [1] Admin                  ||
    ||           [2] Pegawai                ||
    ||           [3] Customer               ||
    ||           [4] Akhiri Program         ||
    ||======================================||
    ''')

    pengguna = input('Masukan: ')

    match pengguna:
        case '1':
            while True:
                os.system('cls')
                username = input('Masukkan username: ')
                password = getpass.getpass('Masukkan password: ')

                if autentikasi_admin(username, password):
                    input('Autentikasi berhasil! Tekan enter untuk melanjutkan')
                    print("Berhasil Masuk")
                    home_admin()
                    break
                else:
                    print('Username atau password salah!')
                    print('''
    ||======================================||
    ||           [1] Coba lagi              ||
    ||           [2] Kembali                ||
    ||======================================||
    ''')
                    a = input('Masukan: ')
                    if a == '1':
                        continue
                    elif a == '2':
                        break
                    else:
                        input('Pilihan tidak valid! Kembali ke menu awal')
                        break

        case '2':
            while True:
                os.system('cls')
                username = input('Masukkan username: ')
                password = getpass.getpass('Masukkan password: ')

                if autentikasi_pegawai(username, password):
                    input('Autentikasi berhasil! Tekan enter untuk melanjutkan')
                    print("Berhasil Masuk")
                    home_tambah_stock()
                    break
                else:
                    print('Username atau password salah!')
                    print('''
    ||======================================||
    ||           [1] Coba lagi              ||
    ||           [2] Kembali                ||
    ||======================================||
    ''')
                    a = input('Masukan: ')
                    if a == '1':
                        continue
                    elif a == '2':
                        break
                    else:
                        input('Pilihan tidak valid! Kembali ke menu awal')
                        break
        case '3':
            home_customer()
        case '4':
            break
        case _:
            input('Tolong pilih sesuai dengan tabel yang telah disediakan. Tekan enter untuk melanjutkan')