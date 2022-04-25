# 19102241 - Ahmad Riau Ardi - S1IF07MM2

import json  # library untuk membaca file json
import time  # library untuk menampilkan format waktu

# deklarasi variable untuk menhitung waktu program
execute_time = time.time()


def mergeSort(data):  # fungsi untuk sorting, parameter data berupa array
    # sorting hanya akan dijalankan jika panjang array > 1
    if len(data) > 1:
        # mengambil index tengah
        indexTengah = len(data)//2
        # L_side berisi array sebanyak 'indexTengah' diambil dari setengah pertama array data
        L_side = data[:indexTengah]
        # R_side berisi array sebanyak 'indexTengah' diambil dari setengah terakhir array data
        R_side = data[indexTengah:]

        # recursive untuk membagi array hingga tidak bisa dibagi 2
        mergeSort(L_side)
        mergeSort(R_side)

        # variabel untuk indexing sisi kiri dan kanan array
        L_count = 0
        R_count = 0

        # untuk index array
        key = 0

        # proses penggabungan data
        while L_count < len(L_side) and R_count < len(R_side):
            # jika jumlah array kiri lebih sedikit dari jumlah array kanan
            if L_side[L_count] < R_side[R_count]:
                # elemen di array L_side dimasukkan ke data index 'key'
                data[key] = L_side[L_count]
                # naikan nilai 'L_count'
                L_count += 1

            # jika jumlah array kanan lebih sedikit dari jumlah array kiri
            else:
                # elemen di array R-side dimasukkan ke data index 'key'
                data[key] = R_side[R_count]
                # naikan nilai 'R_count'
                R_count += 1

            # tambah nilai 'key' dengan 1
            key += 1

        # mengecek jumlah elemen yang tersisa di array kanan dan kiri
        while L_count < len(L_side):
            # data index 'key' diisi elemen L_side index ke 'L_count'
            data[key] = L_side[L_count]
            # tambah nilai L_count dan key sebanyak 1
            L_count += 1
            key += 1

        while R_count < len(R_side):
            # data index 'key' diisi elemen R_side index ke 'R_count'
            data[key] = R_side[R_count]
            # tambah nilai L_count dan key sebanyak 1
            R_count += 1
            key += 1


# untuk menampilkan elemen elemen array data
def printList(data):
    # perulangan sebanyak panjang array data untuk menampilkan elemen array
    for i in range(len(data)):
        print(data[i], end=", ")


# function main
if __name__ == '__main__':
    # memanggil berkas berisi elemen array
    berkas = open("sauce.json")
    # isi dari berkas dimuat ke json_data
    json_data = json.load(berkas)
    # variable untuk menampung isi json_data
    data = []

    # perulangan untuk memasukan isi json ke dalam array 'data'
    for i in json_data['nama']:
        # memasukan nilai 'i' ke dalam array data
        data.append(i)

    print("========================================")
    # menampilkan jumlah data
    print("Jumlah data: ", len(data))
    print("========================================\n")

    # uji coba sorting sebanyak 10 kali untuk melihat seberapa cepat algoritma
    for i in range(10):
        # penampung sementara data
        data_temp = data
        # sorting array
        mergeSort(data_temp)
        # deklarasi variable berisi lama waktu eksekusi program
        hasil_execute = time.time() - execute_time
        # menampilkan waktu eksekusi program
        print("Waktu eksekusi ke-", i+1, " :  %s detik" %
              (round(hasil_execute, 5)))
    print("========================================\n")

    # menampilkan elemen array data sesudah disort
    print("Menampilkan array dengan sorting ", end="\n")

    # memanggil fungsi printList untuk menampilkan isi array data
    print("========================================")
    printList(data_temp)

    print("\n========================================")
    # untuk menjeda program
    input("\nTekan enter")
