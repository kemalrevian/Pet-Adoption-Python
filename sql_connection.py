import mysql.connector
from dotenv import load_dotenv        
import os 

# load semua environment varible dari file .env
load_dotenv()

def connect_sql():
	# definisikan kredensial dari environment
	user_name = os.environ.get("MYSQL_USERNAME")
	password = os.environ.get("MYSQL_PASSWORD")
	database = os.environ.get("DB_NAME")

	# membuat koneksi ke MySQL server
	conn = mysql.connector.connect(
			host="localhost",
			user=user_name,
			password=password,
			database=database,
			)
	return conn
