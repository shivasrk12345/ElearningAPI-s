from configparser import ConfigParser
import mysql.connector

config = ConfigParser()
config.read(r"./config.ini")
hostname = config.get('db', 'hostname')
port = config.get('db','port')
database = config.get('db', 'database')
username = config.get('db', 'username')
password = config.get('db', 'password')

def create_connection():
    return mysql.connector.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        passwd=password
    )

def close_connection(con):
    con.close()