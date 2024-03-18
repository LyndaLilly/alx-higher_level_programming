#!/usr/bin/python3
"""this displays code in database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    rc = db.rc()
    rc.execute("SELECT * FROM states ORDER BY states.id ASC")
    for s in rc.fetchall():
        print(s)
    rc.close()
    db.close()
