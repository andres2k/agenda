__author__ = 'mauro'
agenda = [{"apellido": "Perez", "nombre": "Juan", "telefono": "341-156280014", "correo": "mm@hotmail.com"}]


class Contacto(object):
    def __init__(self, apellido="", nombre="", telefono="", correo=""):   # al poner = algo, si no viene el parametro toma ese valor por defecto
        self.apellido=apellido
        self.nombre=nombre
        self.telefono=telefono
        self.correo=correo

    def validar(self):
        if not self.nombre or "".__eq__(self.nombre):
            return False, "El nombre no puede estar vacio"
        if not self.apellido or "".__eq__(self.apellido):
            return False, "El apellido no puede estar vacio"
        if not self.telefono or "".__eq__(self.telefono):              # ver de meter expresion regular
            return False, "El telefono no puede estar vacio"
        if not self.correo or self.correo=="":                      # ver de meter expresion regular
            return False, "El correo no puede estar vacio"

    def to_txt(self):
        return ",".join((self.nombre, self.apellido, self.telefono, self.correo))

    def __str__(self):
        return ("Apellido: %s \n"
                "Nombre: %s \n"
                "Telefono: %s \n"
                "Correo: %s \n") % (self.apellido,
                                    self.nombre,
                                    self.telefono,
                                    self.correo)


class Repositorio(object):
    def __init__(self, filename="agenda.db"):
        self.filename = filename
        self.db = []
        self.__load()

    def __load(self):
        try:
            archivo = open(self.filename, "r")
        except:
            print("No se pudo abrir el archivo")
        else:
            for linea in archivo.readlines():
                linea = linea.rstrip("\n").split(",")
                self.db.append(Contacto(linea[0], linea[1], linea[2], linea[3]))    # No es tan pythonico
            archivo.close()

    def __store(self):
        try:
            archivo = open(self.filename, "w")
        except:
            print ("No se pudo abrir el archivo")
        else:
            for contacto in self.db:
                archivo.writelines(contacto.to_txt()+"\n")
            archivo.close()

    def save(self, contacto):
        self.db.append(contacto)

    def find(self, campo, valor):
        # otra forma seria:
        # 2.- Esta es la recomendada
        # return [x for x in self.db if getattr(x, campo).lower() == valor.lower()]
        return filter(lambda x: getattr(x, campo)==valor, self.db)   # la function getattr(<objeto>, <atributo>) nos devuelve el valor del atributo en el objeto
                                                                     # similar a objeto.atributo

    def list(self):
        return self.db

    def delete(self, contacto):
        self.db.remove(contacto)

    def close(self):
       # self.__store(filename=self.filename)        # por que manda esto????
        self.__store()


class Agenda(object):
    def __init__(self):
        self.db = Repositorio(filename="agenda.txt")    # porque aca es agenda.txt y el init de Repo por default
                                                        # recibe agenda.db????

    def __mostrar_lista(self, lista):
        for item in lista:
            print(str(item) + "\n")

    def __solicita_datos(self, contacto):
        print ("Datos del contacto")
        print ("~~~~~~~~~~~~~~~~~~")
        contacto.apellido = raw_input("Apellido [%s]: " % contacto.apellido)    # para que sirve el [%s] dentro de un string???
        contacto.nombre = raw_input("Nombre [%s]: " % contacto.nombre)          # creo que se usa asi para mostrar los datos del contacto
        contacto.telefono = raw_input("Telefono [%s]: " % contacto.telefono)    # en el caso de la modificacion
        contacto.correo = raw_input("Correo [%s]: " % contacto.correo)
        return contacto

    def __buscar(self):
        campo = raw_input("Ingrese el criterio de busqueda [nombre|apellido|telefono|correo]:")
        if campo in ("nombre", "apellido", "telefono", "correo"):
            valor = raw_input("Ingrese el %s del contacto: " % campo)
            contactos = self.db.find(campo, valor)
            if not [].__eq__(contactos):
                return contactos
        return []

    def menu(self):
        while True:
            print ("Agenda de contactos")
            print ("~~~~~~~~~~~~~~~~~~~")
            print ("")
            print ("1) - Listar contacto")
            print ("2) - Nuevo contacto")
            print ("3) - Actualizar contacto")
            print ("4) - Eliminar contacto")
            print ("5) - Buscar contacto")
            print ("0) - Salir")
            print ("")
            opcion = raw_input("Seleccione una opcion: ")
            if opcion not in ("0", "1", "2", "3", "4", "5"):
                print ("La opcion ingresada es invalida")
                continue
            else:
                return int(opcion)

    def inicio(self):
        while True:
            {1: self.listar,
             2: self.nuevo,
             3: self.modificar,
             4: self.eliminar,
             5: self.buscar,
             0: self.salir}.get(self.menu()     # nos devuelve un numero del 0 al 5
                                )()             #el diccionario, segun el numero nos da un nombre de funcion, luego con el () lo invocamos.

    def listar(self):
        self.__mostrar_lista(self.db.list())

    def buscar(self):
        contactos = self.__buscar()
        if len(contactos) == 0:
            print ("No se encontraron contactos con ese criterio de busqueda")
        else:
            self.__mostrar_lista(contactos)

    def nuevo(self, contacto=None):
        _contacto = self.__solicita_datos(contacto or Contacto())       # esto verifica q si es none genera uno???
        res, msj = _contacto.validar()
        if not res:
            print msj
        else:
            self.db.save(_contacto)                                     # por que usa _contacto? Es local?

    def modificar(self):
        contactos = self.__buscar()
        if len(contactos) != 1:
            raw_input("Se han encontrado uno o mas contactos"           # por que entrada???
                      "para el criterio de busqueda especificado")
        else:
            contacto = contactos[0]
            self.db.delete(contacto)
            self.nuevo(contacto=contacto)                               # para "modificar", se crea un nuevo, que en realidad es el mismo pero
                                                                        # pudiendo modificar los valores.

    def eliminar(self):
        contactos = self.__buscar()
        if len(contactos) > 0:
            for contacto in contactos:
                self.db.delete(contacto)
            raw_input("Se eliminaron %d contactos." % len(contactos))
        else:
            raw_input("No se encontraron contactos para el criterio de busqueda especificado")

    def salir(self):
        self.db.close()
        print ("Saliendo...")
        exit()

if __name__ == "__main__":
    agenda = Agenda()
    agenda.inicio()


