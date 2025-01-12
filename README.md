Server Log Data Extraction and User History Database Update

### Description:
## Problem Statement
This project focuses on extracting, transforming, and analyzing data from a server log file (mbox.txt). 
The main goal is to fetch email addresses and their corresponding dates from the log, clean the data, 
and upload it to a MongoDB collection for further analysis and historical tracking. Additionally, 
the project involves moving the processed data to a MySQL relational database for advanced querying.

## Tools and Technologies Used
- **Python**: Main programming language used.
- **Pandas**: For data cleaning and processing.
- **MongoDB**: For data storage and retrieval.
- **MySQL**: Used as a relational database for storing structured data.


## Approach
1. **Data Extraction & Cleaning**: Used scripts like `extract_emails_and_dates.py` to standardize and clean datasets.
2. **Data Transfer**: Transferred data between MongoDB and MySQL using `Mongoto_Mysql.py`.
3. **Data Analysis**: using `Queries.py` to visualize and analyze the processed data.


## Installation

1. **Clone the repository**:
    ```bash
    git clone "Your repo link" 
    ```
2. **Install dependencies**:
    ```bash
    #pip install  --You can Have To install Below Packages 
pandas==1.5.3          # For data manipulation and analysis
pymongo==4.4.0         # For MongoDB interactions
mysql-connector-python==8.0.32  # For MySQL interactions

    ```
3. **Set up databases**:
    - Install MongoDB and MySQL .
    - Ensure the databases are running and properly configured.
    
4. **Run the project**:
    ```bash
    python Quaries.py
    ```

## Project Structure

|-- extract_emails_and_dates.py    # Python script for email extraction, transformation, and data upload
|--Mongoto_Mysql.py                #Transfers the Data from MongoDB to MySQL
|-- mbox.txt                       # Sample log file containing the server logs
|-- Quaries.py                     # It Has All the queries 
|-- README.md                      # Project documentation

