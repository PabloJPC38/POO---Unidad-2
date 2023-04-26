from modulo2 import Archivo
from modulo1 import Viajero

if __name__ == "__main__":
    
    viajero:list[Viajero] = Archivo.leerArchivo()
    Archivo.Menu(viajero,int(input("Ingresar número de viajero:")))
    