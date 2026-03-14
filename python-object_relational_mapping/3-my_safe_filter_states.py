#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injection.
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
    
    # SQL Injection-dan qorunmaq üçün:
    # 1. %s-i dırnaq (') daxilinə ALMA.
    # 2. Arqumenti execute-un ikinci parametri olaraq (tuple kimi) ötür.
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları bağlayırıq
    cur.close()
    db.close()
