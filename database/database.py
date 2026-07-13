import sqlite3

DATABASE_NAME ="database/jobs.db"

print("Starting")

print(DATABASE_NAME)	
def create_database():
	print(DATABASE_NAME)

conn=sqlite3.connect(DATABASE_NAME)

print("conn")	

cursor = conn.cursor()

print("STARTING DATABASE CREATION ")

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

conn.commit()
conn.close()

print("Database created successfully")

if __name__ == "__main__":
	create_database()
