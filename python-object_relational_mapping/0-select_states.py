#!/usr/bin/python3
"""Lists all states from the database 'hbtn_0e_0_usa'"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))

    # Extract the command-line arguments
    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to SQL server running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306
        )

        # Create a cursor
        cur = db.cursor()

        # Execute the SQL query to select all states
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        # Close the cursor and database connection
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
