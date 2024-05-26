import pandas as pd
from tabulate import tabulate
import os
import random

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def baca_csv(nama_file):
    df = pd.read_csv(nama_file, index_col="id")
    return df

def tulis_csv(df, nama_file):
    df.to_csv(nama_file)

def get_last_id(df):
    if len(df.index) > 0:
        return df.index[-1]
    else:
        return 0

def knapsack_makanan():
    os.system('cls')
    df = baca_csv('Food.csv')

    uang_customer = int(input('Masukkan jumlah uang yang dimiliki customer: '))

    items = [{"name": row['MEREK'], "price": row['HARGA'], "weight": row['NETTO']} for index, row in df.iterrows()]

    # Group items by (price, weight) and select one item randomly from each group
    grouped_items = {}
    for item in items:
        key = (item["price"], item["weight"])
        if key not in grouped_items:
            grouped_items[key] = []
        grouped_items[key].append(item)

    unique_items = [random.choice(group) for group in grouped_items.values()]
    
    capacity = uang_customer
    max_weight, selected_items = knapsack_01(unique_items, capacity)

    print(f"Berat maksimal dari pemilihan barang: {max_weight} gram")
    print("Barang yang dipilih:")

    # Create a table for the selected items
    table = [[item["name"], item["price"], item["weight"]] for item in selected_items]
    print(tabulate(table, headers=["Barang", "Harga (Rp)", "Berat (gram)"], tablefmt="grid"))
    
    input(f"Barang diatas merupakan barang yang anda dapat dengan uang {uang_customer} Rupiah, Tekan enter untuk melanjutkan")

def knapsack_minuman():
    os.system('cls')
    df = baca_csv('Drink.csv')

    uang_customer = int(input('Masukkan jumlah uang yang dimiliki customer: '))

    items = [{"name": row['MEREK'], "price": row['HARGA'], "weight": row['NETTO']} for index, row in df.iterrows()]

    # Group items by (price, weight) and select one item randomly from each group
    grouped_items = {}
    for item in items:
        key = (item["price"], item["weight"])
        if key not in grouped_items:
            grouped_items[key] = []
        grouped_items[key].append(item)

    unique_items = [random.choice(group) for group in grouped_items.values()]
    
    capacity = uang_customer
    max_weight, selected_items = knapsack_01(unique_items, capacity)

    print(f"Berat maksimal dari pemilihan barang: {max_weight} ml")
    print("Barang yang dipilih:")

    # Create a table for the selected items
    table = [[item["name"], item["price"], item["weight"]] for item in selected_items]
    print(tabulate(table, headers=["Barang", "Harga (Rp)", "Berat (ml)"], tablefmt="grid"))
    
    input(f"Barang diatas merupakan barang yang anda dapat dengan uang {uang_customer} Rupiah, Tekan enter untuk melanjutkan")

def knapsack_01(items, capacity):
        n = len(items)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        included_items = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif items[i - 1]["price"] <= w:
                    if items[i - 1]["weight"] + dp[i - 1][w - items[i - 1]["price"]] > dp[i - 1][w]:
                        dp[i][w] = items[i - 1]["weight"] + dp[i - 1][w - items[i - 1]["price"]]
                        included_items[i][w] = included_items[i - 1][w - items[i - 1]["price"]] + [items[i - 1]]
                    else:
                        dp[i][w] = dp[i - 1][w]
                        included_items[i][w] = included_items[i - 1][w]
                else:
                    dp[i][w] = dp[i - 1][w]
                    included_items[i][w] = included_items[i - 1][w]

        return dp[n][capacity], included_items[n][capacity]





while True:
    os.system('cls')

    print('''
    ||======================================||
    ||      [1] Rekomendasi Makanan         ||
    ||      [2] Rekomendasi Minuman         ||
    ||      [3] Kembali                     ||
    ||======================================||
    ''')

    pilih = input('Masukkan pilihan: ')
    match pilih:
        case '1':
            knapsack_makanan()
        case '2':
            knapsack_minuman()
        case '3':
            break
        case _ :
            input('masukkan opsi sesuai yang diberikan. tekan enter untuk melanjutkan')