

class PlanAhorro:
    
    __cuotas = 0
    __cuotas_licitar = 0
    
    def __init__(self, cod, modelo, vers, valor) -> None:
        
        self.__cod = cod
        self.__modelo = modelo
        self.__vers = vers
        self.__valor = valor

    def getCod(self):
        
        return self.__cod
    
    def getModelo(self):
        
        return self.__modelo
    
    def getVers(self):
        
        return self.__vers
    
    def getValor(self):
        
        return self.__valor
    
    def getCant_Cuotas(self):
        
        return self.__cuotas
    
    def setValor(self, valor : float):
        
        self.__valor = valor
    
    def valorCuota(self):
        
        return (self.__valor / float(PlanAhorro.__cuotas)) + self.__valor * 0.1
    
    @classmethod
    def setCuotas(cls,cant):
        
        cls.__cuotas = cant

    @classmethod
    def setCuotasLicitar(cls, cant):
        
        cls.__cuotas_licitar = cant

    @classmethod
    def getCuotas(cls):
        
        return cls.__cuotas
    
    @classmethod
    def getCant_Cuotas_Licitar(cls):
        
        return cls.__cuotas_licitar
