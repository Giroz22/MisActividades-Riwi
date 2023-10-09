def calcularCalificacion():
    try:
        calificacion = float(input("Ingrese su calificacion numerica:\n"))        
        
        #if(calificacion in range(0, 100)):
        if(calificacion < 100 and calificacion > 0):
            if(calificacion > 80):
                msjCalificacion("A")
            elif(calificacion > 65):
                msjCalificacion("B")
            elif(calificacion > 55):
                msjCalificacion("C")                
            elif(calificacion > 55):
                msjCalificacion("D")                
            else:
                msjCalificacion("F")
        else:
            print("Ingrese un numero entre 0 y 100")
            calcularCalificacion()
        
    except ValueError:
        print("Ingrese un valor valido")
        calcularCalificacion()
    except:
        print("Error en ejecucion")    

# - Imprime un mensaje en comun para las calificaciones
def msjCalificacion(calificacionAlfabetica):    
    print("Su calificacion alfabetica es", calificacionAlfabetica)
    
calcularCalificacion()