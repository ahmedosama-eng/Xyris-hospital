import sqlite3
import pandas as pd

from db_model import *


def insert_data(conn):
    """
    Inserts data from the Excel file into the database tables.
    """
    cursor = conn.cursor()

    # Read the Excel file
    excel_file = r"F:\xyris test\xyris_HIS_test\data\Xyris HIS_data.xlsx"
    physicians_df = pd.read_excel(excel_file, sheet_name='Physicians')
    schedules_df = pd.read_excel(excel_file, sheet_name='Schedules')
    specialities_df = pd.read_excel(excel_file, sheet_name='Specialities')
    pricelist_df = pd.read_excel(excel_file, sheet_name='Pricelist')
    policy_df = pd.read_excel(excel_file, sheet_name='Policy')

    # Insert data into Physicians table
    for _, row in physicians_df.iterrows():
        cursor.execute('''
            INSERT INTO Physicians (name, speciality, degree)
            VALUES (?, ?, ?)
        ''', (row['Name'], row['Speciality'], row['Degree']))

    # Insert data into Schedules table
    for _, row in schedules_df.iterrows():
        cursor.execute('''
            INSERT INTO Schedules (doctor_name, monday, tuesday, wednesday, thursday, friday, saturday, sunday)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['Doctor Name'], row['Monday'], row['Tuesday'], row['Wednesday'], row['Thursday'], row['Friday'], row['Saturday'], row['Sunday']))

    # Insert data into Specialities table
    for _, row in specialities_df.iterrows():
        cursor.execute('''
            INSERT INTO Specialities (speciality_name, definition)
            VALUES (?, ?)
        ''', (row['Speciality Name'], row['Definition']))

    # Insert data into Pricelist table
    for _, row in pricelist_df.iterrows():
        cursor.execute('''
            INSERT INTO Pricelist (service_name, price_usd)
            VALUES (?, ?)
        ''', (row['Service Name'], row['Price (USD)']))

    # Insert data into Policy table
    for _, row in policy_df.iterrows():
        open_date = str(row['Open Date'])  
        cursor.execute('''
            INSERT INTO Policy (name, policy_description, address, landline, open_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (row['Name'], row['Policy Description'], row['Address'], row['Landline'], open_date))


    conn.commit()

def main():
    # Define the database path
    db_path = get_db_path(db_name='hospital.db', output_dir=r'F:\xyris test\xyris_HIS_test\data\output_db')

    # Create a connection to the database
    conn = create_connection(db_path)

    # Create tables
    create_tables(conn)

    # Insert data
    insert_data(conn)

    # Close the connection
    conn.close()

    print(f"Database created successfully at: {db_path}")

if __name__ == '__main__':
    main()