#!/usr/bin/env python3
 
# Autor: Diego Fernando Marin
# Programa: ordenamiento.py
# Fecha: Sat Oct 3 07:51:18 COT 2015
# Descripcion: este programa ordena una lista por distintos metodos
 
import random, time
 
def aleatorios(n):
    """ (numero) -> (lista, lista, lista)
 
   retorna una lista de n numeros para cada caso: azar, ordenado, inverso
 
   """
    ordenado = list(range(0,n))
    azar = ordenado.copy()
    inverso = ordenado.copy()
    random.shuffle(azar)
    inverso.reverse()
    return (azar, ordenado, inverso)
 
def test(metodo, azar, ordenado, inverso):
    """ (funcion, lista, lista, lista) -> None
   
   Prueba el metodo de ordenamiento con una lista de tamano n
   
   """
    def prueba(metodo, lista):
        copia = lista.copy()
        ini = time.clock() # guarda la hora de inicio
        metodo(copia)
        fin = time.clock() # guarda la hora final
        return fin - ini
    t_azar = prueba(metodo, azar)
    t_ordenado = prueba(metodo, ordenado)
    t_inverso = prueba(metodo, inverso)
    print("{} ({}) : {:f}, {:f}, {:f}".format(metodo.__name__, n, t_azar, t_ordenado, t_inverso))
 
# Metodos de Ordenamiento
 
def insercion(lista):
    """ (lista) -> None
   
   ordena la lista por el metodo de insercion (Insertion)
   http://www.sorting-algorithms.com/insertion-sort
   
   >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
   >>> insercion(lista)
   >>> lista
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   """
    for i in range(1, len(lista)):
        k = i
        while k > 0 and lista[k] < lista[k-1]:
            # intercambia lista[k] y lista[k-1]
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k-=1 # es igual a k=k-1
 
def seleccion(lista):
    """ (lista) -> None
   
   ordena la lista por el metodo de seleccion (Selection)
   http://www.sorting-algorithms.com/selection-sort
   
   >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
   >>> seleccion(lista)
   >>> lista
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   """
    n = len(lista)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if lista[j] < lista[k]:
                k = j
        # intercambia lista[i] y lista[k]
        lista[i], lista[k] = lista[k], lista[i]    
 
def burbuja(lista):
    """ (lista) -> None
   
   ordena la lista por el metodo de burbuja (Bubble)
   http://www.sorting-algorithms.com/bubble-sort
   
   >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
   >>> burbuja(lista)
   >>> lista
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   """
    n = len(lista)
    for i in range(0, n):
        swapped = False
        j = n - 1
        while j > i:
            if lista[j] < lista[j-1]:
                # intercambia lista[j] y lista[j-1]
                lista[j], lista[j-1] = lista[j-1], lista[j]
                swapped = True
            j -= 1
        if not swapped: break
 
def shell(lista):
    """ (lista) -> None
   
   ordena la lista por el metodo de shell (Shell)
   http://www.sorting-algorithms.com/shell-sort
   
   >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
   >>> shell(lista)
   >>> lista
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   """
    tam = len(lista)
    inc=1
    for inc in range(1,tam,inc*3+1):
        while inc>0:
            for i in range(inc,tam):
                j=i
                temp=lista[i]
                while j>=inc and lista[j-inc]>temp:
                    lista[j]=lista[j-inc]
                    j=j-inc
                lista[j]=temp
            inc=inc//2
# Pruebas
def quick(lista):
    
    """ (lista) -> None
   
   ordena la lista por el metodo de quick (Quick)
   http://www.sorting-algorithms.com/quick-sort
   
   >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
   >>> quick(lista)
   >>> lista
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   
   """    
    i=izq
    j=der
    x=lista[(izq + der)/2]
 
    while( i <= j ):
        while lista[i]<x and j<=der:
            i=i+1
        while x<lista[j] and j>izq:
            j=j-1
        if i<=j:
            aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
            i=i+1;  j=j-1;
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
 

# Programa Principal
for n in [100, 1000,10000]:
    azar, ordenado, inverso = aleatorios(n)
    #test(insercion, azar, ordenado, inverso)
    #test(seleccion, azar, ordenado, inverso)
    #test(burbuja, azar, ordenado, inverso)
    #test(shell, azar, ordenado, inverso)
    #test(merge, azar, ordenado, inverso)
    #test(heap, azar, ordenado, inverso)
    test(quick, azar, ordenado, inverso)