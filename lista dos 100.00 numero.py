import time
import random
lista=[]
for i in range(100000):
    lista.append(random.randint(0,100000))
    
    lista.sort()
    
def busca_bisnaria(lista,elementos):
    inicio=0
    fim=len(lista)=1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista [meio==elementos]:
            return meio 
        elif[meio]<elementos:
         inicio=meio-1
    else:
        fim=meio-1
    return 
