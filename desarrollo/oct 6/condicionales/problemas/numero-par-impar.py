def verificarParInpar():
    try:
        num = int(input("Ingrese un numero:\n"))
                
        if( num % 2 == 0 ):
            msj = "El numero es par"
        else:
            msj = "El numero es impar"
            
        if( num > 10 ):
            msj += " y es mayor a 10"
        else:
            msj += " y es menor a 10"
            
        print(msj)
                
    except ValueError:
        print("Ingrese un valor valido")
        verificarParInpar()
    except:
        print("Error en ejecucion") 
        
verificarParInpar()