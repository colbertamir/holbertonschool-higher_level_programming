#!/usr/bin/python3
"""
Lists all states from the database 'hbtn_0e_0_usa'
"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit("Usage: {} <mysql_username> <mysql_password> \
                 <database_name>".format(sys.argv[0]))

    # Extract the command-line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to SQL server running on localhost at port 3306
    db = MySQLdb.connect(user=username, passwd=password,
                         db=database_name, host='localhost', port=3306)
    cursor = db.cursor()

    # Execute the SQL query to select all states and order them by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches all rows
    data = cursor.fetchall()

    # Display the results as specified
    for row in data:
        print(row)

    cursor.close()
    db.close()
