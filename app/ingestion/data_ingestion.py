import sqlite3
import pandas as pd
 
 
def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def fetch_joined_data(conn):
    query = """
        SELECT 
            Physicians.name AS doctor_name,
            Physicians.speciality AS doctor_speciality,
            Specialities.definition AS speciality_definition,
            Physicians.degree AS doctor_speciality_degree,
            Schedules.friday AS friday_doctors_Schedule,
            Schedules.saturday AS saturday_doctors_Schedule,
            Schedules.sunday AS sunday_doctors_Schedule,
            Schedules.monday AS monday_doctors_Schedule,
            Schedules.tuesday AS tuesday_doctors_Schedule,
            Schedules.wednesday AS wednesday_doctors_Schedule,
            Schedules.thursday AS thursday_doctors_Schedule
        FROM Physicians
        JOIN Schedules
        ON Physicians.name = Schedules.doctor_name
        JOIN Specialities
        ON Specialities.speciality_name = Physicians.speciality
    """
    df = pd.read_sql_query(query, conn)
    return df

def fetch_data_from_table(conn, table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    return df


def process_pricelist_data(pricelist_df):
    
    return pricelist_df

def process_policy_data(policy_df):
    
    return policy_df

def retrieve_and_process_data(db_path):

    conn = get_db_connection(db_path)
    doctor_view_df=fetch_joined_data(conn)
    pricelist_df = fetch_data_from_table(conn, 'Pricelist')
    policy_df = fetch_data_from_table(conn, 'Policy')

    conn.close()
    # Return the processed data
    return {
        'doctor_view_df' : doctor_view_df,
        'pricelist': pricelist_df,
        'policy': policy_df,
    }

 
# '''
# if __name__ == '__main__':
#     # Example usage
#     db_path = r'F:\xyris test\xyris_HIS_test\app\data\output_db\hospital.db'
#     processed_data = retrieve_and_process_data(db_path)

#     for key, df in processed_data.items():
#         print(f"Processed {key} data:")
#         print(df.head())
#         print("\n")


#         '''