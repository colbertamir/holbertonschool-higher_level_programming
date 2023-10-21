#!/usr/bin/python3
"""Lists all states from the database 'hbtn_0e_0_usa'"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if there are 3 command-line arguments
    if len(sys.argv) != 4:
        sys.exit("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to SQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    cur = db.cursor()
    
    # Execute the SQL query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
