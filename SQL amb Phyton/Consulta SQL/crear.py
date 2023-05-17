# importem 'sqlite3' pere treballar amb bbdd
import sqlite3
# definim la funcio per comprobarn si la bbdd existeix
import os
def check_db(filename):
    return os.path.exists(filename)
# Posem noms als arxius per bbdd i SQL
db_file = 'database.db'
schema_file = 'schema.sql'
# Si existeix un arixiu de bbdd, sortim del programa
if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)
# Si no existeix l'arxiu en el programa, s'obra l'arxiu de SQL i es llegeix el seu contingut
with open(schema_file, 'r') as rf:
    # Read the schema from the file
    schema = rf.read()
# Es crea una conexio amb bbdd 
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    # Execute the SQL query to create the table
    conn.executescript(schema)
# S'inserten alguns valors de la taula d'imatges
    print('Created the Table! Now inserting')
    conn.executescript("""
                       insert into images (name, size, date)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07');
                       """)
    print('Inserted values into the table!')
#Es tanca la conexio en bbdd
print('Closed the connection!')
   
