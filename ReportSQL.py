import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# Consulta SQL para obtener los clientes con más de 3 fallos
query = """
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer, COUNT(*) AS failures
FROM customers c
JOIN campaigns ca ON c.id = ca.customer_id
JOIN events e ON ca.id = e.campaign_id
WHERE e.status = 'failure'
GROUP BY c.first_name, c.last_name
HAVING COUNT(*) > 3;
"""

cursor.execute(query)

results = cursor.fetchall()

print("Clientes con más de 3 fallos:")
for row in results:
    print(f"Cliente: {row[0]}, Fallos: {row[1]}")

cursor.close()
conn.close()