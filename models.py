import pyodbc

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost\sqlexpress;"
            "Database=AED;"
            "UID=AED;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()
#cursor.execute("SELECT @@VERSION as version")

cursor.execute("SELECT lugar from Sala_Lugar")

while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.lugar)