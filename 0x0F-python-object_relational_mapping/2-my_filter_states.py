#!/usr/bin/python3

"""
A script that takes in an argument and
displays all values in the state table
from the database hbtn_0e_0_usa that
matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
            """SELECT *
                FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC
            """.format(argv[4]))
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
