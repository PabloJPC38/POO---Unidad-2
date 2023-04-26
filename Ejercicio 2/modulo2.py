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
    def menu(viajero:Viajero):
        
        print("1 - Consultar Cantidad de Millas")
        print("2 - Acumular Millas")
        print("3 - Canjear Millas")
        print("4 - Salir")
        
        op = int(input("Ingrese opción:"))        
        while(op != 4):
            
            if op == 1:
                
                print(f"Tiene acumulado {viajero.cantidadTotaldeMillas()} millas")
            
            if op == 2:
                
                millas = viajero.acumularMillas(float(input("Ingrese cantidad de millas:")))
                print(f"Millas acumuladas:{millas}")
            
            if op == 3:
                
                millas = viajero.canjearMillas(float(input("Ingrese cantidad de millas:")))
                print(f"Millas restantes:{millas}")
    
            print()
            print("1 - Consultar Cantidad de Millas")
            print("2 - Acumular Millas")
            print("3 - Canjear Millas")
            print("4 - Salir")
        
            op = int(input("Ingrese opción:")) 
    
    @staticmethod        
    def Menu(viajeros:list[Viajero], num:int):
        
        
        for  viajero in viajeros:
            
            if viajero.getNum() == num:
                
                Archivo.menu(viajero)

        
                

    