# - Sistema de inventario para tienda
from funciones.funciones import mostrar_inventario, actualizar_producto, agregar_producto, eliminar_producto, exportar_excel
            
def main():
    inventario = [
        {"nombre":"Arroz","cantidad": 34, "precio": 2700},
        {"nombre":"Panela","cantidad": 25, "precio": 2300},
        {"nombre":"Pan","cantidad": 21, "precio": 700},                
    ]
    
    while (True):
        input("Presione enter para continuar...")
        print("\n Sistema de inventario ")
        print("1. Mostrar todos los productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Exportar excel")
        print("6. Salir")
        
        opc = input("Ingrese una opcion: ")
        if (opc == "1"):
            mostrar_inventario(inventario)
        elif (opc == "2"):
            agregar_producto(inventario)
        elif (opc == "3"):            
            actualizar_producto(inventario)
        elif (opc == "4"):
            eliminar_producto(inventario)
        elif (opc == "5"):                                    
            exportar_excel(inventario)
        elif (opc == "6"):
            break
        
main()