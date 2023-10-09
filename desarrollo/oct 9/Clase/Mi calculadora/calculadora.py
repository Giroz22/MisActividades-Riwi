# - 
def main():              

    # Solicitamos que el usuario seleccione la operacion
    opc = mostrarMenu()
    listaNum = []
        
    # En base a la seleccion realizamos una operacion u otra
    match opc:
        # opcion de salir
        case 0:
            return
        case 1:
            suma(listaNum)
        case 2:
            resta(listaNum)   
        case 3:
            multiplicacion(listaNum)
        case 4:                 
            division(listaNum)                                                             
        case 5:
            potencia(listaNum) 
        case _:
            mostrarmsjError("Ingrese un valor valido")    
            
    main()  

# - Operaciones basicas         
def suma(listaNum):
    total = 0   
    msj = "La suma de :" 
    
    listaNum = pedirNumeros(2, True, listaNum)    
    for num in listaNum:
        total += num
        msj += f' {num} +' 
          
    msj += f' = {total}'
    mostrarMsj( msj )
    
def resta(listaNum):
    total = 0   
    msj = "La resta de :" 
    
    listaNum = pedirNumeros(2, True, listaNum)    
    for num in listaNum:
        total -= num
        msj += f' {num} -' 
          
    msj += f' = {total}'
    mostrarMsj( msj )
    
def multiplicacion(listaNum):
    total = 1  
    msj = "La multiplicacion de :" 
    
    listaNum = pedirNumeros(2, True, listaNum)    
    for num in listaNum:
        total = total * num
        msj += f' {num} *' 
          
    msj += f' = {total}'
    mostrarMsj(msj)
    
def division(listaNum):
    
    total = 0   

    listaNum = pedirNumeros(2, False, listaNum) 
    
    if(listaNum[1] == 0):
        mostrarmsjError("No es posible dividir entre 0, vuelva a intentar.")
        return division([])
    else:        
        total = listaNum[0] / listaNum[1]   
          
    mostrarMsj( f'La division de : {listaNum[0]} / {listaNum[1]} = {total}' )
    
def potencia(listaNum):

    listaNum = pedirNumeros(2, False, listaNum) 
    
    total = pow(listaNum[0], listaNum[1])   
            
    mostrarMsj( f'La potencia de : {listaNum[0]} ^ {listaNum[1]} = {total}' ) 
                  
# - Muestra un mensaje de error         
def mostrarmsjError(msj):
    print("\nError:", msj, "\n")    
    
# - Muestra un mensaje         
def mostrarMsj(msj):
    print(f'\n {msj} \n')   
    
# - Solicita los numeros necesarios para realizar una operacion 
# - numMinDto: Número minimo de datos que se necesitan para realizar la operacion
# - flagMasDatos: Booleano que indica si la operacion puede utilizar una cantidad ilimitada de números(Datos)
# - listnum: array donde se van a almacenar los numeros
# - 
# - Return: lista con los números ingresados por el usuario
def pedirNumeros(numMinimoDto, flagMasDatos, listaNum):
    try:        
                
        # - Ciclo en el que se pide un minimo de datos necesarios para realizar una operacion
        for i in range(numMinimoDto):
            num = float(input("Ingrese un valor: "))
            listaNum.append(num)
            numMinimoDto -=1
        
        # - Ciclo en que el usuario ingresa la cantidad de números que desee.
        # - Siempre y cuando la operacion permita MasDatos como (Suma, Resta, multiplicacion...)
        while(flagMasDatos):
            opc = input("Desea ingresar otro valor S/N:\n").upper()
            
            match (opc):
                case "S":
                    listaNum.append(float(input("Ingrese un valor: ")))
                case "N":
                    break
                case _:
                    print("Error: Opcion invalida")                           
        return listaNum
    except ValueError:
        mostrarmsjError("Ingrese un valor valido")
        
        # - numMinimoDto = 0, ya se pidieron el número minimo de datos
        # - se vuelve a enviar la informacion para que no se pierda el proceso
        return pedirNumeros(numMinimoDto, flagMasDatos, listaNum)         
        
# - Muestra un menu de opciones y retorna el numero con la opcion seleccionada 
# 1.Suma 2.Resta 3.Multiplicacion 4.Division 5.Potencia 6.Salir
def mostrarMenu():
    try:                
        return int(input("Seleccione la operacion que desea realizar: \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division\n5.Potencia\n0.Salir\n"))
    except:
        mostrarmsjError("Ingrese un valor valido")
        main()
    
main()

#num = float(input("Ingrese un numero: "))
#print("Tu número es: " + num)