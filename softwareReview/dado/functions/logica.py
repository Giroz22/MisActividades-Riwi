import random
from functions.function import msjInfo, msjError

def jugar_turno():
    saldoInicial = 100
    jugadores = [
{
    "nombre": "USUARIO",
    "ptos": 0,
    "saldo": saldoInicial,
    "wins": 0
},
{
    "nombre": "COM",
    "ptos": 0,
    "saldo": saldoInicial,
    "wins": 0
}]
    flag = True
    while flag:        
        
        msjInfo("Es tu turno de lanzar!!")
        puntosRondaJugador = lanzar_dado()
        jugadores[0]["ptos"] += puntosRondaJugador
        msjInfo(f'Sacaste: {puntosRondaJugador}')
        
        msjInfo("Es turno de COM para lanzar")
        puntosRondaCOM = lanzamiento_computadora()
        jugadores[1]["ptos"] += puntosRondaCOM
        msjInfo(f'COM saco: {puntosRondaCOM}')
        
        if(puntosRondaJugador != puntosRondaCOM):            
            if(puntosRondaJugador > puntosRondaCOM):
                jugadores[0]["wins"] += 1            
            else:
                jugadores[1]["wins"] += 1
        else:
            msjInfo("Empate!! en el lanzamiento")
        
        for jugador in jugadores:
            if(jugador["wins"] == 3):
                flag = False
                            
    jugadorWin = jugadores[0]
    for jugador in jugadores:
        if(jugador["wins"] > jugadorWin["wins"]):
            jugadorWin = jugador
            
    msjInfo(f'El jugador ganador es {jugadorWin["nombre"]} con {jugadorWin["ptos"]}, Felicidades!!')
    
    
def lanzar_dado():
    print("Lanzando dado...")
    
    numRandom = random.randint(1, 6)    
    
    return numRandom
    
    
def lanzamiento_computadora():
    print("COM va a lanzar el dado...")
    return lanzar_dado()