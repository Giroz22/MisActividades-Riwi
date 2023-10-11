from functions.crud import crear_tarea, mostrar_tarea, modificar_tarea, eliminar_tarea
from functions.function import menu

def main():
    listaTareas = []  
    listaTareas = [
                    {"nombre":"Expo",
                    "descripcion":"Exposicion habilidades",
                    "fecha": "11/oct/23"},
                    {"nombre":"desarrollo",
                    "descripcion": "Hacer programa de preguntas",
                    "fecha": "11/oct/23"},
                    {"nombre":"Tarea Ingles",
                    "descripcion":"Consultar verbo tobe",
                    "fecha": "11/oct/23"}
        ]      
    
    while (True):                
        
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
                eliminar_tarea(listaTareas)                            
                
main()