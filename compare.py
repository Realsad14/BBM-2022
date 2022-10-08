import sqlite3 as sql


con = sql.connect ('db.sqlite3')

cur = con.cursor()

cur.execute ("SELECT * FROM blood_group " )
for i in cur:
        print(i)

con.close()




































