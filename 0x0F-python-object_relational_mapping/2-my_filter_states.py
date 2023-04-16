#!/usr/bin/python3
'''
Filter states by user
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cursor = db.cursor()
    command = """SELECT id, name
    FROM states
    WHERE name LIKE BINARY '{}'
    ORDER BY id ASC""", format(argv[4])
    cursor.execute(command)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
