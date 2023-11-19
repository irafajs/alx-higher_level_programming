#!/usr/bin/python3
"""
Shebang to create a python script
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ prevent the code to run when imported"""
    if len(sys.argv) != 5:
        sys.exit(1)
    uname, pword, dtbs = sys.argv[1], sys.argv[2], sys.argv[3]
    value = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost", port=3306, user=uname, passwd=pword, db=dtbs)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states WHERE name = '{value}' ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
