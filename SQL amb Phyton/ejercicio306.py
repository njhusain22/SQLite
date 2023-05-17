# Implementarem un programa que demanarà un codi de producte i després ens mostrarà la seva descripció i preu

# PAS1:El primer pas es importar el modul 'sqlite3'per poder treballar amb SQLite

import sqlite3

# PAS2:En el segon pas sestableix una conexió amb bbdd anomenada'bd1.db

conexion=sqlite3.connect("bd1.db")

# PAS3: A continuació, el programa sol·licita a l'usuari que introdueixi el codi d'un article utilitzant la funció 'input' de Python. El valor ingressat es converteix en un enter utilitzant la funció 'int'
 
codigo=int(input("Ingrese el código de un artículo:"))

#PAS4: El programa executa una consulta SELECT a la taula 'articles' utilitzant el mètode 'execute' de la connexió de la base de dades. La consulta selecciona les columnes 'descripcio' i 'preu' de la taula d'articles' on el codi d'article és igual al valor ingressat per l'usuari

# El mètode 'execute' retorna un objecte de la classe 'Cursor', que s'utilitza per recórrer els resultats de la consulta
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))

# PAS5: El programa utilitza el mètode 'fetchone' de l'objecte 'Cursor' per recuperar la primera fila dels resultats de la consulta.

fila=cursor.fetchone()
# Si no hi ha files que coincideixin amb el codi ingressat, el mètode 'fetchone' retorna 'None'.
if fila!=None:
# Si el mètode 'fetchone' torna una fila, el programa imprimeix la informació de les columnes 'descripcio' i 'preu' de la fila utilitzant la funció 'print'
    print(fila)
# Si no hi ha files que coincideixin amb el codi ingressat, el programa imprimeix un missatge que indica que no s'ha trobat cap article amb aquest codi
else:
    print("No existe un artículo con dicho código.")

# PAS6:El programa tanca la connexió a la base de dades utilitzant el mètode 'close'

conexion.close()





