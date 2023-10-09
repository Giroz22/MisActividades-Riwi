# - Muestre la tabla de multiplicar del 0 al 10
def imprimirTablaMultiplicar():
    for i in range(11):
        for j in range(1,11):
            print(f'{i} * {j} = {i*j}')          
        print("\n")

imprimirTablaMultiplicar()