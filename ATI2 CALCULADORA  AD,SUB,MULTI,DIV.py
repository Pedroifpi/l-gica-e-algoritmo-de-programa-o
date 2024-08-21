
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b
def multiplica(a,b):
    return a*b
def divisao(a,b):
    if a<0:
        print("não e posivel dividir um numero por zero")
    else:
        return a/b
    
def menu():
    print("degite 1 para soma")
    print("degite 2 para subtracao")
    print("degite 3 para multiplica")
    print("degite 4 para divisão")
    
    
while(True):
    menu()
    opçoa="0"
    a=int(input("degite o primeiro numero:"))
    b=int(input("degite o segundo numero:"))
    opçoa=int(input("escolha uma opção:"))
    if opçoa ==1:
        print(soma (a,b))
    elif opçoa ==2:
        print(subtracao(a,b))
    elif opçoa ==3:
        print(multiplica(a,b))
    elif opçoa == 4:
        print(divisao(a,b))
    elif opçoa == 5:
        break
    else:
        print("opção invalida")
        
        
    

    