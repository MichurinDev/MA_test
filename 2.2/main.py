import sqlite3

conn = sqlite3.connect('Test.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE pos
    (
        id INTEGER PRIMARY KEY,
        title TEXT
    );
""")

cursor.execute("""
    CREATE TABLE reports
    (
        id INTEGER PRIMARY KEY,
        barcode TEXT,
        price REAL,
        pos_id INTEGER,
        FOREIGN KEY (pos_id) REFERENCES pos(id)
    );
""")
conn.commit()

cursor.execute("INSERT INTO pos (id, title) VALUES (1, 'Item 1');")
cursor.execute("INSERT INTO reports (id, barcode, price, pos_id) VALUES (1, '123456', 10.0, 1);")
cursor.execute("INSERT INTO reports (id, barcode, price, pos_id) VALUES (2, '123456', 10.0, 1);")
conn.commit()

cursor.execute(
    """
    SELECT
        p.title,
        r.barcode,
        r.price
    FROM 
        pos p
    JOIN 
        reports r ON p.id = r.pos_id
    GROUP BY 
        p.title, r.barcode, r.price
    HAVING 
        COUNT(*) > 1;
    """
)

print(cursor.fetchall())

conn.close()
