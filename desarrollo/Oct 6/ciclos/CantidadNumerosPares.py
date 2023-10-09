# - Problema: Escribe un programa que muestre cuantos numeros pares hay del 4 al 200
def contarNumPares(numInicio, numFinal):
    numPares = 0
    for num in range(numInicio, numFinal+1):
        if (num % 2 == 0):
            numPares += 1        
            
    print(f'Hay {numPares} numeros pares del {numInicio} al {numFinal}')
    
contarNumPares(4, 200)
            