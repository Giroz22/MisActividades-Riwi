from functions.crud import crear_tarea, mostrar_tarea, modificar_tarea, terminar_tarea
from functions.function import menu, msjError

def main():
    listaTareas = []        
    
    while (True):
        
        input("\nEnter para continuar...\n")
        
        opc = menu()
        
        match opc:
            case 0: 
                break
            case 1:
                crear_tarea(listaTareas)
            case 2:
                mostrar_tarea(listaTareas)
            case 3:
                modificar_tarea(listaTareas)
            case 4:
                terminar_tarea(listaTareas)                            
                
main()