#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument.
This script is safe from MySQL injections.
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
    
    # SQL Injection-dan qorunmaq üçün %s yer tutucusundan istifadə edirik
    # Diqqət: Sorğu daxilində %s dırnağa ALINMIR. 
    # Məlumat isə ikinci arqument kimi (tuple formatında) verilir.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Bağlantıları təmizləyirik
    cur.close()
    db.close()
