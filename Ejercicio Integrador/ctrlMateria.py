from modMateria import Materia
from csv import reader
from ctrlAlumno import ctrlAlu


class ctrlMat:
    
    def __init__(self, ruta : str) -> None:
        
        self.__materias = ctrlMat.leerArchivo(ruta)
    
    def promedio(self, dni : int):
        
        nota1 = [materia.getNota() for materia in self.__materias if materia.getDni() == dni and materia.getNota() >= 4]
        nota2 = [materia.getNota() for materia in self.__materias if materia.getDni() == dni]
        
        print(f"Promedio sin aplasos:{sum(nota1) / len(nota1)} - Promedio con aplasos:{sum(nota2) / len(nota2)}")

    def promocional(self, nbre : str, ctrlA : ctrlAlu ):
        
        print("DNI      Apellido y nombre   Fecha       Nota  Año que cursa")
        
        for materia in self.__materias:
            
            if materia.getMateria() == nbre and materia.getAprob() == 'P' and materia.getNota() >= 7:
                
                for alu in ctrlA.getAlumnos():
                    
                    if materia.getDni() == alu.getDni():
                        
                        print(f"{materia.getDni()} {alu.getApe()} {alu.getNbre()}    {materia.getFecha()}   {materia.getNota()}         {alu.getAnio()}")

    @staticmethod
    def leerArchivo(ruta : str):
        
        with open(ruta, "r", encoding = "utf-8", errors = "ignore") as file:
            
            next(file)
            return list(map(lambda l: Materia(int(l[0]), l[1], l[2], float(l[3]), l[4]), (reader(file, delimiter = ";"))))