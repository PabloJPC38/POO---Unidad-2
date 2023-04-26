from os import path
from csv import reader
from modulo1 import Viajero

class Archivo:
    
    @staticmethod
    def leerArchivo() -> list[Viajero]:
        
        viajeros:list[Viajero] = []
        
        with open(path.dirname(__file__)+ "/viajero.txt","r",encoding="utf8") as file:
        
            return list(map(lambda lista: Viajero(int(lista[0]),int(lista[1]),str(lista[2]),str(lista[3]),float(lista[4])),reader(file,delimiter=",")))
    
    @staticmethod
    def mayorMillas(viajeros : list[Viajero]):
        
        
        mayores = [viajero for viajero in viajeros if viajero > 3000]
        
        print("Los viajeros con mayor cantidad de millas son:")
        
        for mayor in mayores:
            
            print(f"{mayor.getNbre()} {mayor.getApe()}")
            
    
    @staticmethod
    def menu(viajeros : list[Viajero]):
        
        print("1 - Determinar el/los viajero/s con mayor cantidad de millas acumuladas")
        print("2 - Acumular Millas")
        print("3 - Canjear Millas")
        print("4 - Salir")
        
        op = int(input("Ingrese opción:"))        
        while(op != 4):
            
            if op == 1:
                
                Archivo.mayorMillas(viajeros)
                
            if op == 2:
                
                i = [viajero.getNum() for viajero in viajeros].index(int(input("Ingrese número de viajero:")))
                viajeros[i] += float(input("Ingrese cantidad de millas:"))
                print(f"Millas acumuladas:{viajeros[i].getMillas()}")
                
            if op == 3:
                
                i = [viajero.getNum() for viajero in viajeros].index(int(input("Ingrese número de viajero:")))
                viajeros[i] -= float(input("Ingrese cantidad de millas:"))
                print(f"Millas acumuladas:{viajeros[i].getMillas()}")
                
            print()
            print("1 - Determinar el/los viajero/s con mayor cantidad de millas acumuladas")
            print("2 - Acumular Millas")
            print("3 - Canjear Millas")
            print("4 - Salir")
        
            op = int(input("Ingrese opción:")) 