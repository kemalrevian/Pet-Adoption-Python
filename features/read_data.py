import pandas as pd
import mysql.connector
from sql_connection import connect_sql

def read_data():
	try:
		#panggil fungsi connect_sql
		conn = connect_sql()
		# apabila koneksi berhasil
		if conn.is_connected():
			print("Successfully connecting to MySQL database!")

			# membuat object "cursor" untuk eksekusi SQL
			cursor = conn.cursor() 

			# mengeksekusi query		
			cursor.execute("""
				SELECT * 
				FROM Pets;
				""") 
			# mengambil data dari query 
			results = cursor.fetchall()

			columns = ["pet_id","pet_name","species", "age", "gender", "adopted", "adoption_fee"]
			df = pd.DataFrame(results, columns=columns)
			return df

	# menghandle error  
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