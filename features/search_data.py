import mysql.connector
from sql_connection import connect_sql
import pandas as pd

menu_search = """
+=============================================+
| 🔎 Menu Cari Data Hewan					 
+=============================================+
[1] Cari berdasarkan Nama Hewan								  
[2] Cari berdasarkan Spesies								  
[3] Cari berdasarkan Status Adopsi (Yes/No)
[4] Back to menu							  
+=============================================+
"""

def search_data():
	try:
		conn = connect_sql()

		if conn.is_connected():
			print("Successfully connecting to MySQL database!")

			cursor = conn.cursor()

			while True:
				print(menu_search)
				input_search = int(input(">>> Pilih Menu search: "))

				if input_search == 1:
					input_nama = input(">>> Masukkan nama hewan yang ingin dicari: ")
					cursor.execute(f"""
							SELECT * 
                            FROM pets 
                            WHERE pet_name LIKE '{input_nama}';
						""")
					results = cursor.fetchall()
					columns = ["pet_id","pet_name","species", "age", "gender", "adopted", "adoption_fee"]
					df = pd.DataFrame(results, columns=columns)
					print(df)
				
				elif input_search == 2:
					input_species = input(">>> Masukkan spesies hewan yang ingin dicari: ")
					cursor.execute(f"""
							SELECT * 
                            FROM pets 
                            WHERE species LIKE '{input_species}';
						""")
					results = cursor.fetchall()
					columns = ["pet_id","pet_name","species", "age", "gender", "adopted", "adoption_fee"]
					df = pd.DataFrame(results, columns=columns)
					print(df)	

				elif input_search == 3:
					input_adopsi = input(">>> Masukkan status adopsi hewan (Yes/No): ")
					cursor.execute(f"""
							SELECT * 
                            FROM pets 
                            WHERE adopted LIKE '{input_adopsi}';
						""")
					results = cursor.fetchall()
					columns = ["pet_id","pet_name","species", "age", "gender", "adopted", "adoption_fee"]
					df = pd.DataFrame(results, columns=columns)
					print(df)			

				elif input_search == 4:
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