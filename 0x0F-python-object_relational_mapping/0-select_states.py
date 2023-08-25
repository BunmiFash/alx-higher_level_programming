#!/usr/bin/python3

"""
A script that lists all states from the database
hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost", port=3306, user="root",
            passwd="Oluwabunmi12.", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute(
            """SELECT *
                FROM states
                ORDER BY states.id
            """)
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
