# - problema: calcular el IMC
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