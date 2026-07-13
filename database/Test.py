import sqlite3

print("Starting")

conn = sqlite3.connect("database/jobs.db")

cursor =conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS jobs(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		company TEXT,
		title TEXT,
		location TEXT,
		experience TEXT,
		salary TEXT,
		source TEXT,
		apply_link TEXT,
		posted_date TEXT,
		skills TEXT,
		score INTEGER DEFAULT 0,
		applied INTEGER DEFAULT 0
	)
""")	

print("Database created successfully")

conn.commit()
print("Changes committed")	

conn.close()

print("Finished")


