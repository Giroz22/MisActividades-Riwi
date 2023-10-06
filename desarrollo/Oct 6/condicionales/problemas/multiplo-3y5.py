def encotrarMultiplo():
    try:          
        num = int(input("Ingrese un numero:\n"))                
        multiplosde3y5 = []
        noMultiplosde3y5 = []
        msj = ""
        
        for i in range(3):
            esMultiplo3y5 = validarMultiplo3y5(num)
            
            if(esMultiplo3y5):
                multiplosde3y5.append(num)
            else:
                noMultiplosde3y5.append(num)
        
        # for num in multiplosde3y5:
        #     print(num)
            
        # for num in noMultiplosde3y5:
        #     print(num)
        
        #print(msj) 
        
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