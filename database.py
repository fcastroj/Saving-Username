import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def init_db():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.database = DB_NAME
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def guardar_nombre(nombre):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO personas (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conn.commit()
    cursor.close()
    conn.close()

def ver_nombres():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")
    for id, nombre in cursor.fetchall():
        print(f"{id}: {nombre}")
    cursor.close()
    conn.close()
