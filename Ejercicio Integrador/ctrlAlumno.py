from modAlumno import Alumno
from csv import reader
import numpy as np


class ctrlAlu:
    
    def __init__(self, ruta : str) -> None:
        
        self.__alumnos = ctrlAlu.leerArchivo(ruta)
    
    def getAlumnos(self):
        
        return self.__alumnos
    
    @staticmethod
    def dimension(ruta: str):
        with open(ruta, "r", encoding="utf8") as file:
            # Saltar la primera línea (header)
            next(file)
        
            # Contar la cantidad de líneas restantes
            lineas = sum(1 for _ in file)
        
            return lineas

            
    @staticmethod
    def leerArchivo(ruta: str):

        # Obtener la dimensión del archivo CSV
        dim = ctrlAlu.dimension(ruta)

        # Crear un arreglo vacío de tipo object con la dimensión obtenida
        alumnos = np.empty(dim, dtype=object)

        with open(ruta, "r", encoding="utf-8", errors="ignore") as file:
            # Saltar la primera línea (header)
            next(file)

            # Leer línea por línea y crear objetos de la clase Alumno
            for i, line in enumerate(file):
                # Dividir la línea por el delimitador ';'
                values = line.strip().split(';')

                # Crear un objeto Alumno con los valores de la línea
                alumno = Alumno(values[0], values[1], values[2], values[3], values[4])

                # Guardar el objeto Alumno en el arreglo de NumPy
                alumnos[i] = alumno

        return alumnos
