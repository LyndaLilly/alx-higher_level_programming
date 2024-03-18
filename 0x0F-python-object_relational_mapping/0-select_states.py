#!/usr/bin/python3
"""this displays code in database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    rc = database.rc()
    rc.execute("SELECT * FROM states ORDER BY states.id ASC")
    for s in rc.fetchall():
        print()
    rc.close()
    database.close()
