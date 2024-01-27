import mysql.connector

# Replace these values with your MySQL connection details
host = 'localhost'
user = 'root'
password = ''

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    # If the connection is successful, print a success message
    print("GOOOD Connection !!!! ")

    # Close the connection
    connection.close()

except mysql.connector.Error as err:
    # If an error occurs during the connection attempt, print the error message
    print(f"Error: {err}")