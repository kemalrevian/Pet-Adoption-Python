import mysql.connector
from sql_connection import connect_sql

def delete_data():
	try:
		conn = connect_sql()

		if conn.is_connected():
			print("Successfully connecting to MySQL database!")

			cursor = conn.cursor()
			input_hapus = int(input(">>> Masukkan ID hewan yang ingin di hapus: "))	

			cursor.execute(f"""
				DELETE FROM Pets
				WHERE pet_id = {input_hapus}
			""")
			conn.commit()
			return f"Data dengan ID {input_hapus} Berhasil dihapus!"

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