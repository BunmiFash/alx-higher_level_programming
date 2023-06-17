#!/usr/bin/python3

"""
A script that lists all states from the
database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Retrieve states
    """
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("""SELECT * FROM states
            ORDER BY states.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
