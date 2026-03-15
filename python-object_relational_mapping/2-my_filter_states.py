#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Argumentləri götür
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # DB-ə qoşul
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=database)

    cursor = db.cursor()

    # SQL sorğunu format ilə yarat (holberton tələbi)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
