import mysql.connector
import pandas as pd

# MySQL connection details (for root user without a password)
host = 'localhost'
user = 'root'
password = ''
database = 'WA_OPEN_DATA'

# Establish a connection to MySQL server
with mysql.connector.connect(
    host=host,
    user=user,
    password=password
) as connection:
    with connection.cursor() as cursor:
        # Create or use the specified database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        cursor.execute(f"USE {database}")

        # Path to the first CSV file
        
        # csv_file_path = r'C:\Users\efilh\OneDrive\Documentos\PROJECT_18\Data_CSV\Cycle_Routes.csv'
        # name_tb="cycle_routes_data"

        csv_file_path = r'C:\Users\efilh\OneDrive\Documentos\PROJECT_18\Data_CSV\Rank_school_top100_12to22.csv'
        name_tb="rank_school_top100"

        #csv_file_path = r'C:\Users\efilh\OneDrive\Documentos\PROJECT_18\Data_CSV\WA_school_list.csv' 
        #name_tb="wa_school_list"



        # Read the first CSV file into a DataFrame with the correct delimiter
        df1 = pd.read_csv(csv_file_path, delimiter=';')

        # Remove spaces from column names
        df1.columns = [col.replace(' ', '_') for col in df1.columns]

        # Convert columns to string if needed
        for col in df1.columns:
            if df1[col].dtype != 'object':
                df1[col] = df1[col].astype(str)

        # Define a function to map pandas data types to MySQL data types
        def get_mysql_data_type(pandas_data):
            if pandas_data.dtype == 'int64':
                return 'INT'
            else:
                return 'TEXT'

        # Extract column names and data types from the DataFrame
        columns_and_types1 = ', '.join([
            f'`{col}` {get_mysql_data_type(df1[col])}'
            for col in df1.columns.tolist()
        ])

        # Create the first table
        create_table_query1 = f"""
        CREATE TABLE IF NOT EXISTS {name_tb} (
            {columns_and_types1}
        )
        """

        try:
            cursor.execute(create_table_query1)

            # Insert data from the first CSV file into the first MySQL table
            for index, row in df1.iterrows():
                insert_query = f"""
                INSERT INTO {name_tb} ({', '.join([f'`{col}`' for col in df1.columns])}) 
                VALUES ({', '.join(['%s'] * len(df1.columns))})
                """
                cursor.execute(insert_query, tuple(row))

            # Commit the changes to the database
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            # Rollback the changes in case of an error
            connection.rollback()