# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:10:03 2024

@author: Andrea
"""

import tree


class Nodo:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next
    
def crea(A):
    if A == []:
        return None
    p = Nodo(A[0])
    q = p
    for i in range(1, len(A)):
        q.next = Nodo(A[i])
        q = q.next
    return p




'''
Esercizio 3 (10 punti): Si consideri un albero binario radicato
T, i cui nodi abbiano un campo val contenente un intero e i
campi left e right con i puntatori ai figli. Un nodo v dell’albero
si dice valido se si verificano le seguenti tre condizioni:
- v ha entrambi i figli;
- il campo val di uno dei due figli è minore di quello padre;
- il campo val dell’altro figlio è maggiore di quello del padre.
Ad esempio nell’ albero in figura ci sono esattamente 2 nodi
validi (quelli con valore 6 e 2).
'''

def es(p):
    count = 0
    if p == None: return 0
    if p.left and p.right:
        if p.left.value < p.value < p.right.value or p.right.value < p.value < p.left.value:
            count += 1
        count += es(p.left)
        count += es(p.right)
    return count

root = tree.BinaryTree.fromList([7, [3, [2, [9, None, None], [1, None, None]], [1, None, None]], [6, [8, [4, [5, None, None], [6, None, None]], [3, None, None]], [5, [10, None, None], None]]])
# print(es(root))


'''
Esercizio 3 (10 punti): Abbiamo una lista a puntatori contenente nodi
con campo chiave contenente interi e vogliamo
sapere il valore massimo ed il valore minimo delle chiavi dei
nodi della lista.
Ad esempio per la lista a puntatori in figura la risposta è la
coppia di interi 9 e −4.
'''

def es2(p):
    if p == None: 
        return None, None
    if p.next == None:
        return p.key, p.key
    
    a, b = es2(p.next)

    return max(a, p.key), min(b, p.key)

# A = [1,8,-4,9,-2,2]
# p = crea(A)   
# print(es2(p))    



'''
Esercizio 3 (10 punti):
Dato un albero binario non vuoto a valori interi T ed un suo
nodo v, il costo del cammino radice-v è definito come la somma
2
dei valori dei nodi nel percorso che va dalla radice al nodo v
(estremi inclusi).
Vogliamo calcolare il costo del massimo cammino radicefoglia di T.
Ad esempio nell’albero binario in figura, la risposta è 18, infatti
nell’albero sono presenti quattro diversi cammini radice-foglia
di costo 3, 18, 11 e −70, rispettivamente.
'''





'''
Ritornare il numero di nodi che hanno 2 figli e valore pari
'''

def es3(p, count = 0):
    if p == None: return 0
    if p.left and p.right:
        if p.value % 2 == 0:
            count+=1
        count += es3(p.left)
        count += es3(p.right)
    return count

print(es3(root))














