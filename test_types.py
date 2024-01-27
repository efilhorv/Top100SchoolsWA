import pandas as pd
import mysql.connector

# CSV file path
csv_file_path = r'C:\Users\Jose\Documents\PROJECT_18\Data_CSV\Rank_school_top100_12to22.csv'

# MySQL connection details
host = 'localhost'
user = 'root'
password = ''
database = 'wa_open_data'
table = 'rank_school_top100'

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(csv_file_path)

# Display data types of columns in the CSV file
print("CSV File Data Types:")
print(df_csv.dtypes)

# Connect to MySQL
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

# Execute a query to describe the table
query = f"DESCRIBE {table}"
cursor.execute(query)

# Fetch the results and display data types of columns in the MySQL table
results = cursor.fetchall()
print("\nMySQL Table Data Types:")
for row in results:
    print(f"{row[0]}: {row[1]}")

# Close the cursor and connection
cursor.close()
conn.close()