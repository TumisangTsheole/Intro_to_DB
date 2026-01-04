import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        # Replace 'your_username' and 'your_password' with your actual credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        cursor = connection.cursor()

        # Create database if it doesn't exist
        # We do not use SELECT or SHOW statements here
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Specific error handling for MySQL connection/execution issues
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Handle closing of the database/connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
