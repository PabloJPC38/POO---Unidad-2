from collections import Counter

class Conjunto:
    
    def __init__(self, elementos : list[int]):
        
        self.__elementos = elementos
    
    def __iter__(self):
        return iter(self.__elementos)
    
    def __add__(self, otro):
        
        nuevo = self.__elementos
        
        for elemento in otro:
            
            if elemento not in self.__elementos:
                
                nuevo.append(elemento)
            
        return nuevo
    
    def __sub__(self, otro):
        
        nuevo = []
        
        for elemento in self.__elementos:
            
            if elemento not in otro:
                
                nuevo.append(elemento)
        
        return nuevo
    
    def __eq__(self, otro):
        
        return  Counter(self.__elementos) == Counter(otro)