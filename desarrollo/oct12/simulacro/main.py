from functions.function import menuPrincipal, mostrarMenuMantenimiento, mostrarMenuPremiosRIWI
from functions.logica.mantenimientoCoders import *
from functions.logica.premiacionRIWI import *
# - 
def main():
    
    # variables    
    grupos = [
        {
            "nombre": "A",
            "coders": [],
            "trainer": ""
        },
        {
            "nombre": "B",
            "coders": [],
            "trainer": ""
        },
        {
            "nombre": "C",
            "coders": [],
            "trainer": ""
        }]        
    
    # - Traemos los datos    
    grupos[0]["coders"] = dbCodersGPA()
    grupos[1]["coders"] = dbCodersGPB()
    
    while (True):
        opc = menuPrincipal()
        
        match (opc):             
            case 0:
                break
            case 1:
                opcMant = mostrarMenuMantenimiento()
                
                match(opcMant):
                    case 1:
                        ingresarCoder(grupos)
                    case 2:
                        registrarTrainer(grupos)
                    case 3:
                        buscarCodersDuplicados(grupos)
                    case 4:
                        eliminarCodersInasistencia(grupos)
                    case 5:
                        listarCoders(grupos)
                    case 6:
                        trasladarCoder(grupos)
                    case 7:
                        listarCoderEdad(grupos)
                    case 8:
                        listarGrupos(grupos)
                        
            case 2:
                opcPremios = mostrarMenuPremiosRIWI()
                
                match(opcPremios):
                    case 1:
                        buscarMonitorClase(grupos)
                    case 2:
                        buscarInasistencia(grupos)
                    case 3:
                        buscarMasEntregasTalleres(grupos)
                    case 4:
                        buscarMasColaborador(grupos)
                    case 5:
                        buscarMayorNotaTestNivelación(grupos)
                    case 6:
                        buscarMasParticipativo(grupos)
                    case 7:
                        buscarJovenColaborador(grupos)
                        
def dbCodersGPA():
    coders = [{
        "nombre": "Juan Gonzales",
        "mesIngreso": 12,
        "grupo": "A",
        "Edad": 19,
        "numVecesMonitor": 4,
        "numInasistencia": 2,
        "numTalleresEntregados": 6,
        "numColaboracion": 3,
        "notaTestnivelacion": 90,
        "numparticipacion": 3
    },
    {
        "nombre": "Pepito Perz",
        "mesIngreso": 1,
        "grupo": "A",
        "Edad": 18,
        "numVecesMonitor": 4,
        "numInasistencia": 2,
        "numTalleresEntregados": 6,
        "numColaboracion": 3,
        "notaTestnivelacion": 90,
        "numparticipacion": 3
    }]    
    
    return coders

def dbCodersGPB():
    coders = [{
        "nombre": "Juan Gabiria",
        "mesIngreso": 12,
        "grupo": "A",
        "Edad": 19,
        "numVecesMonitor": 4,
        "numInasistencia": 2,
        "numTalleresEntregados": 6,
        "numColaboracion": 3,
        "notaTestnivelacion": 90,
        "numparticipacion": 3
    },
    {
        "nombre": "Pepito Perz",
        "mesIngreso": 1,
        "grupo": "A",
        "Edad": 18,
        "numVecesMonitor": 4,
        "numInasistencia": 2,
        "numTalleresEntregados": 6,
        "numColaboracion": 3,
        "notaTestnivelacion": 90,
        "numparticipacion": 3
    }]    
    
    return coders                  

main()