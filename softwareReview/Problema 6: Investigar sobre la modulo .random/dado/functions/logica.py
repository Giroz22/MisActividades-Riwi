import random
from functions.function import msjInfo, msjError, menuJuego

def iniciar_juego():
    saldoInicial = 100
    jugadores = [ 
{
    "nombre": "USUARIO",
    "ptos": 0,
    "saldo": saldoInicial,
    "wins": 0,
    "apuesta" : 0
},
{
    "nombre": "COM",
    "ptos": 0,
    "saldo": saldoInicial,
    "wins": 0,
    "apuesta": 0
}]
    flag = True    
    
    while flag:        
        vrApuesta = 0
        
        # - Menu juego
        while(True):            
            opc = menuJuego()
        
            match opc:
                # - iniciar juego
                case 1:                                                   
                    break                    
                # - 2. Realizar apuesta
                case 2:
                    realizarApuesta(jugadores)
                    break                                        
                # - Terminar juego 
                case 3: 
                    return
        
        jugadores = jugar_turno(jugadores) 
        
        # - Validamos si algun jugador ya gano
        for jugador in jugadores:                        
            if(jugador["wins"] == 3):
                jugadorWin = jugador
                flag = False                            
           
    msjInfo(f'El jugador ganador es {jugadorWin["nombre"]} con {jugadorWin["ptos"]}, Felicidades!!')
    
def jugar_turno(jugadores):
    # Turno jugador
    print("============================")
    input("Enter para lanzar dado...")    
    
    ptosP1 = lanzar_dado()
    jugadores[0]["ptos"] += ptosP1
    msjInfo(f'Sacaste: {ptosP1}')

    # - Turno maquina                    
    msjInfo(f'Es turno de {jugadores[1]["nombre"]} para lanzar')
    ptosP2 = lanzamiento_computadora()
    jugadores[1]["ptos"] += ptosP2
    msjInfo(f'{jugadores[1]["nombre"]} saco: {ptosP2}')
    
    return validarGanador(jugadores, ptosP1, ptosP2)
    
def lanzar_dado():        
    numRandom = random.randint(1, 6)        
    return numRandom
    
def lanzamiento_computadora():
    return lanzar_dado()
  
def realizarApuesta(jugadores):
    try:                          
        msjInfo(f'Tu saldo actual es de: ${jugadores[0]["saldo"]}')
        jugadores[0]["apuesta"] = float(input("Ingrese la cantidad que desea apostar: "))
        
        if(jugadores[0]["apuesta"] % 10 != 0):
            msjError("La apuesta debe ser multiplo de 10")
            jugadores[0]["apuesta"] = 0                                                   
            return realizarApuesta(jugadores)            
        else:    
            if( jugadores[0]["apuesta"] <= jugadores[0]["saldo"]):            
                jugadores[0]["saldo"] -= jugadores[0]["apuesta"]             
                msjInfo("Apuesta realizada con exito!!")
            else:                                
                msjInfo("Saldo insuficiente, ingresa un valor menor") 
                jugadores[0]["apuesta"] = 0                                                   
    except ValueError:
        msjError("Ingrese un valor númerico")
        
def validarGanador(jugadores, ptosP1, ptosP2):
    # - Validacion ganador lanzamiento
    if(ptosP1 != ptosP2):            
        if(ptosP1 > ptosP2):            
            jugadores[0]["wins"] += 1             
            msjInfo("Felicidades eres el ganador!!")
            
            #Validamos si el usuario realizo una apuesta
            if (jugadores[0]["apuesta"] != 0) :
                jugadores[0]["saldo"] += jugadores[0]["apuesta"] * 2
                msjInfo(f'Ganaste un total de: ${jugadores[0]["apuesta"] * 2}')
                
        else:
            jugadores[1]["wins"] += 1
            msjInfo("El Ganador es COM")
            
            if (jugadores[0]["apuesta"] != 0) :                
                msjInfo(f'Perdiste un total de: ${jugadores[0]["apuesta"]}')
    else:            
        msjInfo("Empate!! en el lanzamiento")
        
        if (jugadores[0]["apuesta"] != 0) :
            jugadores[0]["saldo"] += jugadores[0]["apuesta"] 
            msjInfo(f'Recuperaste tu apuesta: ${jugadores[0]["apuesta"]}')
    
    if (jugadores[0]["apuesta"] != 0) :   
        msjInfo(f'Tu saldo actual es de: ${jugadores[0]["saldo"]}')                            
        
    jugadores[0]["apuesta"] = 0 
    return jugadores
    
