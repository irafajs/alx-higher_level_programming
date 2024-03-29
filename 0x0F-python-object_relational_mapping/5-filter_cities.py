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
    query = (
            "SELECT  c.name FROM cities c JOIN states s "
            "ON c.state_id = s.id WHERE s.name LIKE BINARY %s ORDER BY c.id;")
    cursor.execute(query, (value,))
    rows = cursor.fetchall()
    if not rows:
        print()
    else:
        city_names = [row[0] for row in rows]
        print(", ".join(city_names))
    cursor.close()
    db.close()
