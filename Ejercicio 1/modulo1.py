

class Email:
    
    def __init__(self,idCuenta,dominio,tipoDom,password = None) -> None:
        
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDom = tipoDom
        self.__password = password
    
    def retornaEmail(self) -> str:
        
        return (self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDom)

    def getDominio(self):
        
        return self.__dominio
    
    def mensaje(self, nombre):
        
        print (f"Estimado {nombre} te enviaremos tus mensajes a la dirección {self.retornaEmail()}")


    def cambiarContraseña(self):
        
        pw = input("Ingrese contraseña actual:")
        
        while(pw != self.__password):
            
            pw = input("Ingrese contraseña actual:")
        
        pw = input("Ingrese nueva contraseña:")
        
        self.__password = pw
        
        print(f"Su nueva contraseña es {self.__password}")
    
    @staticmethod
    def crearCuenta(direct:str):
        
        cuenta = direct.replace('@',' ').replace('.',' ').split()
        
        return Email(cuenta[0],cuenta[1],cuenta[2])