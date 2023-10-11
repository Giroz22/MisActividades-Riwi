
def menu():
    try:                
        print("\n===========To Do List============")
        print("1. Crear tarea nueva")
        print("2. Mostrar tareas pendientes")
        print("3. Modificar tarea")
        print("4. Eliminar tarea")
        print("0. Salir")
        print("=================================")

        opc = int(input("Seleccione una opcion:"))    
        
    except:                
        opc = -1
    
    if (opc < 0 or opc > 5):
        msjError("Opcion invalida")
        
    return opc
    
def seleccionarTarea(tareas):
    from functions.crud import mostrar_tarea
    
    while (True):
        mostrar_tarea(tareas)        
    
        try:        
            indice = int(input("Seleccione una tarea: "))
            
            if (indice < 0 or indice > len(tareas)):
                msjError("La tarea seleccionada no existe")
                continue

            return indice
            
        except:
            msjError("Ingrese un valor valido")
            continue
                
def msjError(msj):
    print("\n=================================\n")
    print(f'Error: {msj}')
    input("\nEnter para continuar...\n")
    
def msjInfo(msj):
    print("\n=================================")
    print(msj)
    input("\nEnter para continuar...\n")