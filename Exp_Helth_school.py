import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# MySQL connection details
host = 'localhost'
user = 'root'
password = ''
database = 'wa_open_data'
table = 'students_data'

try:
    # Connect to MySQL
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    # Query to select all columns from the specified table
    query = f"SELECT * FROM {table}"

    # Execute the query and fetch results into a Pandas DataFrame
    df = pd.read_sql(query, conn)

    if not df.empty:
        # Display the first 5 rows of the DataFrame
        print(df.head())

        # Display DataFrame info, describe, and shape
        print(df.info())
        print(df.describe())
        print(df.shape)

        # Plot histogram
        df['Age (years)'].hist()
        plt.title('Histogram of Age Column')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.show()

        # Explore Trends Over Time
        result_over_time = df.groupby('Year')['Result (%)'].mean()
        plt.figure(figsize=(10, 6))
        result_over_time.plot(marker='o', linestyle='-', color='b')
        plt.title('Average Result (%) Over Time')
        plt.xlabel('Year')
        plt.ylabel('Average Result (%)')
        plt.grid(True)
        plt.show()

        # Explore Results by Region
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='Region', y='Result (%)', data=df)
        plt.title('Distribution of Result (%) by Region')
        plt.xlabel('Region')
        plt.ylabel('Result (%)')
        plt.xticks(rotation=45, ha='right')
        plt.show()

        # Correlation Analysis
        correlation_matrix = df.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()

        # Explore Results by Sex and Age
        plt.figure(figsize=(12, 8))
        sns.violinplot(x='Sex', y='Result (%)', hue='Age (years)', data=df, split=True)
        plt.title('Result (%) Distribution by Sex and Age')
        plt.xlabel('Sex')
        plt.ylabel('Result (%)')
        plt.show()

        # Compare Categories
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Category', y='Result (%)', data=df)
        plt.title('Average Result (%) by Category')
        plt.xlabel('Category')
        plt.ylabel('Average Result (%)')
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