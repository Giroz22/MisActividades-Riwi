# - Cuadrado de un numero
def cuadrado():
    # - Se solicita los datos
    try:
        num = int(input("Ingrese un número: "))        
    except:
        print( "\nIngrese un valor valido\n" )
        cuadrado()
        
    # - Se calcula el cuadrado del numero
    cuadrado = pow(num, 2)
    
    # - Se imprime el resultado
    print("El cuadrado de", num, "es", cuadrado)

cuadrado()    