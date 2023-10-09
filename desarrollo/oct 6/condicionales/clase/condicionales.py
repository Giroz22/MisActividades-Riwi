try:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    if(a == b):
        print("Los dos numeros son iguales")
    elif a > b:
        print("El numero", a, "es mayor que", b)
    else:
        print("El numero", b, "es mayor que", a)
except:
    print("Solo puedes ingresar numeros")