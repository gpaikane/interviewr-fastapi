import mysql.connector
import  os
from dotenv import load_dotenv
load_dotenv()

def connect_to_db(db):
    conn = mysql.connector.connect(
        host=os.environ.get("RDS_HOST"),
        user=os.environ.get("RDS_USER"),
        password=os.environ.get("RDS_PASSWORD"),
        database=db
    )
    return conn

def insert_sql_data(values_dict, table_name, db):
    try:
        conn =  connect_to_db(db)
        cursor = conn.cursor()
        columns = ", ".join(values_dict.keys())
        placeholders = ", ".join(['%s'] * len(values_dict))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(values_dict.values())

        cursor.execute(sql, values)
        conn.commit()  # Important: You need to commit the changes to the database

    except Exception as e:
        conn.rollback()  # Rollback changes in case of an error
        print("Error occurred while adding data to database:", e)

    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


def read_sql_data(query, db):
    try:
        conn = connect_to_db(db)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows
    except Exception as e:
        print("Error occured while reading data from database: ", e)

    finally:
        cursor.close()
        conn.close()

