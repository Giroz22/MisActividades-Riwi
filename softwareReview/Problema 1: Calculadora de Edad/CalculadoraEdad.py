# Problema 1: Calculadora de Edad
# Descripción del problema: Escribe un programa en Python que solicite al usuario su año de
# nacimiento y calcule automáticamente su edad. Luego, el programa debe verificar si la persona es
# mayor de 18 años y mostrar un mensaje que diga "Eres mayor de edad" o "Eres menor de edad"
# según corresponda

from datetime import datetime

# - Problema: En base al año de nacimiento se valida si una persona es mayor o menor de edad
def calcularEdad():
    try:        
        # - Pedimos el año de nacimiento
        annoNacimiento = input("Ingrese su año de nacimiento: ")        

        # - validamos si el año de nacimiento es numerico y positivo
        if(not annoNacimiento.isnumeric()):
            print("Ingrese un año correcto")
            calcularEdad()
        
        # - Obtenemos el año actual y convertimos el año de nacimiento a tipo de datao numerico
        annoActual = datetime.now().year
        annoNacimiento = int(annoNacimiento)
        
        # - Calculamos la edad  
        edad = annoActual - annoNacimiento 
        
        # - En base a la edad imprimimos si es mayor o menor de edad 
        if(edad > 18):
            print("Eres mayor de edad")
            
            if(edad > 60):
                print("y ademas eres un adulto mayor")
        else:
            print("Eres menor de edad")
                        
    except:
        print("Error en ejecucion")
        calcularEdad()
        
calcularEdad()