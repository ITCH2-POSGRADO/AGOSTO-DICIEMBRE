def ArbolBinario(raiz):
    return [raiz, [], []]

def insertarIzquierda(raiz, nuevoValor):
    rama_izquierda = raiz.pop(1)
    if len(rama_izquierda) > 1:
        raiz.insert[1,[nuevoValor, rama_izquierda,[]]]
    else:
        raiz.insert(1,[nuevoValor,[],[]])
    return raiz

def insertarDerecha(raiz, nuevoValor):
    rama_derecha = raiz.pop(2)
    if len(rama_derecha):
        raiz.insert[2,[nuevoValor,[],rama_derecha]]
    else:
        raiz.insert(2,[nuevoValor,[],[]])
    return raiz

arbol = ArbolBinario('A')
insertarIzquierda(arbol,'B' )
insertarDerecha(arbol, 'C')
insertarIzquierda(arbol,'D' )
print(arbol)