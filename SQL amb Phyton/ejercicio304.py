'Ara implementarem un programa que insereix unes quantes files a la taula "articles" de la base de dades "bd1" que acabem de crear amb el programa anterior'

# PAS1:El primer pas es importar el modul 'sqlite3'per poder treballar amb SQLite

import sqlite3

# PAS2:En el segon pas sestableix una conexió amb bbdd anomenada'bd1.db'

conexion=sqlite3.connect("bd1.db")

# PAS3: En aquest pas sutilitzen  3 trucades el metode 'execute' per inserir 3 files a la taula articles. Cada fila té 2 valors: descripcio i preu, els valors es passen com un tupla al segon argument del metode 'execute'

# La primera trucada insereix una fila de taronges amb un preu de 23,50
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
# La segona trucada insereix una fila de peras amb un preu de 34
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
# La tercera trucada insereix una fila de bananas amb un preu de 25
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))

# PAS4: En aquest pas es truca el 'commit' per desar els canvis a les bases de dades.

conexion.commit()

# PAS5: Finalment es tanca la conexió a bases de dades utilitzant el mètode 'close'

conexion.close()

