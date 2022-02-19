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

# create a new database called library
cursor.execute("create database if not exists library")

# use that database 
cursor.execute("use library")
print("[+] Changed to `library` database")

# create a table
cursor.execute("""create table if not exists book (
    `id` integer primary key auto_increment not null,
    `name` varchar(255) not null,
    `author` varchar(255) not null,
    `price` float not null,
    `url` varchar(255)
    )""")
print("[+] Table `book` created")
