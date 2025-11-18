from features.read_data import read_data
from features.add_data import add_data
from features.delete_data import delete_data
from features.update_data import update_data
from features.statistik_data import statistik_data
from features.search_data import search_data
from features.visualization import visualization_data

run = True
menu = """
+=============================================+
| 🐾 SELAMAT DATANG DI PUSAT ADOPSI HEWAN! 🏡 |
+=============================================+

|============== 📖 MENU UTAMA ===============|
|                                            |
|[1] Tampilkan semua data hewan              |
|[2] Menambahkan data hewan                  |
|[3] Hapus data hewan                        |
|[4] Perbarui data hewan                     |
|[5] Statistik Hewan                         |
|[6] Cari data hewan                         |
|[7] Visualisasi                             |
|[8] exit                                    |
+=============================================+
"""

while run:
    print(menu)
    input_user = int(input(">>> Masukkan Angka Pilihan Anda:  "))
    if input_user == 1:
        data = read_data()
        print(data)

    elif input_user == 2:
        data = add_data()
        print(data)

    elif input_user == 3:
        data = delete_data()
        print(data)

    elif input_user == 4:
        data = update_data()
        print(data)
    
    elif input_user == 5:
        data = statistik_data()
        print(data)
    elif input_user == 6:
        data = search_data()
        print(data)
    elif input_user == 7:
        data = visualization_data()
        print(data)
    
    elif input_user == 8:
        print("Exit program...")
        run=False
    else:
        print("😺 Oops! Menu yang kamu pilih tidak tersedia \nSilakan masukkan angka sesuai menu yang tersedia")