import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("DELETE FROM ocean_data")

conn.commit()
conn.close()

print("All ocean data cleared")