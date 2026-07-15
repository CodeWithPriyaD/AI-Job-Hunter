import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "jobs.db"

print("Database Manager - Starting")
print(f"Database file path: {DB_FILE}")

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT,
                title TEXT,
                location TEXT,
                description TEXT,
                experience TEXT,
                salary TEXT,
                source TEXT,
                apply_link TEXT,
                posted_date TEXT,
                skills TEXT,
                score INTEGER DEFAULT 0,
                applied INTEGER DEFAULT 0
            )
            """
        )
        self.connection.commit()
        
    def insert_job(self, job):
        self.cursor.execute("""
        INSERT INTO jobs (
            company,
            title,
            location,
            description,
            experience,
            salary,
            source,
            apply_link,
            posted_date,
            skills,
            score,
            applied
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job.company,
            job.title,
            job.location,
            job.description,
            job.experience,
            job.salary,
            job.source,
            job.apply_link,
            job.posted_date,
            ", ".join(job.skills) if isinstance(job.skills, (list, tuple)) else job.skills,
            job.score,
            int(job.applied)
        ))

        self.connection.commit()

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.create_table()
    db_manager.close()

print("Database ready")
			