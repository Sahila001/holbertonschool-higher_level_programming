#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cur = db.cursor()
    # 'N' ilə başlayanları seçmək üçün SQL sorğusu
    # BINARY istifadə edirik ki, kiçik 'n' ilə başlayanları götürməsin
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları təmizləyirik
    cur.close()
    db.close()
