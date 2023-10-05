# - Problema: pasar de celsius a fahrenheit

def main():
    try:
        opc = int(input("Seleccione la operacion que desea realizar:\n1. Pasar de celsius a fahrenheit\n2. Pasar de fahrenheit a celsius\n"))        
        
        match opc:
            case 1:
                pasarCelsiusFahrenheit()
            case 2: 
                pasarFahrenheitCelsius()
    except:
        print( "\nIngrese un valor valido\n" )
        main()    

# - pasa de celsius a fahrenheit
def pasarCelsiusFahrenheit():
    
    # - Se solicita los datos
    try:
        c = float(input("Ingrese la temperatura en celsius:\n"))
    except:
        print( "\nIngrese un valor valido\n" )
        pasarCelsiusFahrenheit()
    
    # - Se pasa de celsius a fahrenheit
    f = ( ( c * (9 / 5) ) + 32 )
    f = round(f, 3)
    
    print( c, "grados celsius equivalen a", f, "grados fahrenheit")

# - pasa de fahrenheit a celsius
def pasarFahrenheitCelsius():
    
    # - Se solicita los datos
    try:
        f = float(input("Ingrese la temperatura en fahrenheit:\n"))
    except:
        print( "\nIngrese un valor valido\n" )
        pasarCelsiusFahrenheit()
    
    # - Se pasa de  fahrenheit a celsius   
    c = (f - 32) * ( 5 / 9 )
    c = round(c, 3)
    
    print( f, "grados fahrenheit equivalen a", c, "grados celsius")
    
# - Ejecuta el metodo main    
main()
