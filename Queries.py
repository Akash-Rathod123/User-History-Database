import mysql.connector
from mysql.connector import Error

def execute_query(query):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Akashdb',
            user='root',
            password='Akashwini@123'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            
            # Print the result
            for row in result:
                print(row)
            
    except Error as e:
        print(f"Error executing query: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example: List all unique email addresses
query = "SELECT DISTINCT email FROM user_history;"
execute_query(query)

# Example: Count the number of emails received per day
query = """
SELECT DATE(date) AS email_date, COUNT(*) AS email_count
FROM user_history
GROUP BY email_date
ORDER BY email_date;
"""
execute_query(query)

# Example: Find the first and last email date for each email address
query = """
SELECT email, 
       MIN(date) AS first_email_date, 
       MAX(date) AS last_email_date
FROM user_history
GROUP BY email;
"""
execute_query(query)

# Example: Count the total number of emails from each domain
query = """
SELECT SUBSTRING_INDEX(email, '@', -1) AS domain, COUNT(*) AS email_count
FROM user_history
GROUP BY domain
ORDER BY email_count DESC;
"""
execute_query(query)
