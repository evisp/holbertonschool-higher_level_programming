#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    connection = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3],
                                charset="utf8")
    cur = connection.cursor()
    stateName = argv[4]
    cmd = """ SELECT cities.name FROM cities INNER JOIN states
    ON cities.state_id = states.id WHERE states.name=%s
    ORDER BY cities.id ASC """
    cur.execute(cmd, (stateName,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    connection.close()
