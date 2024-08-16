import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=UTKU;'
    'DATABASE=OKUL;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

sql_update_query = "UPDATE Bolum SET BolumAdi = ? WHERE BolumID = ?"

new_bolum_adi = 'Elektronik'
record_id = 10

cursor.execute(sql_update_query, (new_bolum_adi, record_id))

conn.commit()

cursor.close()
conn.close()

print(f"ID'si {record_id} olan kayıt güncellendi.")