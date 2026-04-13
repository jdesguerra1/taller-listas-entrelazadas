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

    # Mostrar lista
    def mostrar(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.dato, end=" → ")
            actual = actual.siguiente

        print("null")

    # Buscar elemento
    def buscar(self, dato):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente

        return False

    # Eliminar primer elemento
    def eliminar_inicio(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return

        eliminado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        print(f"Elemento {eliminado} eliminado del inicio")

    # Eliminar por valor
    def eliminar_por_valor(self, dato):
        actual = self.cabeza
        anterior = None

        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Elemento no encontrado")
            return

        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

        print(f"Elemento {dato} eliminado")

    # Tamaño de la lista
    def tamaño(self):
        contador = 0
        actual = self.cabeza

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

    # Invertir lista
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente

        self.cabeza = anterior

    def ordenar(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return  

        cambio = True

        while cambio:
            cambio = False
            actual = self.cabeza
            anterior = None

            while actual.siguiente:
                siguiente = actual.siguiente

                if actual.dato > siguiente.dato:

                    cambio = True

                    if anterior is None:
                        self.cabeza = siguiente
                    else:
                        anterior.siguiente = siguiente
                    actual.siguiente = siguiente.siguiente
                    siguiente.siguiente = actual

                    # Mover punteros
                    anterior = siguiente
                else:
                    anterior = actual
                    actual = actual.siguiente




def ejecutar_lista():
    lista = ListaEnlazada()

    # Pruebas
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    lista.insertar_final(30)

    lista.mostrar()
    

