#En principi només hem de tenir instalat el Phyton per poder fer els exercicis amb SQLite. 


# PAS1:El primer pas es importar el modul 'sqlite3'per poder treballar amb SQLite'

import sqlite3

# PAS2: En el segon pas sestableix una conexió amb bbdd anomenada'bd1.db'.

 # si la base de dades no existeix, es crearà automaticamment
conexion= sqlite3.connect ("bd1.db")

# PAS3:sexecuta una ordre SQL per crear una taula anomenada 'articles' amb tres camps: 'codi', 'descripcio' i 'preu' 
Si la taula ja existeix, es captura lexcepció 'OperationalError' i es mostra un missatge que la taula ja existeix'.

try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")   

# PAS4:Si no volem la execpcio 'OperationalError' podem modificar la comanda SQL de la taula amb la següent sintaxis:

import sqlite3
conexion=sqlite3.connect("bd1.db")
conexion.execute("""create table if not exists articulos (
                          codigo integer primary key AUTOINCREMENT,
                          descripcion text,
                          precio real
                    )""")

 # PAS5: Finalment es tanca la conexió a bases de dades utilitzant el mètode 'close'

conexion.close()

