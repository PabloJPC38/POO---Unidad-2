from modMenu import Menu
from ctrlAlumno import ctrlAlu
from ctrlMateria import ctrlMat
from os import path


if __name__ == "__main__":
    
    Alumnos = ctrlAlu(path.dirname(__file__)+ "/alumnos.csv")
    Materias = ctrlMat(path.dirname(__file__)+ "/materiasAprobadas.csv")
    Menu.menu(Alumnos, Materias)