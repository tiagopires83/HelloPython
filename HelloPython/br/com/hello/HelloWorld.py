'''
Created on 29 de dez de 2015

@author: tiago.pires
'''


import platform
'''
# Função de soma...código alterado 15/01/16
'''
def soma(a,b):
    print('A soma dos números passados é: ', a+b)


'''
# Retorna tamanho da string passada.
'''
def returnTamanhoString(x):
    
    print("Tamanho da String: ", len(x))
        
    
def printMap():
    lista = [1,2,3,4,5,6,7,8,9,10]
    mapa = {1 : 'Banana', 2 : 'Laranja', 3 : 'Uva', 'Ids' : lista} 
    print("Elementos do dictionary são: ", mapa)   
    

def returnTipo(x):
    print("Tipo: ", type(x))
    

def printNumerosPares(num):
    
    pares = list()
    
    while num >= 0:
        if (num % 2) == 0:
            
            pares.append(num)
        
        num = num - 1
    
    print('Os números pares são: ', pares)

def printPCInformations():
    
    print("Plataforma: ", platform.machine())
    print("Versão: ", platform.version())
    print("Hostname: ", platform.node())
    print("Processador: ", platform.processor())
    print("sistema Operacional: ", platform.system())
    print("Nº de CPU's: ",platform.os.cpu_count())
    
    
    
def printNumerosImpares(num):
    
    impares = list()
    
    while num >= 0:
        if (num % 2) != 0:
            impares.append(num)
            
        num = num - 1
    
    print('Os números ímpares são: ', impares)
            

def verificarNumero(num):
    
    if (num % 2) == 0:
        print('O número passado é par!')
    else:
        print('O número passado é ímpar!')
        

def returnAndCompareItensIguaisDeListas(lista1, lista2):
    
    print('Os ítens em comum as duas listas são:', list(set(lista1).difference(lista2)))        
    

if __name__ == '__main__':
    pass
    variavel = 'Hello World my friend!!!'
    print(variavel)
    a=2
    b=4
    n=10
    soma(a, b)
    printMap()
    printNumerosPares(n)
    printNumerosImpares(n)
    verificarNumero(n)
    
    lista1 = [1,2,3,4,5]
    lista2 = [2,3]

    aba = 'abacate'
    print(aba.split('a', 3))
    
    returnTipo([1,2,3])
    printPCInformations()
    returnAndCompareItensIguaisDeListas(lista1, lista2)
    