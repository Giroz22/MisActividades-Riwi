# Problema 6: Investigar sobre la modulo .random
# Enunciado:
# El objetivo de este programa es simular el lanzamiento de un dado de seis caras y permitir al
# usuario jugar contra la computadora. Cada jugador tiene un saldo inicial de $100 y pueden realizar
# apuestas en cada lanzamiento del dado. El juego se juega al mejor de 3 lanzamientos, y el jugador
# que gane más lanzamientos al final del juego es el ganador.
# Requerimientos:
# 1. El programa debe importar el módulo random para generar números aleatorios.
# 2. Debe definir una función lanzar_dado() que genere un número aleatorio entre 1 y 6,
# simulando el lanzamiento de un dado de seis caras.
# 3. Debe definir una función lanzamiento_computadora() que simplemente llame a la función
# lanzar_dado() para obtener el lanzamiento de la computadora.
# 4. La función principal del juego, llamada jugar_turno(), debe realizar el juego completo.
# Debe configurar saldos iniciales para el jugador y la computadora, y llevar un recuento de
# los turnos ganados por cada uno.
# 5. Debe permitir al jugador y la computadora realizar apuestas en cada lanzamiento. Las
# apuestas deben ser múltiplos de 10 y no pueden exceder el saldo disponible.
# 6. Debe mostrar el resultado de los lanzamientos y determinar el ganador de cada
# lanzamiento. Los saldos deben actualizarse en consecuencia.
# 7. El juego debe continuar hasta que uno de los jugadores gane tres lanzamientos.
# 8. Al final del juego, debe determinar al ganador y mostrar un mensaje que indique quién
# ganó, así como los saldos finales del jugador y la computadora.
# 9. El juego se inicia llamando a la función jugar_turno().


from functions.function import menuPrincipal
from functions.logica import iniciar_juego

def main():
    while (True):
        opc = menuPrincipal()
        
        match (opc):             
            case 1:
                iniciar_juego()
            case 2:
                break

main()