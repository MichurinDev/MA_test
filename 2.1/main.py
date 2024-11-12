import sqlite3

conn = sqlite3.connect('Test.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS reports
    (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        reward INTEGER,
        created_at TEXT
    )"""
)

cursor.execute("INSERT INTO reports VALUES (1, 1, 100, '2021-01-01')")
cursor.execute("INSERT INTO reports VALUES (2, 1, 150, '2021-01-01')")
cursor.execute("INSERT INTO reports VALUES (3, 2, 200, '2021-02-01')")

conn.commit()

cursor.execute(
    """SELECT user_id FROM reports
    WHERE strftime('%Y', created_at) = '2021'
    GROUP BY user_id
    HAVING MIN(created_at) = MAX(created_at)"""
)

print(cursor.fetchall())

conn.close()
