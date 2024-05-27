import pandas as pd
from tabulate import tabulate
import os
import random

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def baca_csv(nama_file):
    try:
        df = pd.read_csv(nama_file, index_col="id")
        return df
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
        return pd.DataFrame()

def tulis_csv(df, nama_file):
    df.to_csv(nama_file)

def get_last_id(df):
    if len(df.index) > 0:
        return df.index[-1]
    else:
        return 0

def knapsack_01(items, capacity):
    random.shuffle(items)  # Mengacak urutan item sebelum diproses
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




def rekomendasi_barang(nama_file, jenis_barang):
    os.system('cls' if os.name == 'nt' else 'clear')
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
    else:
        max_weight, selected_items = knapsack_01(items, uang_customer)

        unit = 'gram' if jenis_barang == 'makanan' else 'ml'
        print("Barang yang dipilih:")

        total_price = sum(item["price"] for item in selected_items)  # Menghitung total harga dari semua item yang dipilih
        total_weight = sum(item["weight"] for item in selected_items)  # Menghitung total gram dari semua item yang dipilih
        table = []

        for item in selected_items:
            table.append([item["name"], item["price"], item["weight"]])

        print(tabulate(table, headers=["Barang", "Harga (Rp)", f"Berat ({unit})"], tablefmt="fancy_grid"))
        print(f"Total harga: {total_price} Rupiah")
        print(f"Total berat: {total_weight} {unit}")

        input(f"Barang di atas merupakan barang yang Anda dapatkan dengan uang {uang_customer} Rupiah. Tekan Enter untuk melanjutkan")
      
import time

def knapsack_makanan():
    random.seed(time.time())  # Mengatur biji acak menggunakan waktu saat ini
    rekomendasi_barang('Food.csv', 'makanan')

def knapsack_minuman():
    random.seed(time.time())  # Mengatur biji acak menggunakan waktu saat ini
    rekomendasi_barang('Drink.csv', 'minuman')




while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
        ||======================================||
        ||      [1] Rekomendasi Makanan         ||
        ||      [2] Rekomendasi Minuman         ||
        ||      [3] Kembali                     ||
        ||======================================||
        ''')

        pilih = input('Masukkan pilihan: ')
        if pilih == '1':
            knapsack_makanan()
        elif pilih == '2':
            knapsack_minuman()
        elif pilih == '3':
            break
        else:
            input('Masukkan opsi sesuai yang diberikan. Tekan Enter untuk melanjutkan.')