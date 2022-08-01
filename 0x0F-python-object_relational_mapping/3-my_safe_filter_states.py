#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    data_base = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3],
                                charset="utf8")
    cur = data_base.cursor()
    search = argv[4]
    cmd = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(cmd, (search,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    data_base.close()
