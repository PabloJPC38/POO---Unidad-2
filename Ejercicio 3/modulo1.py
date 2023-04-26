

class Registro:
    
    def __init__(self,temp:float, humed:float, pres:float) -> None:
        
        self.__temp = temp
        self.__humed = humed
        self.__pres = pres
    
    def getTemp(self):
        
        return self.__temp
    
    def getHumed(self):
        
        return self.__humed
    
    def getPres(self):
        
        return self.__pres
        