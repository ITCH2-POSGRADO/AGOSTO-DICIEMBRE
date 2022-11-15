#Arboles binarios
class ArbolBinario():
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
    def insertarIzquierdo(self, Nodo):
        if self.izquierdo == None:
            self.izquierdo = ArbolBinario(Nodo)
        else:
            arbol = ArbolBinario(Nodo)
            arbol.izquierdo = self.izquierdo
            self.izquierdo = arbol
    def insertarDerecho(self, Nodo):
        if self.derecho == None:
            self.derecho = ArbolBinario(Nodo)
        else:
            arbol = ArbolBinario(Nodo)
            arbol.derecho = self.derecho
            self.derecho = arbol
    def getRaiz(self):
        return self.raiz
    def getIzquierdo(self):
        return self.izquierdo
    def getDerecho(self):
        return self.derecho
    def setRaiz(self, nuevoValor):
        self.valor = nuevoValor

arbol = ArbolBinario('A')
arbol.insertarIzquierdo('B')
arbol.insertarDerecho('C')

print(arbol.getDerecho())