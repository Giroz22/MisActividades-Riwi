# - logica del juego
from functions.function import msjError, msjInfo

def iniciarJuego():
    # Puntuacion
    puntuacion = 0
    
    # Buscamos preguntas
    preguntas = leerPreguntas()
    
    # Imprimir pregunta
    for pregunta in preguntas: 
        # En caso de un error se debe repetir la pregunta       
        while(True):
            print(pregunta["pregunta"])
            
            # Recorremos las opciones de la pregunta
            for index, opcion in enumerate(pregunta["opciones"]):
                print(f'{index} - {opcion}')            
        
            # Solicitar respuesta
            try:
                seleccionUsuario = int(input("Seleccione una opcion: "))                        
                
                if ( seleccionUsuario < 0 or seleccionUsuario > len(pregunta["opciones"])-1 ):
                    msjError("Opcion invalida")
                    continue
                else:                
                    respuestaUsuario = pregunta["opciones"][seleccionUsuario]                                                
                    break
            except ValueError:
                msjError("Ingrese un valor númerico")
                continue
                    
        # Validar si es correcta
        if (respuestaUsuario == pregunta["respuesta"]): 
                       
            # Aumentamos puntuacion
            puntuacion = puntuacion + 1                
            
            msjInfo("Pregunta Correcta!!")         
        else:
            msjInfo("Pregunta incorrecta")
                                            
    # Imprimimos puntos
    msjInfo(f'Preguntas correctas: {puntuacion}')
    
    
def leerPreguntas():
    preguntas = [
{
    "pregunta": "pregunta 1",
    "opciones": ["opcion1", "opcion2","opcion3",],
    "respuesta": "opcion1"
},
{   "pregunta": "pregunta 2",
    "opciones": ["opcion1", "opcion2","opcion3",],
    "respuesta": "opcion2"
},
{
    "pregunta": "pregunta 3",
    "opciones": ["opcion1", "opcion2","opcion3",],
    "respuesta": "opcion3"
}]
    
    return preguntas   
    
def imprimirPregunta():
    print("imprimir preguntas")