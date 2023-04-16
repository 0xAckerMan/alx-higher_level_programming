#!/usr/bin/python3
'''
Filter states by user
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(hostname='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s   ORDER BY ASC",
                   (argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
