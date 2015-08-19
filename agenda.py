__author__ = 'mauro'
agenda = [{"apellido": "Perez", "nombre": "Juan", "telefono": "341-156280014", "correo": "mm@hotmail.com"}]


def menu():
    while True:
        print ("Agenda de contactos")
        print ("~~~~~~~~~~~~~~~~~~~")
        print ("")
        print ("1) - Listar contacto")
        print ("2) - Nuevo contacto")
        print ("3) - Actualizar contacto")
        print ("4) - Eliminar contacto")
        print ("0) - Salir")
        print ("")
        opcion = raw_input("Seleccione una opcion: ")
        if opcion not in ("0", "1", "2", "3", "4"):
            print ("La opcion ingresada es invalida")
            continue
        else:
            return int(opcion)


# codificar para que muestre el menu y ejecute la funcion que corresponda
def inicio():
    while True:
        opcion = menu()
        if opcion == 0:
            break
        elif opcion == 1:
            listar_contactos()
        elif opcion == 2:
            nuevo_contacto()
        elif opcion == 3:
            modificar_contacto()
        elif opcion == 4:
            eliminar_contacto()


def mostrar_contacto(contacto):
    print("Apellido: " + contacto["apellido"])
    print("Nombre: " + contacto["nombre"])
    print("Telefono: " + contacto["telefono"])
    print("Correo: " + contacto["correo"])
    print("-" * 40)  # imprime 40 guiones medios


# solicita los datos de contacto, y devuelve un diccionario con los mismos
def solicita_datos_contacto():
    nvo_contacto = {}
    nvo_contacto["apellido"] = raw_input("Ingrese el apellido:")
    nvo_contacto["nombre"] = raw_input("Ingrese el nombre:")
    nvo_contacto["telefono"] = raw_input("Ingrese el telefono:")
    nvo_contacto["correo"] = raw_input("Ingrese el correo:")
    return nvo_contacto


def nuevo_contacto():
    nuevo = solicita_datos_contacto()
    agenda.append(nuevo)
    raw_input("Presiones enter para volver al menu...")


def modificar_contacto():
    contacto_nro = int(raw_input("Ingrese el numero de contacto a modificar: "))
    if contacto_nro in range(0, len(agenda)):
        agenda[contacto_nro]=solicita_datos_contacto()
        print ("Modificado con exito!")
    else:
        print ("El contacto especificado no existe!")


# lista los contactos de la agenda, mostrando su id (posicion dentro de la lista) y datos
def listar_contactos():
    for contacto_nro in range(0, len(agenda)):
        print "ID: ", str(contacto_nro)
        mostrar_contacto(agenda[contacto_nro])


# elimina un contacto de la agenda basandose en la posicion que ocupa dentro de la agenda
def eliminar_contacto():
    contacto_nro = int(raw_input("Ingrese el numero de contacto a eliminar: "))
    if contacto_nro in range(0, len(agenda)):
        agenda.remove(agenda[contacto_nro])



if __name__ == "__main__":
    inicio()    # invocamos a la rutina de inicio del programa

