from functions.function import msjInfo, msjError, seleccionarTarea

def crear_tarea(tareas):    
    try:
        print("=====Crear Tarea=====")
        
        nombre = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripcion de la tarea: ")
        fecha = input("Ingrese la fecha de finalizacion de la tarea: ")
        
        tarea = {"nombre":nombre,
                "descripcion":descripcion,
                "fecha": fecha}
        
        tareas.append(tarea)
        
        msjInfo("Tarea creada exitosamente!!")
    except:
        msjError("El valor ingresado es invalido")
    
def mostrar_tarea(tareas):        
    if (not tareas):        
        msjInfo("No tienes tareas pendientes")
        return
    
    print("============ Tareas =============")
    for clave, valor in enumerate(tareas):
        print(f'\n{clave}. Nombre: {valor["nombre"]}')
        print(f'   Descripcion: {valor["descripcion"]}')
        print(f'   Fecha: {valor["fecha"]}')
        print("________________________________________")
    
def modificar_tarea(tareas):        
    indice = seleccionarTarea(tareas)            
        
    try:
            
        msjInfo(f'=====Modificando la tarea ({tareas[indice]["nombre"]})=====')    
        nombre = input("Ingrese el nuevo nombre de la tarea: ")
        descripcion = input("Ingrese la nueva descripcion de la tarea: ")
        fecha = input("Ingrese la nueva fecha de finalizacion de la tarea: ")
        
        tareas[indice]["nombre"] = nombre
        tareas[indice]["descripcion"] = descripcion
        tareas[indice]["fecha"] = fecha
        
        msjInfo("La tarea se modifico correctamente!!")
    except:
        msjError("El valor ingresado es invalido")
    
    
def eliminar_tarea(tareas):
    indice = seleccionarTarea(tareas)        
    
    confirmacion = input("Esta seguro de terminar la tarea S/N: ")
    
    if(confirmacion.upper() != "S"):
        print(f'No se elimino la tarea ({tareas[indice]["nombre"]})')
        return
    
    tareaEliminada = tareas.pop(indice)
    
    msjInfo(f'La tarea ({tareaEliminada["nombre"]}) se elimino correctamente')
    
    
    
    