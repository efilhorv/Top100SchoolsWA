import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# MySQL connection details
host = 'localhost'
user = 'root'
password = ''
database = 'wa_open_data'
table = 'cycle_routes_data'

try:
    # Connect to MySQL
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    # Query to select all columns from the specified table
    query = f"SELECT * FROM {table}"

    # Execute the query and fetch results into a Pandas DataFrame
    df = pd.read_sql(query, conn)

    if not df.empty:
        # Display basic statistics
        print(df.describe(include='all'))

        # Visualize Route Counts by Asset Owner
        plt.figure(figsize=(12, 8))
        sns.countplot(x='ASSET_OWNER', data=df)
        plt.title('Route Counts by Asset Owner')
        plt.xlabel('Asset Owner')
        plt.ylabel('Route Count')
        plt.xticks(rotation=45, ha='right')
        plt.show()

        # Visualize Route Classification Distribution
        plt.figure(figsize=(12, 8))
        sns.countplot(x='CLASSIFICATION', data=df)
        plt.title('Route Classification Distribution')
        plt.xlabel('Classification')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.show()

        # Visualize Infrastructure Type Distribution
        plt.figure(figsize=(12, 8))
        sns.countplot(x='INFRASTRUCT_TYPE', data=df)
        plt.title('Infrastructure Type Distribution')
        plt.xlabel('Infrastructure Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.show()

        # Visualize Route Status Distribution
        plt.figure(figsize=(12, 8))
        sns.countplot(x='STATUS', data=df)
        plt.title('Route Status Distribution')
        plt.xlabel('Status')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.show()

        # Visualize Program Distribution
        plt.figure(figsize=(12, 8))
        sns.countplot(x='PROGRAM', data=df)
        plt.title('Program Distribution')
        plt.xlabel('Program')
        plt.ylabel('Count')
        plt.xticks(rotation=45, ha='right')
        plt.show()

    else:
        print("No data found.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()