from __future__ import annotations

class Viajero:
    
    def __init__(self, num, dni:int, nbre:str, ape:str, millas_acum:float) -> None:
        
        self.__num = num
        self.__dni = dni
        self.__nbre = nbre
        self.__ape = ape
        self.__millas_acum = millas_acum
    
    def getNum(self):
        
        return self.__num
    
    def getMillas(self) -> float:
        
        return self.__millas_acum
    
    def getNbre(self) -> str:
        
        return self.__nbre
    
    def getApe(self) -> str:
        
        return self.__ape
    
    def cantidadTotaldeMillas(self):
        
        return self.__millas_acum
    
    def acumularMillas(self, millas):
        
        self.__millas_acum += millas

        return self.__millas_acum

    def canjearMillas(self, millas) -> float:
        
        if self.__millas_acum > millas:
            
            self.__millas_acum -= millas
            return self.__millas_acum
        
        else:
        
            print("La cantidad de millas sobrepasa a las acumuladas")
            return self.__millas_acum
    
    def __gt__(self, other : float):
        
        return self.__millas_acum > other
    
    def __add__(self, millas) -> Viajero:
        
        self.acumularMillas(millas)
        
        return self

    def __radd__(self, millas) -> Viajero:
        
        self.acumularMillas(millas)
        
        return self
    
    def __sub__(self, other):
        
        self.canjearMillas(other)
        
        return self

    def __rsub__(self, millas):
        
        return self - millas

    def __eq__(self, other):
        
        if type(other) == Viajero:
            
            return self.__millas_acum == other
        
        elif type(other) == int:
            
            return self.__millas_acum == other
        
        else:
            
            raise TypeError("No se puede comparar")
            