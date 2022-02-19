import mysql.connector as mysql
from tabulate import tabulate

# insert MySQL Database information here
HOST = "localhost"
DATABASE = ""
USER = "root"
PASSWORD = ""

# connect to the database
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# get server information
print(db_connection.get_server_info())

# get the db cursor
cursor = db_connection.cursor()
# get database information
cursor.execute("select database();")
database_name = cursor.fetchone()
print("[+] You are connected to the database:", database_name)
