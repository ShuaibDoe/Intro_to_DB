import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (not a specific DB yet)
        connection = mysql.connector.connect(
            host="localhost",       # Replace with your host
            user="root",   # Replace with your MySQL username
            password="Doeshuaib@24" # Replace with your MySQL password
        )

        cursor = connection.cursor()
        
        # CREATE DATABASE IF NOT EXISTS (doesn't fail if it already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

    finally:
        # Clean up
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
