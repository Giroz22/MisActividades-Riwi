import pandas as pd

def mostrar_inventario(inventario):
    if (not inventario):
        print("\n El inventario esta vacio \n")
    else:
        print("\nLista de productos\n")
        for index, valor in enumerate(inventario):
            print(index,".", valor["nombre"],"-",valor["cantidad"],"unidades - $",valor["precio"])

def agregar_producto(inventario):
    try:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = int(input("Ingrese el precio del del producto: ")) 
        
        producto = {"nombre": nombre.capitalize(), "cantidad": int(cantidad), "precio": float(precio)}
        inventario.append(producto)
        
        print("\nProducto agregado exitosamente!!\n")
    except:
        print("Los valores ingresados no son validos")
    
def actualizar_producto(inventario):
    mostrar_inventario(inventario)
    
    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice del producto: "))
            
            if(indice < 0 or indice > len(inventario)):
                print("El indice ingresado no corresponde a ningun producto")
            else:
                print("Actualizando el producto", inventario[indice]["nombre"],"-", inventario[indice]["cantidad"],"unidades - $", inventario[indice]["precio"])
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = int(input("Ingrese el precio del del producto: ")) 
        
                inventario[indice]["nombre"] = nombre.capitalize()
                inventario[indice]["cantidad"] = int(cantidad)
                inventario[indice]["precio"] = float(precio)
                
                print("\n El producto fue actualizado correctamente!! \n")                                
        except ValueError:
            print("El valor ingresado debe ser un número")
            
def eliminar_producto(inventario):
    
    mostrar_inventario(inventario)

    if not inventario:
        return
    else:
        try:                            
            indice = int(input("Ingrese el indice del producto a eliminar: "))
            
            if(indice < 0 or indice > len(inventario)):
                print("El indice ingresado no corresponde a ningun producto")
            else:     
                confirmacion = input("Esta Seguro que desea eliminar el producto?: ") 
                        
                if(confirmacion.lower() == "si"):
                    productoEliminado = inventario.pop(indice)
                    print("\nEl producto", productoEliminado["nombre"],"-", productoEliminado["cantidad"],"unidades - $", productoEliminado["precio"], ", Se elimino correctamente!!\n")                                                                                    
                else:
                    print("\n Se cancelo la eliminacion \n")                                                           
        except ValueError:
            print("\nError: El valor ingresado debe ser un número\n")   

def exportar_excel(inventario):
    if not inventario:  
        return
    else:
        df = pd.DataFrame(inventario)
        
        nombre_archivo = input("Ingrese el nombre del archivo de excel: ")
        
        df.to_excel(nombre_archivo, df)

