import pandas as pd
import mysql.connector
from sql_connection import connect_sql

def add_data():
	try:
		conn = connect_sql()

		if conn.is_connected():
			print("Successfully connecting to MySQL database!")

			cursor = conn.cursor()
			# input_ID_hewan = int(input(">>> Masukkan ID Hewan: "))
			input_Name = input(">>> Masukkan nama hewan: ")
			input_species = input(">>> Masukkan Spesies hewan: ")
			input_Age = int(input(">>> Masukkan Umur hewan (Tahun): "))
			input_gender = input(">>> Masukkan jenis kelamin hewan (Male/Female): ")
			input_adopted = input(">>> Masukkan Status adopsi (Yes/No): ")
			input_adoption_fee = int(input(">>> Masukkan harga untuk adopsi ($): "))		

			cursor.execute(f"""
				INSERT INTO Pets (pet_name, species,age,gender, adopted, adoption_fee)
				VALUES ("{input_Name}","{input_species}","{input_Age}","{input_gender}","{input_adopted}","{input_adoption_fee}")
			""")
			conn.commit()
			return f"Data Berhasil ditambahkan!"
		
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