import pymongo
import mysql.connector
from mysql.connector import Error

# MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb+srv://akashrathod1433333:q7CKWcPEzdOlojzY@cluster12.jegtg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12")
mongo_db = mongo_client["user_data"]  # replace with your MongoDB database name
mongo_collection = mongo_db["user_history"]  # MongoDB collection name

# MySQL connection details
def create_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # or your MySQL server's IP
            database="Akashdb",  # replace with your MySQL database name
            user="root",  # MySQL username
            password="Akashwini@123"  # MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create user_history table in MySQL
def create_user_history_table(connection):
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        date DATETIME NOT NULL,
        UNIQUE(email, date)
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    print("Table user_history created successfully.")
    cursor.close()

# Insert data into MySQL
def insert_data_into_mysql(connection, email, date):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO user_history (email, date)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE email = email;
    """  # Using ON DUPLICATE KEY UPDATE to avoid inserting duplicate entries
    cursor.execute(insert_query, (email, date))
    connection.commit()
    cursor.close()

# Fetch data from MongoDB and insert into MySQL
def migrate_data_from_mongo_to_mysql():
    mysql_conn = create_mysql_connection()
    if mysql_conn:
        create_user_history_table(mysql_conn)
        
        # Fetch data from MongoDB
        records = mongo_collection.find()
        
        # Insert data into MySQL
        for record in records:
            email = record.get('email')
            date = record.get('date')
            insert_data_into_mysql(mysql_conn, email, date)
        
        print("Data migration from MongoDB to MySQL completed.")
        mysql_conn.close()

# Main script
if __name__ == "__main__":
    migrate_data_from_mongo_to_mysql()