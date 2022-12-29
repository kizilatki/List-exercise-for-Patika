"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir.

"""

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l1 = []                                   # We should create an empty list as l1 or different names

def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            l1.append(i)

flatten(l)
print(l1)

