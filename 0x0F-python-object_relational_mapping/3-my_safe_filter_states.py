#!/usr/bin/python3
'''
List all states where name matches the arg. No sqli
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    command = '''SELECT id, name
                FROM states
                WHERE name=%s
                ORDER BY id ASC'''
    cur.execute(command, (sys.argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
