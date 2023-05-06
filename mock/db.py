import sqlite3

con = sqlite3.connect("remote.db")
cursor = con.cursor()

# create table
# cursor.execute("CREATE TABLE main (country TEXT, code TEXT)")

# write
# cursor.execute("INSERT INTO main VALUES ('Japan', 'JP')")
# cursor.execute("INSERT INTO main VALUES ('China', 'CN')")
# cursor.execute("INSERT INTO main VALUES ('USA', 'US')")

# read
rows = cursor.execute("SELECT country, code FROM main").fetchall()
print(rows)
print(con.total_changes)

# delete
# query = """
# DROP TABLE IF EXISTS main;
# """
# cursor.execute(query)

# commit changes
con.commit()

con.close()
