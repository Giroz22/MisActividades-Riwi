#Variables globales
# global a, b

# - Recibe dos numeros y en base a la operacion realizada realiza una operacio u otra
def main():              

    # Solicitamos que el usuario seleccione la operacion
    opc = mostrarMenu()
    
    # Validamos que la opcion seleccionada este en el rango de las opciones
    if opc > 0 & opc < 6: 
            
        #Solicitamos los valores
        a,b = pedirNumeros()

        # En base a la seleccion realizamos una operacion u otra
        match opc:
            case 1:
                suma(a,b)
            case 2:
                resta(a,b)   
            case 3:
                multiplicacion(a,b)
            case 4: 
                if b != 0:
                    division(a,b)
                else:
                    mostrarmsjError("No se puede dividir entre cero")  
                    main()                  
            case 5:
                potencia(a,b)
                
    # opcion de salir
    elif opc == 6:
        return
    else:
        mostrarmsjError("Ingrese un valor valido")    
        main()

# - Operaciones basicas         
def suma(a,b):
    suma = a+b        
    print("La suma de:" ,a ,"+",b ,"=" ,suma)
    
def resta(a,b):
    resta = a-b
    print("La resta de:" ,a ,"-",b ,"=" ,resta) 
    
def multiplicacion(a,b):
    multiplicacion = a*b
    print("La multiplicacion de:" ,a ,"*",b ,"=" ,multiplicacion) 
    
def division(a,b):
    division = a//b        
    print("La division de:" ,a ,"/",b ,"=" ,division)
    
def potencia(a,b):
    potencia = pow(a,b)
    print("La potencia de" ,a ,"sobre", b, "=", potencia)
        
# - Muestra un mensaje de error         
def mostrarmsjError(msj):
    print("\nError:", msj, "\n")    
    
# - Solicita dos numeros enteros
def pedirNumeros():
    try:              
        a = int(input("Ingrese el primer valor: "))

        b = int(input("Ingrese el segundo valor: "))
        
        return a, b
    except:
        mostrarmsjError("Ingrese un valor valido")
        main()          
        
# - Muestra un menu de opciones y retorna el numero con la opcion seleccionada 
# 1.Suma 2.Resta 3.Multiplicacion 4.Division 5.Potencia 6.Salir
def mostrarMenu():
    try:                
        return int(input("Seleccione la operacion que desea realizar: \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division\n5.Potencia\n6.Salir\n"))
    except:
        mostrarmsjError("Ingrese un valor valido")
        main()
    
main()