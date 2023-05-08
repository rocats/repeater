import sqlite3

con = sqlite3.connect("remote.db")
con.row_factory = sqlite3.Row
cursor = con.cursor()

# write
# cursor.execute("INSERT INTO stickers VALUES ('inouenagi', 'xxx', 0)")

# read
rows = cursor.execute("SELECT * FROM stickers;").fetchall()
print([dict(i) for i in rows])

# commit changes
con.commit()
print(con.total_changes)

con.close()
