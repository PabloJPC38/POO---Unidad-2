from __future__ import annotations

class Alumno:
    
    def __init__(self, dni, ape, nbre, carrera, anio):
        
        self.__dni = int(dni)
        self.__ape = ape
        self.__nbre = nbre
        self.__carrera = carrera
        self.__anio = int(anio)
    
    def getDni(self):
        
        return self.__dni
    
    def getNbre(self):
        
        return self.__nbre
    
    def getApe(self):
        
        return self.__ape
    
    def getAnio(self):
        
        return self.__anio
    
    def __lt__(self, otro: Alumno):
        
        return (self.__anio, self.__ape, self.__nbre) < (otro.__anio, otro.__ape, otro.__nbre)

    def __repr__(self):
        return f"Alumno(dni={self.__dni}, ape={self.__ape}, nbre={self.__nbre}, carrera={self.__carrera}, anio={self.__anio})"