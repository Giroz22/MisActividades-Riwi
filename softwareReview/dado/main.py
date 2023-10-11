from functions.function import menuPrincipal
from functions.logica import jugar_turno

def main():
    while (True):
        opc = menuPrincipal()
        
        match (opc):             
            case 1:
                jugar_turno()
            case 2:
                break

main()