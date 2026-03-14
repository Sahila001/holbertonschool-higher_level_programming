#!/usr/bin/python3
"""
Fix: SQL query-də dırnaq və sıralama dəqiqliyi
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Bağlantı zamanı arqumentlərin sırasına və portun integer olmasına bax
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    # Ştat adını '{}' dırnaqları daxilinə alırıq
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(sys.argv[4]))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    cur.close()
    db.close()
