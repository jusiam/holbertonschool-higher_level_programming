#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select states with names starting with 'N'
    query = """
    SELECT * FROM states
    WHERE name LIKE 'N%'
    ORDER BY id ASC;
    """
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
    