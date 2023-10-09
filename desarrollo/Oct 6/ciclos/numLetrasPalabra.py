# - Escribe un programa que cuente el numero de letras en una palabra
def contarNumLetras(palabra):
    numletras = 0       
    
    for letra in palabra:  
        if(letra.isalpha()):             
            numletras+=1
        
    print(f'La palabra "{palabra}" tiene {numletras} letras')

def main():
    palabra = input("Ingrese una palabra\n")
    
    contarNumLetras(palabra)

main()