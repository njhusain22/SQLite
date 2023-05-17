# Implementarem un programa que demanarà un preu i després ens mostrarà una descripció de tots els articles que costen menys que el preu que hem introduït

# PAS1:El primer pas es importar el modul 'sqlite3'per poder treballar amb SQLite

import sqlite3

# PAS2:En el segon pas sestableix una conexió amb bbdd anomenada'bd1.db

conexion=sqlite3.connect("bd1.db")

# PAS3: Sol·licitem a lusuari que ingressi un preu'

precio=float(input("Ingrese un precio:"))

# PAS4:Executem una consulta SQL per recuperar totes les files de la taula "articles" que tenen un preu inferior al preu ingressat per l'usuari

cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))

# PAS5: Fem servir el mètode 'fetchall' per recuperar totes les files que compleixen la condició

filas=cursor.fetchall()

# PAS6: Verifiquem si la llista de files no és buida

if len(filas)>0:
    for fila in filas:
        print(fila)
# Si la llista és buida, imprimim un missatge indicant que no hi ha files que compleixin la condició
else:
    print("No existen artículos con un precio menor al ingresado.")

# PAS7: Tanquem la connexió a la base de dades

conexion.close()

