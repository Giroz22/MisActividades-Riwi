from functions.function import msjInfo

def crear_tarea(tareas):
    print("=====Crear Tarea=====")
    
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripcion de la tarea: ")
    fecha = input("Ingrese la fecha de finalizacion de la tarea: ")
    
    tarea = {"nombre":nombre,
             "descripcion":descripcion,
             "fecha": fecha}
    
    tareas.append(tarea)
    
    msjInfo("Tarea creada exitosamente!!")
    
def mostrar_tarea(tareas):        
    if (not tareas):        
        msjInfo("Felicidades!! No tienes tareas pendientes")
        return
    
    print("=====Tareas pendientes=====")
    for clave, valor in enumerate(tareas):
        print(f'{clave}. Nombre: {valor["nombre"]}')
        print(f'   Descripcion: {valor["descripcion"]}')
        print(f'   Fecha: {valor["fecha"]}')
        print("________________________________________")
    
def modificar_tarea(tareas):
    print("modificar")
def terminar_tarea(tareas):
    print("terminar")