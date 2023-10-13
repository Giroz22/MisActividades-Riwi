def menuPrincipal():
    print("====================")
    print("1. Iniciar Juego")
    print("2. Salir")
    print("====================")
    
    try:
        opc = int(input("Seleccione una opcion: "))
        
        if (opc < 0 or opc > 2):
            msjError("Opcion invalida")
            
        return opc                
    except:
        msjError("Ingrese un valor númerico")
        
def menuJuego():
    print("====================")
    print("1. Lanzar dado")
    print("2. Apostar")
    print("3. Terminar juego")    
    print("====================")
    
    try:
        opc = int(input("Seleccione una opcion: "))
        
        if (opc < 0 or opc > 3):
            msjError("Opcion invalida")
            
        return opc                
    except:
        msjError("Ingrese un valor númerico")
     
def msjError(msj):
    print("\n=================================\n")
    print(f'Error: {msj}')
    input("\nEnter para continuar...\n")
    
def msjInfo(msj):
    print("\n=================================")
    print(msj)
    input("\nEnter para continuar...\n")