# 19102241 - Ahmad Riau Ardi - S1IF07MM2

import json  # library untuk membaca file json
import time  # library untuk menampilkan format waktu

# deklarasi variable untuk menhitung waktu program
execute_time = time.time()


def index_terkecil(data, index, n):  # fungsi Return index terkecil
    # data berupa array
    # index untuk nilai index awal
    # n berupa int jumlah elemen array - 1,

    # jika nilai index sama dengan n (elemen terakhir di array)
    if index == n:
        # maka return nilai index
        return index

    # rekursif mencari elemen terkecil dari sisa array yang belum disort
    key = index_terkecil(data, index + 1, n)

    # Return nilai index elemen terkecil jika nilai data[index] < data[key]
    # jika tidak lebih kecil, maka return nilai key
    return (index if data[index] < data[key] else key)


def selectionSort(data, n, index=0):  # fungsi selection sort
    # data berupa array
    # n berupa int jumlah elemen array,
    # index untuk nilai index awal

    # ketika index dan ukuran array sama
    if index == n:
        # return nilai -1
        return -1

    # Memanggil fungsi index_terkecil untuk mencari index elemen
    # yang lebih kecil dari index elemen yang terakhir disort
    key = index_terkecil(data, index, n-1)

    # jika nilai key tidak sama dengan index
    if key != index:
        # menukar elemen data[index] dengan dengan data[key]
        data[key], data[index] = data[index], data[key]

    # memanggil selection sort lagi hingga nilai index == n
    # dengan nilai index + 1 atau index selanjutnya
    selectionSort(data, n, index + 1)


if __name__ == '__main__':
    # memanggil berkas berisi data
    berkas = open("sauce.json")
    # isi dari berkas dimuat ke json_data
    json_data = json.load(berkas)
    # variable untuk menampung isi json_data
    data = []

    # perulangan untuk memasukan isi json ke dalam array 'data'
    for i in json_data['nama']:
        # memasukan nilai 'i' ke dalam array data
        data.append(i)

    print("\n========================================")

    # mengetahui jumlah data pada list
    n = len(data)
    print("Jumlah data : ", n)

    print("\n========================================")

    # uji coba sorting sebanyak 10 kali untuk melihat seberapa cepat algoritma
    for i in range(10):
        # penampung sementara data
        data_temp = data
        # sorting array
        selectionSort(data_temp, n)
        # deklarasi variable berisi lama waktu eksekusi program
        hasil_execute = time.time() - execute_time
        # menampilkan waktu eksekusi program
        print("Waktu eksekusi ke-", i + 1, ":  %s detik" %
              (round(hasil_execute, 5)))
    print("========================================")
    # mencetak output proses selection sort
    print("Data setelah diurutkan : \n")
    # perulangan untuk menampilkan setiap item(nilai) pada array data
    for item in data_temp:
        print(item, end=", ")

    print("\n========================================")
    # untuk menjeda program
    input("\nTekan enter")
