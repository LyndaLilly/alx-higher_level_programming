#!/usr/bin/python3
"""
this accept an argument to show all entries in
"states" table of hbtn_0e_0_usa where name hits the provided.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    rc = db.cursor()
    rc.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = rc.fetchall()
    for row in rows:
        print(row)
    rc.close()
    db.close()
