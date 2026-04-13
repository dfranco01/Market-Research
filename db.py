#TO DO: create table with columns of API parameters we care about
# initialize the database with results so far
# when a new posting comes, figure out how to only receieve relevant postings so
   #the discord doesn't get bombarded
    # the discord cant get hit with results already in the table, only new
# consider making a separate discord server and sqlite table for subcontracting
import sqlite3
import call

results = call.get_sam_opportunities()
if results:
    pass

with sqlite3.connect("data.sqlite3") as conn:
    cursor = conn.cursor()

    cursor.execute(
            """CREATE TABLE IF NOT EXISTS projects (
            solnum INTEGER PRIMARY KEY, 
            title text NOT NULL, 
            posted DATE, 
            deadline DATE
            );"""
        )
    conn.commit()

    #The '?' will allow call data to be inserted into the db
    #Insert or Ignore will prevent duplicate entries being added
    #cursor.rowcount could be used to only send new data to Discord 
    
    
    print("success")