from os import path
from csv import reader
from modulo1 import Registro
from typing import List

class Archivo:
    
    @staticmethod
    def construirLista():
        
        lista=[]

        for i in range(30):
            
            lista.append([0]*24)
        
        return lista
    
    @staticmethod
    def leerArchivo():
        
        Datos = Archivo.construirLista()
        
        with open(path.dirname(__file__)+ "/mes.csv","r", encoding="utf8") as arch:
    
            fila = reader(arch)
    
            for f in fila:
            
                Datos[int(f[0])-1][int(f[1])-1]=(Registro(float(f[2]),float(f[3]),float(f[4])))

        return Datos
    
    
    @staticmethod
    def mayorYmenor_H(Datos:List[List[Registro]]):
        
        mayor, menor, d1, d2, h1, h2 = Datos[0][0].getHumed(),Datos[0][0].getHumed(),0,0,0,0
        
        for i, fila in enumerate(Datos):
            
            for j, registro in enumerate(fila):
                
                if registro.getHumed() > mayor:
                    
                    mayor = registro.getHumed()
                    d1 = i
                    h1 = j
                if registro.getHumed() < menor:
                    
                    menor = registro.getHumed()
                    d2 = i
                    h2 = j
        
        print(f"La mayor humedad ocurrió el día {d1+1} a las {h1+1} horas")
        print(f"La menor humedad ocurrió el día {d2+1} a las {h2+1} horas")
        
    
    @staticmethod
    def mayorYmenor_T(Datos:List[List[Registro]]):
        
        mayor, menor, d1, d2, h1, h2 = Datos[0][0].getTemp(),Datos[0][0].getTemp(),0,0,0,0
        
        for i, fila in enumerate(Datos):
            
            for j, registro in enumerate(fila):
                
                if registro.getTemp() > mayor:
                    
                    mayor = registro.getTemp()
                    d1 = i
                    h1 = j
                if registro.getTemp() < menor:
                    
                    menor = registro.getTemp()
                    d2 = i
                    h2 = j
        
        print(f"La mayor temperatura ocurrió el día {d1+1} a las {h1+1} horas")
        print(f"La menor temperatura ocurrió el día {d2+1} a las {h2+1} horas")
        
    @staticmethod
    def mayorYmenor_P(Datos:List[List[Registro]]):
        
        mayor, menor, d1, d2, h1, h2 = Datos[0][0].getPres(),Datos[0][0].getPres(),0,0,0,0
        
        for i, fila in enumerate(Datos):
            
            for j, registro in enumerate(fila):
                
                if registro.getPres() > mayor:
                    
                    mayor = registro.getPres()
                    d1 = i
                    h1 = j
                if registro.getPres() < menor:
                    
                    menor = registro.getPres()
                    d2 = i
                    h2 = j
        
        print(f"La mayor presión ocurrió el día {d1+1} a las {h1+1} horas")
        print(f"La menor presión ocurrió el día {d2+1} a las {h2+1} horas")
    
    @staticmethod
    def temperatura_promedio_mensual(Datos:List[List[Registro]]):
        
        prom, num_fila, num_colum, hora = 0, len(Datos), len(Datos[0]), 0
        
        for colum in range(num_colum):
            hora = colum
            for fila in range(num_fila):
                
                prom += Datos[fila][colum].getTemp()
                
                
            print(f"Para la hora {hora} la temperatura promedio mensual es {prom/num_fila} ")
            prom = 0
    @staticmethod
    def MostrarDatosDelDia(dia, Datos:List[List[Registro]]):
        
        print("   Hora          Temperatura         Humedad         Presión")
            
        for hora, registro in enumerate(Datos[dia-1]):
            
            print(f"    {hora+1}            {registro.getTemp()}                {registro.getHumed()}               {registro.getPres()}")
        
    
    @staticmethod
    def menu(Datos: List[List[Registro]]):
        
        print("1 - Mostrar para cada variable el día y hora de menor y mayor valor")
        print("2 - Indicar la temperatura promedio mensual por cada hora")
        print("3 - Dado un número de día listar los valores de las tres variables para cada hora del día dado.")
        print("4 - Salir")
        
        op = int(input("Ingrese opción:"))        
        while(op != 4):
            
            if op == 1:
                
                Archivo.mayorYmenor_T(Datos)
                Archivo.mayorYmenor_H(Datos)
                Archivo.mayorYmenor_P(Datos)
                
            if op == 2:
                
                Archivo.temperatura_promedio_mensual(Datos)
            
            if op == 3:
                
                Archivo.MostrarDatosDelDia(int(input("Ingrese día:")),Datos)
            print()
            
            print("1 - Mostrar para cada variable el día y hora de menor y mayor valor")
            print("2 - Indicar la temperatura promedio mensual por cada hora")
            print("3 - Dado un número de día listar los valores de las tres variables para cada hora del día dado.")
            print("4 - Salir")
            op = int(input("Ingrese opción:")) 
    
    
