# Juego de preguntas
from functions.function import menuPrincipal, msjInfo
from functions.juego import iniciarJuego

def main():
    while (True):
        opc = menuPrincipal()
        
        match (opc):             
            case 1:
                iniciarJuego()
            case 2:
                break

main()