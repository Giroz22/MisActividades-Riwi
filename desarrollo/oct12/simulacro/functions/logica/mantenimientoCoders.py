from functions.function import msjInfo, msjError, mostrarMenuGrupos, menu

def ingresarCoder(grupos):
    try:
        idGrupo = grupos[mostrarMenuGrupos()]["nombre"]         
        
        coder = {
            "nombre" : input("Nombre: "),
            "mesIngreso": int(input("Mes Ingreso: ")),
            "grupo": grupos[idGrupo]["nombre"],
            "Edad": input("Edad: "),
            "numVecesMonitor": int(input("Número de veces en que se ha desempeñado como monitor de clase: ")),
            "numInasistencia": int(input("Número de inasistencias: ")),
            "numTalleresEntregados": int(input("Número de talleres entregados: ")),
            "numColaboracion": int(input("Número de colaboraciones: ")),
            "notaTestnivelacion": float(input("Nota test nivelacion: ")),
            "numparticipacion": int(input("Número de participaciones: "))
        }
        
        grupos
    except:
        msjError("El valor ingresado no es valido")            
        return coder

def registrarTrainer(grupos):
    
    # - Se obtiene la id del grupo
    idGrupo = mostrarMenuGrupos()
    
    # - Se solicita la info del trainer
    infoTrainer = input("Ingrese el nombre del Trainer: ")
    
    # - Se guarda la info
    grupos[idGrupo]["trainer"] = infoTrainer
    msjInfo("El trainer se registro correctamente!!")
    
    

def buscarCodersDuplicados(grupos):
    
    coderDuplicados = []
    
    # - Grupos en los cuales se va hacer la comparacion
    msjInfo("Seleccione los grupos con los cuales se van a buscar duplicados")
    
    idGrupo1 = mostrarMenuGrupos()
    codersGP1 = grupos[idGrupo1]["coders"]
        
    msjInfo("Seleccione el otro grupo")
    
    idGrupo2 = mostrarMenuGrupos()
    codersGP2 = grupos[idGrupo2]["coders"]
    
    if (idGrupo1 == idGrupo2 ):
        msjError("Los grupos no deben ser los mismos")
        return buscarCodersDuplicados()        
    
    #Se comparan los grupos
    for coderGP1 in codersGP1:
        for coderGP2 in codersGP2:
            if (coderGP1["nombre"] == coderGP2["nombre"]):
                coderDuplicados.append(coderGP1)
                
    print(f'Los coders duplicados son: \n {coderDuplicados}')    
        
    

def eliminarCodersInasistencia():
    return

def listarCoders(grupos):
    
    # - Mostrar grupos y obtener seleccion
    idGrupo = mostrarMenuGrupos()
    
    # - Buscar Grupo
    coders = grupos[idGrupo]["coders"]
    
    # - Imprimimos los coders de ese grupo    
    for index, coder in enumerate(coders):                        
        # - Imprimimos los datos de ese coder        
        print(f'\n{index + 1 } - {coder}')
        print("________________________________")    

# - Se lista toda la info de un grupo
def listarGrupos(grupos):
    # - Mostrar grupos y obtener seleccion
    idGrupo = mostrarMenuGrupos()
    
    # - Imprimimos el grupo
    print(grupos[idGrupo])
    msjInfo("Se Listo el grupo correctamente!!")

def trasladarCoder():
    return

def listarCoderEdad():
    return