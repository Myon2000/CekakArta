import pandas as pd
import os
import getpass
from tabulate import tabulate

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
    netto = int(input('Masukkan netto barang anda                              : '))
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

        if password != password2:
            input("Pastikan password anda telah sama. Tekan enter untuk melanjutkan")
            password =  getpass.getpass("Masukkan password pegawai         : ") 
            password2 = getpass.getpass("Masukkan password yang sama       : ")
            continue
        
        if username in df['username'].values:
            input("Username telah dipakai. Tekan enter untuk melanjutkan")
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
    
    keyword = input("Masukkan Pegawai yang ingin dicari (Kosongkan jika ingin melihat semuanya) : ")

    if keyword == "":
        print("Daftar semua Pegawai:")
        tabel = [["Nama", "Nomor Handphone"]]
        for i in range(len(df)):
            tabel.append([df.loc[i, 'Nama'], df.loc[i, 'nomor_telepon']])
        print(tabulate(tabel, headers="firstrow", tablefmt="grid"))
        input("Semua data telah ditampilkan. Tekan enter untuk melanjutkan")

    else :
        for i in range(len(df)):
            if df.loc[i, 'username'] == keyword:
                os.system('cls')
                print(f"Username ditemukan: {df.loc[i, 'Nama']} \nNomor Handphone: {df.loc[i, 'nomor_telepon']}")
                print(input('Data telah ditampilkan. Tekan enter untuk melanjutkan'))
        return "kosong"
    
def edit_pegawai():
    os.system('cls')
    df = baca_csv('Pegawai.csv')

    # Menampilkan semua anggota
    print("Daftar semua anggota:")
    tabel = [["ID", "Nama Lengkap", "Username", "Alamat", "Nomor Telepon"]]
    for i in df.index:
        tabel.append([i, df.loc[i, 'Nama'], df.loc[i, 'username'], df.loc[i, 'alamat'], df.loc[i, 'nomor_telepon']])
    print(tabulate(tabel, headers="firstrow", tablefmt="grid"))

    id = int(input('Masukkan id Pegawai yang ingin diedit (angka): '))

    # Memastikan id anggota ada
    if id not in df.index:
        input(f'Pegawai dengan id {id} tidak ditemukan!')
        return

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
            case '5' :
                break
            case _:
                input('Pilihan tidak valid! Tekan enter untuk melanjutkan')
                continue

        tulis_csv(df, 'Pegawai.csv')
        input('Berhasil! Tekan enter untuk melanjutkan')
    
def home_admin():
    while True:
        os.system('cls')
        print(f'''
||=====================================||
||      SELAMAT DATANG SANG ADMIN      ||
||                                     ||
||        Silahkan Pilih Opsi :        ||
||                                     ||
||  1. Tambahkan Pegawai               ||
||  2. Cari Pegawai                    ||
||  3. Edit Pegawai                    ||
||  4. Tambahkan Barang                ||
||  5. Kembali ke Menu Utama           ||
||                                     ||
||=====================================||            
''')
        pilih = input("Masukkan Opsi Anda : ")
        match pilih :
            case '1' :
                tambah_pegawai()
            case '2' :
                cari_pegawai()
            case '3' :
                edit_pegawai()
            case '4' :
                home_tambah_barang()
            case '5' :
                break
            case _ :
                input("Masukkan opsi sesuai dengan yang telah disediakan. Tekan enter untuk melanjutkan")


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
# _____________________________________________________________PEGAWAI___________________________________________
print('Masukkan fitur pegawai di sini')
# _____________________________________________________________CUSTOMER__________________________________________
print('masukkan fitur customer')
# _____________________________________________________________HOME PAGE_________________________________________

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
            input("Masukkan Username dan Sandi Pegawai")
            break
        case '3':
            input('Masuk ke Customer')
            break
        case '4':
            break
        case _:
            input('Tolong pilih sesuai dengan tabel yang telah disediakan. Tekan enter untuk melanjutkan')