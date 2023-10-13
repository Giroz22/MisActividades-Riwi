# Problemas 3: Calculadora IMC
# Han quedado encantado con todos tus proyectos realizamos hasta este momento, y te hablaron
# de una pequeña clínica que apenas esta comenzando para que les realices un sistema sencillo.
# Debes de crear un programa que ayudará a las personas a entender cómo está su salud. Tu
# programa permitirá a los usuarios ingresar su peso en kilogramos y su altura en metros. Luego, de
# manera automática, calculará su Índice de Masa Corporal (IMC).
# El código debe tener de salida si el índice de masa corporal
# es menor a 18.5, esta por debajo de su peso ideal
# Si mayor a 18.5 y es menor que 24.9, esta en el rango saludable
# Si es mayor a 25 y menor a 29.9, tienes sobre peso
# Si es mayor a 30 y menor a 34.9, tienes obesidad grado I
# Si es mayor a 35 y menor a 39.9, tienes obesidad grado II
# En caso que sea superior, tienes obesidad grado III

def calcularIMC():
    
    # - Se piden los datos
    try:
        peso = int(input("Ingrese su peso(kg): "))
        altura = float(input("Ingrese su altura(mt): "))
    except:
        print("\nIngrese un valor valido\n")
        calcularIMC()
    
    # - Se calcula el IMC
    imc = peso / pow(altura, 2)
    imc = round(imc, 4)
    
    print("\nSu IMC es de:", imc)
    
    if imc < 18.5:
        msjDiagnostico("bajo peso")
    elif imc >= 18.5 and imc < 25:
        msjDiagnostico("peso normal")
    elif imc >= 25 and imc < 30:
        msjDiagnostico("sobrepeso")
    elif imc >= 30 and imc < 35:
        msjDiagnostico("obesidad tipo 1")
    elif imc >= 35 and imc < 40:
        msjDiagnostico("obesidad tipo 2")
    elif imc >= 40:
        msjDiagnostico("obesidad tipo 3")            

def msjDiagnostico(diagnostico):
    print("Te encuentras en " + diagnostico)

calcularIMC()