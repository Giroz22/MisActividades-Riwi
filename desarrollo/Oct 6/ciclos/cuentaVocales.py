# - Cuenta el número de vocales que hay en una palabra 
def cuentaVocales():   
    texto = input("Ingrese una cadena de texto: \n")     
    numVocales = sum(map(texto.lower().count, "aeiouáéíóú"))
    print(f'La palabra "{texto}" tiene {numVocales} vocales')
    
cuentaVocales()
