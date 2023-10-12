# - Funcion con la validacion basica de un menu
# - Return: entero que hace referencia a la opcion que el usuario selecciono 
def menu(numOpc):        
    
    try:
        opc = int(input("Seleccione una opcion: "))
        
        if (opc < 0 or opc > numOpc):
            msjError("Opcion invalida")
            return -1 
            
        return opc                
    except:
        msjError("Ingrese un valor númerico")
        return -1        

# - Muestra el menu con las opciones basicas del programa
def menuPrincipal():    
    print("========== </RIWI> ==========")
    print("1. Ingresar mantenimiento de Coders")
    print("2. Ingresar premiación RIWI")
    print("0. Salir")
    print("====================")
    
    opc = menu(2)
    
    if (opc == -1):
        return menuPrincipal()
    else:         
        return opc
     
# - Muestra el menu módulo de mantenimiento de Coders
def mostrarMenuMantenimiento():
    print("========== Mantenimiento de Coders ==========")
    print("1. Ingresar Coder")
    print("2. Registrar Trainer")    
    print("3. Buscar Coders duplicados")
    print("4. Eliminar coders por inasistencia")
    print("5. Listar Coders")
    print("6. Traslado del coder")
    print("7. Listar CODER edad") 
    print("8. Listar grupos")        
    print("0. Volver Atras")
    print("====================")
    
    opc = menu(8)
    
    if (opc == -1):
        return mostrarMenuMantenimiento()
    else:         
        return opc    
     
# - Muestra el menu del módulo premiación RIWI
def mostrarMenuPremiosRIWI():
    print("========== Premiación RIWI ==========")
    print("1. Monitor de clase")
    print("2. Inasistencia")
    print("3. Más entregas de talleres")
    print("4. Más colaborador")
    print("5. Mayor nota en Test de nivelación.")
    print("6. Más participativo")
    print("7. Joven colaborador")    
    print("0. Volver Atras")
    print("====================")
    
    opc = menu(7)
    
    if (opc == -1):
        return mostrarMenuPremiosRIWI()
    else:         
        return opc 

# - Muestra el menu de los grupos
def mostrarMenuGrupos():
    print("==========Grupos==========")
    print("1. Grupo A")
    print("2. Grupo B")
    print("3. Grupo C")    
    print("====================")

    opc = menu(3)
    
    if (opc == -1 or opc == 0):
        return mostrarMenuGrupos()
    else:         
        return opc - 1 

def msjError(msj):
    print("\n=================================\n")
    print(f'Error: {msj}')
    input("\nEnter para continuar...\n")
    
def msjInfo(msj):
    print("\n=================================")
    print(msj)
    input("\nEnter para continuar...\n")