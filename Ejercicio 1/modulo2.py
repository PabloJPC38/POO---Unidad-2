from modulo1 import Email
from os import path

class Archivo:
     
    @staticmethod   
    def leerArchivo():
        
        emails:list[Email]=[]
    
        with open(path.dirname(__file__)+ "/cuentas.txt","r",encoding="utf8") as file:
        
            cuentas = file.readline().split(",")

        
            for cuenta in cuentas:
            
            
            
                if cuenta.count('@') == 1 and cuenta.count('.') == 1 and cuenta.find('@') < cuenta.find('.'):
                
                    emails.append(Email.crearCuenta(cuenta))

                else:
                
                    print(f"{cuenta} no es una dirección válida")
    
    
        
        dom = input("Ingrese dominio:")
        c = 0
        for email in emails:
        
            if email.getDominio() == dom:
            
                c+=1
        
        print(f"Hay {c} cuentas con el dominio {dom}")   
        
        """
        print()
        print("Cuentas creadas:")    
        for email in emails:
        
            print(email.retornaEmail())"""

