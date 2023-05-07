import sqlite3
import uuid


def gen_uid():
    return uuid.uuid4().hex[:10]


con = sqlite3.connect("remote.db")
cursor = con.cursor()

# create table
# cursor.execute("create table words (uid text, content varchar(50), count int)";

# write
cursor.execute(
    f"insert into words(uid, content, count) values('{gen_uid()}','屌',0),('{gen_uid()}','嗯',0),('{gen_uid()}','好的',0),('{gen_uid()}','好吧',0),('{gen_uid()}','羨慕',0),('{gen_uid()}','额',0),('{gen_uid()}','hhh',0);"
)

# read
rows = cursor.execute("SELECT * FROM words").fetchall()
print(rows)
print(con.total_changes)

# commit changes
con.commit()
con.close()
