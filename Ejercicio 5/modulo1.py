

class PlanAhorro:
    
    __cant_cuotas = 0
    __cant_licitar = 0
    
    def __init__(self, cod, modelo, vers, valor, cant_cuotas, cant_licitar) -> None:
        
        self.__cod = cod
        self.__modelo = modelo
        self.__vers = vers
        self.__valor = valor
        self.__cant_cuotas = cant_cuotas
        self.__cant_licitar = cant_licitar

    def getCod(self):
        
        return self.__cod
    
    def getModelo(self):
        
        return self.__modelo
    
    def getVers(self):
        
        return self.__vers
    
    def getValor(self):
        
        return self.__valor
    
    def getCant_Cuotas(self):
        
        return self.__cant_cuotas
    
    def getCant_Cuotas_Licitar(self):
        
        return self.__cant_licitar
        
    def setValor(self, valor : float):
        
        self.__valor = valor
    
    def setCuotas_Licitar(self, cant):
        
        self.__cant_licitar = cant
    
    def valorCuota(self):
        
        return (self.__valor / self.__cant_cuotas) + self.__valor * 0.1
    