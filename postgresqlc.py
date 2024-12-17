import psycopg2

# Replace with your PostgreSQL connection details
host = "localhost"  # or the IP address or domain of your PostgreSQL server
dbname = "postgres"
user = "postgres"
password = "mysecretpassword"
port = "5432"  # default PostgreSQL port

try:
    # Establish the connection
    connection = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT current_user;")
    result = cursor.fetchone()
    print("Connected as:", result[0])

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print("Error connecting to PostgreSQL database:", error)
