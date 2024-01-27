import mysql.connector

# MySQL connection details
host = 'localhost'
user = 'root'
password = ''
database = 'wa_open_data'
table_name = 'rank_school_top100'

# Create a MySQL connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor
cursor = connection.cursor()

# Define the new data types for each column
new_data_types = {
    '2020_Rank': 'INT',
    'Median_ATAR': 'FLOAT',
    'No_eligible_Yr_12_students': 'INT',
    'No_Students_with_an_ATAR': 'INT',
    'Perc_students_with_an_ATAR': 'FLOAT',
    'Socio_Economi_Status': 'INT',
    'State_Overall_Score': 'INT',
    'Better_Education_Percentile': 'FLOAT',
    'English': 'INT',
    'Maths': 'INT',
    'Total_Students': 'INT',
}

# Iterate over columns and change data types
for column, data_type in new_data_types.items():
    query = f"ALTER TABLE {table_name} MODIFY COLUMN {column} {data_type}"
    cursor.execute(query)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()