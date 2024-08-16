import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=UTKU;'
    'Database=OKUL;'
    'Trusted_Connection=True;'
)

cursor = db.cursor()

cursor.execute('SELECT * FROM Bolum')
Bolum = cursor.fetchall()
for i in Bolum:
    print(i)

sql_insert = """
INSERT INTO Bolum (BolumAdi)
VALUES (?)
"""

values = ('ROKET',)

cursor.execute(sql_insert, values)

db.commit()

db.close()