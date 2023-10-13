# Problema 2: Conversión de Moneda
# Descripción del problema: Crea un programa que permita a un usuario ingresar una cantidad de
# dinero en una moneda extranjera y luego convertirla a la moneda local.
 
# El usuario debe proporcionar la cantidad en la moneda extranjera y la tasa de cambio actual. 
# El programa debe calcular y mostrar el equivalente en la moneda local.

# Espero que estos problemas te ayuden en tu clase de Python. Puedes utilizarlos para enseñar
# conceptos básicos de tipos de datos, variables y condicionales.

def main():
    try:
        monedaExtranjera = float(input("Ingrese la cantidad de dinero en la moneda extranjera: "))
        tasaDeCambio = float(input("Ingrese la tasa de cambio actual: "))
        
        vrMonedaLocal = monedaExtranjera * tasaDeCambio
        print(f'El equivalente de ${monedaExtranjera} en la moneda local es: ${vrMonedaLocal}')        
    except:
        print("Ingrese un valor númerico")
        return main()
    
main()
