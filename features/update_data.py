import mysql.connector
from sql_connection import connect_sql


menu_perbarui_kolom = """
+=============================================+
| Pilih Kolom yang ingin di perbarui [1-6]    |
+=============================================+
[1] Pet Name								  
[2] Species								  
[3] Age									  
[4] Gender									  
[5] Adopted								  
[6] Adoption Fee
[7] Back to menu							  
+=============================================+
"""

def update_data():
	try:
		conn = connect_sql()

		if conn.is_connected():
			print("Successfully connecting to MySQL database!")

			cursor = conn.cursor()
			input_update = int(input(">>> Pilih ID hewan yang ingin di perbarui: "))
			

			while True:
				print(menu_perbarui_kolom)
				input_update_kolom = int(input("Kolom mana yang ingin di perbarui? \n>>> Masukkan indexnya:  "))

				if input_update_kolom == 1:
					update_nama = input(">>> Masukkan nama baru: ")
					cursor.execute(f"""
						UPDATE Pets
						SET pet_name = "{update_nama}"
						WHERE pet_id = {input_update}
					""")
					

				elif input_update_kolom == 2:
					update_spesies = input(">>> Masukkan spesies baru: ")
					cursor.execute(f"""
						UPDATE Pets
						SET species = "{update_spesies}"
						WHERE pet_id = {input_update}
					""")
								
					
				elif input_update_kolom == 3:
					update_umur = input(">>> Masukkan umur baru (tahun): ")
					cursor.execute(f"""
						UPDATE Pets
						SET age = {update_umur}
						WHERE pet_id = {input_update}
					""")
					

				elif input_update_kolom == 4: 
					update_gender = input(">>> Masukkan gender baru (Male/Female): ")
					cursor.execute(f"""
						UPDATE Pets
						SET gender = "{update_gender}"
						WHERE pet_id = {input_update}
					""")
						

				elif input_update_kolom == 5:
					update_adopsi = input(">>> Masukkan status adopsi (Yes/No): ")
					cursor.execute(f"""
						UPDATE Pets
						SET adopted = "{update_adopsi}"
						WHERE pet_id = {input_update}
					""")
								

				elif input_update_kolom == 6:
					update_harga_adopsi = input(">>> Masukkan harga adopsi baru ($): ")
					cursor.execute(f"""
						UPDATE Pets
						SET adoption_fee = {update_harga_adopsi}
						WHERE pet_id = {input_update}
					""")

				elif input_update_kolom == 7:
					break
							
				else:
					print("Opsi tidak tersedia, silakan pilih 1–6 atau 7 untuk kembali.")

			conn.commit()
			# return f"Data Berhasil di Update!"
		
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