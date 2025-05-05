#111. Profundidad mínima del árbol binario
#Fácil
#Temas
#Empresas
#Dado un árbol binario, encuentre su profundidad mínima.

#La profundidad mínima es el número de nodos a lo largo de la ruta más corta desde el nodo raíz hasta el nodo hoja más cercano.

#Nota:  Una hoja es un nodo sin hijos.

 

#Ejemplo 1:


#Entrada: raíz = [3,9,20,null,null,15,7]
# Salida: 2
#Ejemplo 2:

#Entrada: raíz = [2, nulo, 3, nulo, 4, nulo, 5, nulo, 6]
# Salida: 5

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        
class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, dato):
        if self.raiz is None:
            self            
        
    
