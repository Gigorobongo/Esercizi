# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:12:50 2024

@author: Andrea
"""

class Nodo:
    def _init_(self, key=None, next=None):
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

# A = [1,2,3,4,5]
# p = crea(A)