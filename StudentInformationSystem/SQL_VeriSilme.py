import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=UTKU;'
    'DATABASE=OKUL;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

sql_delete_query = "DELETE FROM Bolum WHERE BolumID = ?"

record_id = 10

cursor.execute(sql_delete_query, (record_id,))

conn.commit()

cursor.close()
conn.close()

print(f"ID'si {record_id} olan kayıt silindi.")