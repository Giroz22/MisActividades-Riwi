# - Problema, en base a los numeros igresados se imprime si es multiplo de 3 y 5 o no
def encotrarMultiplo():
    try:
        # Declaramos las listas                                
        multiplosde3y5 = []
        noMultiplosde3y5 = []        
        
        # pedimos los datos 3 veces
        for i in range(3):
            num = int(input("Ingrese un numero:\n"))  
            esMultiplo3y5 = validarMultiplo3y5(num)
            
            # guardamos el numero en una lista u otra
            if(esMultiplo3y5):
                multiplosde3y5.append(num)
            else:                
                noMultiplosde3y5.append(num)                
        
        # - Imprimimos los numeros que son multiplos de 3 y 5        
        msj = "Multiplos de 3 y 5: " 
        for num in multiplosde3y5:
            msj += "\n" + str(num)
               
        # - Creamos un mensaje con los numeros que no son multiplos de 3 y 5
        msj += "\nNo son multiplos de 3 y 5: "
        for num in noMultiplosde3y5:
            msj += "\n" + str(num)
        
        # - Imprimimos el mensaje
        print(msj) 
        
    except ValueError:
        print("Ingrese un valor valido")
        encotrarMultiplo()
    except Exception as e:
        print("Error en ejecucion:", e)         

def validarMultiplo3y5(num):              
    if (num % 3 == 0 and num % 5 == 0):            
        return True
    else:
        return False            
    
encotrarMultiplo()