#TO DO: 
# initialize the database with results so far
# when a new posting comes, figure out how to only receieve relevant postings so
   #the discord doesn't get bombarded
    # the discord cant get hit with results already in the table, only new
# consider making a separate discord server and sqlite table for subcontracting
import sqlite3
import call

def collect():

    results = call.get_sam_opportunities()

    with sqlite3.connect("data.sqlite3") as conn:
        cursor = conn.cursor()

        cursor.execute(
                """CREATE TABLE IF NOT EXISTS solicitations (
                solnum varchar(255) PRIMARY KEY, 
                title varchar(255) NOT NULL, 
                posted varchar(255), 
                deadline varchar(255)
                );"""
            )
        conn.commit()

        for opportunity in results:
            cursor.execute(
                """INSERT OR IGNORE INTO solicitations VALUES(
                ?, ?, ?, ? 
                )""", (opportunity['solicitationNumber'], opportunity['title'], opportunity['postedDate'], opportunity['responseDeadLine'])
            )

        conn.commit()

        cursor.execute(
            """SELECT * from solicitations"""
        )
        rows = cursor.fetchall()
        return rows
