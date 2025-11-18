import mysql.connector
from sql_connection import connect_sql
import pandas as pd
import matplotlib.pyplot as plt

menu_visualisasi= """
+=============================================+
| 📈 Menu Visualisasi Data                    
+=============================================+
[1] Bar Chart
[2] Histogram
[3] Back to Menu Utama
+=============================================+
"""

menu_bar_chart="""
+==========================================+
| Bar Chart: Pilih Data
+==========================================+
[1] Jumlah hewan per spesies
[2] Jumlah hewan berdasarkan status adopsi
[3] Kembali
+==========================================+
"""

menu_histogram="""
+==========================================+
| Histogram: Pilih Data
+==========================================+
[1] Distribusi umur hewan
[2] Distribusi biaya adopsi
[3] Kembali
+==========================================+
"""

def visualization_data():
    try:
        conn = connect_sql()

        if conn.is_connected():
            print("Successfully connecting to MySQL database!")

            cursor = conn.cursor()

            while True:
                print(menu_visualisasi)
                input_visualisasi = int(input(">>> Pilih Menu Visualisasi Data: "))

                if input_visualisasi == 1:
                    while True:
                        print(menu_bar_chart)
                        input_barchart = int(input(">>> Pilih menu yang ingin divisualisasikan: "))

                        # Jumlah hewan per spesies
                        if input_barchart == 1:
                            cursor.execute("""
                                SELECT species, COUNT(species) AS jumlah_hewan
                                FROM pets
                                GROUP BY species;
                            """)
                            results = cursor.fetchall()
                            columns = ["Spesies", "Jumlah Hewan"]
                            df = pd.DataFrame(results, columns=columns)

                            plt.bar(df["Spesies"], df["Jumlah Hewan"])
                            plt.title("Distribusi Spesies Hewan")
                            plt.xlabel("Spesies")
                            plt.ylabel("Jumlah Hewan")
                            plt.show()

                        # Jumlah hewan berdasarkan status adopsi
                        elif input_barchart == 2:
                            cursor.execute("""
                                SELECT adopted, COUNT(adopted) AS jumlah
                                FROM pets
                                GROUP BY adopted;
                            """)
                            results = cursor.fetchall()
                            columns = ["Status Adopsi", "Jumlah"]
                            df = pd.DataFrame(results, columns=columns)

                            plt.bar(df["Status Adopsi"], df["Jumlah"])
                            plt.title("Jumlah Hewan Berdasarkan Status Adopsi")
                            plt.xlabel("Status Adopsi (Yes/No)")
                            plt.ylabel("Jumlah Hewan")
                            plt.show()
                        elif input_barchart ==3:
                            break
                        else:
                             print("Opsi tidak tersedia")
#--------------------------------------------------------------------------------------------#
                if input_visualisasi == 2:
                    while True:
                        print(menu_histogram)
                        input_histogram = int(input(">>> Pilih menu yang ingin divisualisasikan: "))

                        # Distribusi umur hewan
                        if input_histogram == 1:
                            cursor.execute("SELECT age FROM pets;")
                            results = cursor.fetchall()
                            ages = [row[0] for row in results]

                            plt.hist(ages, bins=5, edgecolor='black')
                            plt.title("Distribusi Umur Hewan")
                            plt.xlabel("Umur (tahun)")
                            plt.ylabel("Jumlah Hewan")
                            plt.show()

                        # Distribusi biaya adopsi
                        elif input_histogram == 2:
                            cursor.execute("SELECT adoption_fee FROM pets;")
                            results = cursor.fetchall()
                            fees = [row[0] for row in results]

                            plt.hist(fees, bins=5, edgecolor='black')
                            plt.title("Distribusi Biaya Adopsi")
                            plt.xlabel("Biaya Adopsi ($)")
                            plt.ylabel("Jumlah Hewan")
                            plt.show()

                        # Kembali ke menu sebelumnya
                        elif input_histogram == 3:
                            break

                        else:
                            print("Opsi tidak tersedia")
                elif input_visualisasi == 3:
                    break

                else:
                    print("Opsi tidak tersedia, silakan pilih 1 atau 2, dan 3 untuk kembali.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Tutup cursor dan koneksi
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed!")
