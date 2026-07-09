import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="bank_db",
    user="postgres",
    password="*******"
)
cur = conn.cursor()

query = "SELECT * FROM employees;"
cur.execute(query)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
