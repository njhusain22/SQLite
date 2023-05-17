# Implementarem un programa que sol·liciti una "selecció" a la taula "articles" i retorni totes les seves files

# PAS1:El primer pas es importar el modul 'sqlite3'per poder treballar amb SQLite

import sqlite3

# PAS2:En el segon pas sestableix una conexió amb bbdd anomenada'bd1.db'

conexion=sqlite3.connect("bd1.db")

# PAS3:A continuacio, el programa executa una consulta SELECT en la taula "articulos" utilitzant el metode 'execute' de conexio de bbdd.El mètode 'execute' retorna un objecte de la classe 'Cursor', que s'utilitza per recórrer els resultats de la consulta

# La taula selecciona 'codigo', 'descripcion' i 'precio' de la taula "articulos"
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
# PAS4: 5. El programa utilitza un bucle 'for' per recórrer cada fila del resultat de la consulta. Per a cada fila, el programa imprimeix la informació de les columnes 'codi', 'descripcio' i 'preu'

for fila in cursor:
    print(fila)

# PAS 5: Finalment, el programa tanca la connexió a la base de dades utilitzant el mètode 'close'

conexion.close()


