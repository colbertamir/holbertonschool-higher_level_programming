#!/usr/bin/python3
"""Lists all states from the database 'hbtn_0e_0_usa'"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
        
        try:
            # Connect to SQL server running on localhost at port 3306
            db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name, port=3306)
            cur = db.cursor()
            # Execute the SQL query to select all states and order them by id
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            cur.close()
            db.close()
        except MySQLdb.Error as e:
            print("MySQL Error: {}".format(e))
