# importem 'sqlite3' pere treballar amb bbdd
import sqlite3
db_filename = 'database.db'
# Es defeneix la funcio y mostra els valors en taules d'imatges 
    def display_table(conn):
        cursor = conn.cursor()
        cursor.execute('select name, size, date from images;')
        for name, size, date in cursor.fetchall():
            print(name, size, date)
# S'obra una nova conexio en bbdd
with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    display_table(conn1)
# S'executa una consulta per insertar valors en taula d'imatges
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into images (name, size, date)
    values ('JournalDev.png', 2000, '2020-02-20');
    """)
# Mostra el contingut de la taula
    print('\nAfter changes in conn1:')
    display_table(conn1)
# Mostra el contingut abans de fer els canvis
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Commit from the first connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)
# Afegim un altre registre a la taula
    cursor1.execute("""
    insert into images (name, size, date)
    values ('Hello.png', 200, '2020-01-18');
    """)
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Revert to changes before conn1's commit
    conn1.rollback()
# Mostra els valors de la taula despres del rollback
    print('\nAfter connection 1 rollback:')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)
