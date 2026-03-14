#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided by the user.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma (4 arqument götürürük)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cur = db.cursor()
    
    # .format() istifadə edərək sorğunu qururuq
    # BINARY istifadə edirik ki, həm böyük/kiçik hərf, həm də tam uyğunluq yoxlanılsın
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    
    cur.execute(query)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları təmizləyirik
    cur.close()
    db.close()
