# Problema 4: Saludo según la hora del dia
# Tu trabajo de saludo personalizado ha dejado a todos encantados, atrayendo la atención de
# personas de todo el mundo que desean experimentar ese toque especial. Sin embargo, un
# pequeño grupo de individuos ha expresado su molestia, ya que ingresan al salón de clases en
# horarios nocturnos y reciben el saludo "buenos días". Saben que eres excepcional en lo que haces,
# por lo que te solicitan un ajuste adicional: que, 
# 
# Según la hora del día, el saludo sea "buenos días",
# "buenas tardes" o "buenas noches", 
# Además de mencionar su nombre. 
# 
# Tu habilidad y flexibilidad
# son fundamentales para brindar a cada persona una experiencia de saludo personalizado más
# adecuada a la hora en que ingresan.

from datetime import datetime

def saludoHoraDia():
    msj = ""
    nombreUsuario = input("Ingresa tu nombre: ")    
    horaActual = datetime.now().hour
    
    if (horaActual >= 0 and horaActual < 12):
        msj += "Buenos Dias"
    elif (horaActual >= 12 and horaActual <= 14):
        msj += "Buenas Tardes"
    else:
        msj += "Buenas Noches"
        
    print(f'{msj}, {nombreUsuario}!!')
saludoHoraDia()