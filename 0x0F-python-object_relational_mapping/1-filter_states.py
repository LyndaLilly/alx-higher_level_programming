#!/usr/bin/python3
"""
this executes all states with capital letters
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    rc = db.cursor()
    rc.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = rc.fetchall()
    for row in rows:
        print(row)
    rc.close()
    db.close()
