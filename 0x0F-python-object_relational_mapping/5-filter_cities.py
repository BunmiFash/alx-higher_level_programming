#!/usr/bin/python3

"""
A script that takes in a state as argument and
lists all cities from the state
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
            """SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id ASC
            """, (argv[4],))

    states = cur.fetchall()
    if states is not None:
        print(", ".join([state[0] for state in states]))

    cur.close()
    db.close()
