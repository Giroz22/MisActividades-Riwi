opcion = ""
resultado_actual = 0
def mostrarMenu():
    print("==================================")
    print("======== Menú de opciones =============")
    print("===================================")
    print("1.sumar")
    print("2.restar")
    print("3.multiplicar")
    print("4.dividir")
    print("5.salir")

def sumar(lista,resultado_actual):
    #Suma la lista de números
    total = 0
    numeros_sumados = ""
    for indice in lista:
        total += indice+ resultado_actual
        numeros_sumados +=  str(indice) + "+"
    #Muestra en pantalla la lista de números y su resultado
    # print("La suma de", lista," es: ",total)
    resultado_actual = numeros_sumados
    print("La suma de", numeros_sumados[0:len(numeros_sumados)-1]," es: ",total)

def restar(lista,resultado_actual):
    #Suma la lista de números
    total = lista[0]
    numeros_restados = ""
    for indice in lista[1:]:
        total =  total - indice
        
        # if(resultado_actual >0):
        #     total = total - resultado_actual
        numeros_restados +=  str(indice) + "-"
    #Muestra en pantalla la lista de números y su resultado
    # print("La suma de", lista," es: ",total)
    resultado_actual = numeros_restados
    print("La resta de",lista[0],"-", numeros_restados[0:len(numeros_restados)-1]," es: ",total)

flag = True
flag2 = True
flag3 = True

while flag:
    mostrarMenu()
    opcion = input("Ingrese una opción: ")

    if(opcion ==  "1"):
        lista_numeros = []
        while flag2:
           nuevo_numero = int(input("Ingrese el número a sumar: "))
           lista_numeros.append(nuevo_numero)
           seguir = input("Desea continuar? SI o NO: ")
           if(seguir.lower() == "no"):
               flag2 = False
               sumar(lista_numeros,resultado_actual)
    if(opcion == "2"):
        lista_numeros = []
        while flag3:
           nuevo_numero = int(input("Ingrese el número a restar: "))
           lista_numeros.append(nuevo_numero)
           seguir = input("Desea continuar? SI o NO: ")
           if(seguir.lower() == "no"):
               flag3 = False
               restar(lista_numeros,resultado_actual)
            
    if(opcion ==  "5"):
        flag = False
    