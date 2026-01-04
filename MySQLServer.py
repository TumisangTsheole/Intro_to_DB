import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Establish connection to the MySQL server
        # Update 'user' and 'password' with your MySQL credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database using IF NOT EXISTS to avoid failure if it exists
            # We avoid SELECT or SHOW as per requirements
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection and execution errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure the connection is closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
