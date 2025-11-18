import mysql.connector
from sql_connection import connect_sql
import pandas as pd

menu_statistik = """
+=============================================+
| 📊 Menu Statistik	Data					     
+=============================================+
[1] Rata-Rata umur hewan								  
[2] Rata-rata biaya adopsi								  
[3] Jumlah hewan sudah di adopsi									  
[4] Jumlah hewan belum di adopsi									  
[5] Jumlah hewan tiap spesies							  
[6] Back to menu							  
+=============================================+
"""

def statistik_data():
	try:
		conn = connect_sql()

		if conn.is_connected():
			print("Successfully connecting to MySQL database!")

			cursor = conn.cursor()

			while True:
				print(menu_statistik)
				input_statistik = int(input(">>> Pilih Menu Statistik: "))

				if input_statistik == 1:
					cursor.execute(f"""
							Select avg(age) as Rata_rata_Umur
							from pets
						""")
					results = cursor.fetchone()
					print(f"Rata-rata umur hewan adalah: {results[0]}")
				
				elif input_statistik == 2:
					cursor.execute(f"""
							Select avg(adoption_fee) as Rata_rata_biaya_adopsi
							from pets
						""")
					results = cursor.fetchone()
					print(f"Rata-rata biaya adopsi adalah: ${results[0]}")				

				elif input_statistik == 3:
					cursor.execute(f"""
							Select count(adopted)
							from pets
							where adopted="Yes"
						""")
					results = cursor.fetchone()
					print(f"Jumlah hewan yang sudah diadopsi berjumlah: {results[0]}")

				elif input_statistik == 4:
					cursor.execute(f"""
							Select count(adopted)
							from pets
							where adopted="No"
						""")
					results = cursor.fetchone()
					print(f"Jumlah hewan yang belum diadopsi berjumlah: {results[0]}")

				elif input_statistik == 5:
					cursor.execute(f"""
							Select species, count(species) as jumlah_hewan
							from pets
							group by species
						""")
					results = cursor.fetchall()
					columns = ["Spesies", "jumlah_hewan"]
					df = pd.DataFrame(results, columns=columns)
					print(df)					


				elif input_statistik == 6:
					break
								
				else:
					print("Opsi tidak tersedia, silakan pilih 1–5 atau 6 untuk kembali.")

		
	except mysql.connector.Error as err:
		print(f"Error: {err}")

	# clean-up code (dieksekusi apabila program terjadi error atau pun tidak)
	finally:
			# menghapus objek kursor apabila objek kursor ada
		if 'cursor' in locals() and cursor is not None:
			cursor.close()
		# memutuskan koneksi 
		if 'conn' in locals() and conn.is_connected():
			conn.close()
			print("Connection closed!")