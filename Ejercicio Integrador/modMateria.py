from datetime import datetime

class Materia:
    
    def __init__(self, dni : int, materia : str, fecha : str, nota : float, aprob : str):
        
        self.__dni = dni
        self.__materia = materia
        self.__fecha = Materia.date(fecha)
        self.__nota = nota
        self.__aprob = aprob
    
    def getDni(self):
        
        return self.__dni
    
    def getMateria(self):
        
        return self.__materia
    
    def getNota(self):
        
        return self.__nota
    
    def getFecha(self):
        
        return self.__fecha
    
    def getAprob(self):
        
        return self.__aprob
    
    @staticmethod
    def date(fecha_str):
        
        fecha = datetime.strptime(fecha_str,'%d/%m/%Y')
        fecha_sin_hora = fecha.strftime('%d/%m/%Y')
        return fecha_sin_hora
        