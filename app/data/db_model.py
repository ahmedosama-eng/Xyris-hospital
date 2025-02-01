import sqlite3
import pandas as pd
import os

def get_db_path(db_name='hospital.db', output_dir='data'):
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, db_name)

def create_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Physicians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            speciality TEXT NOT NULL,
            degree TEXT NOT NULL
        )
    ''')

    # Schedules Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_name TEXT NOT NULL,
            monday TEXT,
            tuesday TEXT,
            wednesday TEXT,
            thursday TEXT,
            friday TEXT,
            saturday TEXT,
            sunday TEXT
        )
    ''')

    # Specialities Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Specialities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            speciality_name TEXT NOT NULL,
            definition TEXT NOT NULL
        )
    ''')

    # Pricelist Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pricelist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_name TEXT NOT NULL,
            price_usd REAL NOT NULL
        )
    ''')

    # Policy Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Policy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            policy_description TEXT NOT NULL,
            address TEXT NOT NULL,
            landline TEXT NOT NULL,
            open_date TEXT NOT NULL
        )
    ''')

    conn.commit()

