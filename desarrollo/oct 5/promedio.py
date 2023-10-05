# - Problema: Encontrar el promedio de minimo 7 numeros
def calcularPromedio(minIteracion):
    
    # - Variables   
    valores = []
    numIteraciones = minIteracion
    
    # - Iteramos el minimo de veces que se ingresen en el parametro "minIteracion" para obtener los valores 
    while numIteraciones != 0:           
        valores = guardarValor(valores)
        numIteraciones -= 1 
    
    # - Preguntamos si el usuario desea agregar mas valores  
    valores = agregarMasValores(valores)        
    
    # - Calculamos el promedio
    promedio = sum(valores) / len(valores)
    
    print("\nEl promedio de los numeros ingresados es:", promedio, "\n")

# - Solicita un valor entero y lo almacena en la lista que se pide como parametro   
def guardarValor(valores):
    try:
        valores.append(int(input("Ingrese un valor:\n")))
        return valores
    except:
        print( "\nIngrese un valor valido\n" )
        calcularPromedio()

# - Iteramos hasta que el usuario no desee agregar mas valores       
def agregarMasValores(valores):
    while True:        
        # - Validamos si el usuario desea agregar mas numeros y si selecciona la opcion correcta
        while True:            
            try:
                opc = int(input("Desea agregar otro valor?: \n1.Si\n2.No\n"))
                
                # - Validamos que opc no sea diferente de 1 o 2
                if(opc < 1 and opc > 2):
                    print("Ingrese un valor valido")
                    continue
                break           
            except:
                print( "\nIngrese un valor valido\n" )
                continue
        
        # - Si el ususario desea ingresar otro valor se piden los datos                                                          
        if opc == 1:
            valores = guardarValor(valores) 
            continue          
        else:  
            return valores                                  
    
calcularPromedio(7)
