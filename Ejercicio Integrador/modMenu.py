from ctrlAlumno import ctrlAlu
from ctrlMateria import ctrlMat
import numpy as np



class Menu:
    
    @staticmethod
    def menu(ctrlAlumno : ctrlAlu, ctrlMateria : ctrlMat):
        
        print("1 - Informar promedio con aplazos y sin aplazos de un alumno")
        print("2 - Informar los estudiantes que aprobaron en forma promocional, con nota mayor o igual que 7")
        print("3 - Obtener un listado de alumnos ordenado")
        print("4 - Salir")
        
        op = int(input("Elegir opción:"))
        
        while(op != 4):
            
            if op == 1:
                
                ctrlMateria.promedio(int(input("Ingrese dni:")))

            if op == 2:
                
                ctrlMateria.promocional(input("Ingrese materia:"), ctrlAlumno)
            
            if op == 3:
                
                arreglo_ordenado = np.array(sorted(ctrlAlumno.getAlumnos()))
                
                for alumno in arreglo_ordenado:
                    
                    print(alumno)

            
            print("1 - Informar promedio con aplazos y sin aplazos de un alumno")
            print("2 - Informar los estudiantes que aprobaron en forma promocional, con nota mayor o igual que 7")
            print("3 - Obtener un listado de alumnos ordenado")
            print("4 - Salir")
        
            op = int(input("Elegir opción:"))
        