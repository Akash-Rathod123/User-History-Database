import re
from datetime import datetime
import pymongo
from pymongo import MongoClient

# Task 1: Extract Email Addresses and Dates
def extract_emails_and_dates(file_path):
    emails_and_dates = []
    
    # Regular expression pattern for email and date
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    date_pattern = r'\b[A-Za-z]{3}, \d{1,2} [A-Za-z]{3} \d{4} \d{2}:\d{2}:\d{2}\b'
    
    with open(file_path, 'r') as file:
        for line in file:
            # Check for an email in the line
            email_match = re.search(email_pattern, line)
            
            # Check for a date in the line
            date_match = re.search(date_pattern, line)
            
            if email_match and date_match:
                email = email_match.group()
                date_str = date_match.group()
                
                # Convert the date string to a Python datetime object
                try:
                    date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S')
                except ValueError:
                    date_obj = None
                
                # Add to the list if both email and date are found
                if email and date_obj:
                    emails_and_dates.append((email, date_obj))
    
    return emails_and_dates

# Task 2: Data Transformation
def transform_data(extracted_data):
    # Transform the date to 'YYYY-MM-DD HH:MM:SS' format
    transformed_data = [(email, date.strftime('%Y-%m-%d %H:%M:%S')) for email, date in extracted_data]
    return transformed_data

# Task 3: Save Data to MongoDB
def save_to_mongodb(data):
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://akashrathod1433333:q7CKWcPEzdOlojzY@cluster12.jegtg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster12")
    
    # Use the user_data database and user_history collection
    db = client['user_data']
    collection = db['user_history']
    
    # Insert the transformed data into MongoDB
    for email, date in data:
        record = {
            'email': email,
            'date': date
        }
        collection.insert_one(record)

    print("Data inserted successfully into MongoDB.")

if __name__ == "__main__":
    # File path to the log file (mbox.txt)
    file_path = r'C:\Users\DELL\Downloads/mbox.txt'
    
    # Step 1: Extract Email Addresses and Dates
    extracted_data = extract_emails_and_dates(file_path)
    
    # Step 2: Transform the extracted data
    transformed_data = transform_data(extracted_data)
    
    # Step 3: Save transformed data to MongoDB
    save_to_mongodb(transformed_data)
