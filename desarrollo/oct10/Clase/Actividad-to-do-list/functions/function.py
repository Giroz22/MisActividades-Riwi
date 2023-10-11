def menu():
    try:                
        print("=================================")
        print("1. Crear una tarea nueva")
        print("2. Mostrar tareas pendientes")
        print("3. Modificar una tarea")
        print("4. Terminar una tarea")
        print("0. Salir")
        print("=================================")

        opc = int(input("Seleccione una opcion:"))    
        
    except:                
        opc = -1
    
    if (opc < 0 and opc > 5):
        msjError("Opcion invalida")
        
    return opc
        
def msjError(msj):
    print(f'Error: {msj}')
    
def msjInfo(msj):
    print("=================================")
    print(msj)