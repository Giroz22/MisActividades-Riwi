# - Problema: Hayar el area de un triangulo
def calcularAreaTriangulo():
    
    # - Se solicita los datos
    try:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
    except:
        print( "\nIngrese un valor valido\n" )
        calcularAreaTriangulo()

    # - Se calcula el area del triangulo        
    area = (base * altura) / 2
    
    # - Se imprime el area del triangulo
    print( "El area del triangulo es:", area )
        
calcularAreaTriangulo()