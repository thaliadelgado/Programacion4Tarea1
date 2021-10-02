import sqlite3

con = sqlite3.connect("slang.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS slang
               (palabra text UNIQUE, definicion text)''')

def compruebasiexiste(palabra):
    p = cur.execute("""SELECT EXISTS (SELECT 1 
                                     FROM slang 
                                     WHERE palabra=?
                                     LIMIT 1)""", (palabra, )).fetchone()[0]
    return p

while True:
    print("\n Ingrese el numero  de la opcion que desea \n")
    menuOpt = int(input(" 1 Agrega la nueva palabra \n 2 Editar palabra existente \n 3 Eliminar palabra existente \n 4 Ver listado de las palabras \n 5 Buscar significado de la palabra \n 6 Salir \n"))
    if (menuOpt == 1):
        palabra = input("\n Ingrese la palabra a agregar \n")
        definicion = input("\n por ultimo ingrese la definicion de la palabra \n")

        p = compruebasiexiste(palabra)
        if p == False:

            parametros = (palabra, definicion)
            cur.execute("INSERT INTO slang VALUES (?, ?)", parametros)

            con.commit()

        else:
            print("\n La palabra ya existe. \n")


    elif (menuOpt == 2):
        palabra = input("\n Ingrese la palabra que desea modificar \n")

        nuevaPalabra = input("\n Ingrese el nuevo valor de esta palabra \n")

        definicion = input("\n Ingrese la nueva definicion de la palabra \n")

        parametros = (nuevaPalabra, definicion, palabra)
        p = compruebasiexiste(palabra)


        if p:
           cur.execute("""
           UPDATE slang
           SET palabra = ?,
               definicion= ?
           WHERE palabra = ?;
           """, parametros)
           con.commit()

        else:
             print("No se encontro la palabra, intentelo de nuevo")


    elif (menuOpt == 3):
         palabra = input("\n Ingrese la palabra que desea eliminar \n")
         p = compruebasiexiste(palabra)
         if p:
            cur.execute("""
                    DELETE FROM slang
                    WHERE palabra = ?
                    """, (palabra,))
            con.commit()

         else:
             print("No se encontro la palabra, intentelo de nuevo")

    elif (menuOpt == 4):
         data = cur.execute("""SELECT * FROM slang""")
         i = 1
         for palabra in data:
             print(f"{i}. {palabra[0]}")
             i += 1

    elif (menuOpt == 5):

        palabra = input( "\n Ingrese la palabra que quiera ver su significado \n")
        c = compruebasiexiste(palabra)
        if p:
            data = cur.execute(
                """SELECT * FROM slang WHERE palabra = ?""", (palabra,))
            for palabra in data:
                print(f"\nEl significado es: \n {palabra[1]}")

        else:
            print("No se encontro la palabra, intentelo de nuevo")

    elif (menuOpt == 6):
        break

    else:
        print("\n Esta opcion no es valida, ingrese otra opcion \n")
    con.close()


