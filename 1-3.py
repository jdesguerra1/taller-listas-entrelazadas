#1.Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#2.Lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Insertar al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
     #4.Recorrido
    def mostrar(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.dato, end=" → ")
            actual = actual.siguiente

        print("null")





def ejecutar_lista():
    lista = ListaEnlazada()

    # Pruebas
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    lista.insertar_final(30)

    lista.mostrar()


