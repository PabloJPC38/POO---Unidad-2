from modulo1 import Email
from modulo2 import Archivo


if __name__ == '__main__' :
    
    nombre = input("Ingrese nombre:")
    e1 = Email(input("Ingrese id:"),
                input("Ingrese dominio:"),
                input("Ingrese tipo de dominio:"),
                input("Ingrese contraseña:")
                )

    print()
    e1.mensaje(nombre)
    print()
    print("Se requiere cambiar contraseña...")
    e1.cambiarContraseña()
    
    e2 = Email.crearCuenta(input("Ingrese dirección de correo:"))
    print(e2.retornaEmail() + " creado!!") 
    
    Archivo.leerArchivo()
    
    
    
         
            

    
