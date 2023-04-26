from modulo1 import Conjunto

class Menu:
    
    @staticmethod
    def menu():
        
        c1, c2 = Conjunto([1,2,3,4]), Conjunto([3,6,9])
        
        print("1 - Unión de conjuntos")
        print("2 - Diferencia de conjuntos")
        print("3 - Comparar conjuntos")
        print("4 - Salir")
        
        op = int(input("Ingrese opción:"))
        
        while op != 4:
            
            if op == 1:
            
                print(f"La unión de los conjuntos es {c1 + c2}")
        
            if op == 2:
            
                print(f"La diferencia de los conjuntos es {c1 - c2}")
        
            if op == 3:
            
                if c1 == c2:
                
                    print("Los conjuntos son iguales")
            
                else: 
                
                    print("Los conjuntos no son iguales")

            print("1 - Unión de conjuntos")
            print("2 - Diferencia de conjuntos")
            print("3 - Comparar conjuntos")
            print("4 - Salir")
        
            op = int(input("Ingrese opción:"))