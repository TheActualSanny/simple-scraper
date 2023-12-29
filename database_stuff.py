from test import results
import sqlite3

connection = sqlite3.connect('animedata.db')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE data (
#     pos PRIMARY KEY,
#     name text,
#     rating real
# )""")

# for i in results:
#     num = i[0]
#     name = i[1]
#     rating = i[2]
#     with connection:
#         cursor.execute("INSERT INTO data VALUES(?, ?, ?)", (num, name, rating))
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())
connection.close()