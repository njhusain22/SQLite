# importem 'sqlite3' pere treballar amb bbdd
import sqlite3
db_file = 'database.db'
# S'estableix la conexio amb bbdd
with sqlite3.connect(db_file) as conn:
# S'excuta la consulta
    cursor = conn.cursor()
    cursor.execute("""
                   select * from images
                   """)
# Es recupera el resultat de la consulta                  
    for row in cursor.fetchall():
        name, size, date = row
        print(f'{name} {size} {date}')