def validarCalificacion():
    try:
        return
    except ValueError:
        print("Ingrese un valor valido")
        validarCalificacion()
    except:
        print("Error en ejecucion") 
        
validarCalificacion()