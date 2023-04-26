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
    def menu(viajeros : list[Viajero]):
        
        print("1 - Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero ")
        print("2 - Acumular Millas")
        print("3 - Canjear Millas")
        print("4 - Salir")
        
        op = int(input("Ingrese opción:"))        
        while(op != 4):
            
            if op == 1:
                
                    i = [viajero.getNum() for viajero in viajeros].index(int(input("Ingrese número de viajero:")))
                    valor = int(input("Ingrese un valor a comparar:"))
                    
                    if valor == viajeros[i]:
                        
                        print("Es igual")
                        
                    else:
                        
                        print("No es igual")
                
            if op == 2:
                
                i = [viajero.getNum() for viajero in viajeros].index(int(input("Ingrese número de viajero:")))
                viajeros[i] = float(input("Ingrese cantidad de millas:")) + viajeros[i]
                
                print(f"Millas acumuladas:{viajeros[i].getMillas()}")
                
            if op == 3:
                
                i = [viajero.getNum() for viajero in viajeros].index(int(input("Ingrese número de viajero:")))
                viajeros[i] = float(input("Ingrese cantidad de millas:")) - viajeros[i]
                print(f"Millas acumuladas:{viajeros[i].getMillas()}")
                
            print()
            print("1 - Determinar el/los viajero/s con mayor cantidad de millas acumuladas")
            print("2 - Acumular Millas")
            print("3 - Canjear Millas")
            print("4 - Salir")
        
            op = int(input("Ingrese opción:")) 