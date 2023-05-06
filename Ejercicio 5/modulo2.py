from modulo1 import PlanAhorro
from os import path
from csv import reader

class CtrlPA:
    
    @staticmethod
    def leerArchivo():
        
        autos :list[PlanAhorro] = []
        
        with open(path.dirname(__file__) + "/planes.csv","r",encoding = "utf8") as file:
            
            for i, line in enumerate(file):
                # Dividir la línea por el delimitador ';'
                values = line.strip().split(';')

                auto = PlanAhorro(values[0], values[1], values[2], float(values[3]))
                auto.setCuotas(int(values[4]))
                auto.setCuotasLicitar(int(values[5]))
                autos.append(auto)
            
            return autos
        
    @staticmethod
    def cuotaInferior(datos: list[PlanAhorro], valor):
        
        for dato in datos:

            if dato.valorCuota() < valor:
                
                print(f"{dato.getCod()} - {dato.getModelo()} - {dato.getVers()}")
                
    @staticmethod
    def menu(datos: list[PlanAhorro]):
        
        print("1 - Actualizar el valor del vehículo de cada plan")
        print("2 - Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado")
        print("3 - Mostrar el monto que se debe haber pagado para licitar el vehículo")
        print("4 - Modificar la cantidad cuotas que debe tener pagas para licitar")
        print("5 - Salir")
        
        op = int(input("Ingrese opción:"))
        
        while(op != 5):
            
            if op == 1:
            
                for dato in datos:
                
                    print(f"{dato.getCod()} - {dato.getModelo()} - {dato.getVers()}")
                    dato.setValor(float(input("Ingrese nuevo valor para el vehículo:")))
                    print(f"{dato.getCod()} - {dato.getModelo()} - {dato.getVers()} - {dato.getValor()}")
                    print()
        
            if op == 2:
                
                CtrlPA.cuotaInferior(datos,float(input("Ingrese valor de cuota:")))
            
            if op == 3:
                
                for dato in datos:
                    
                    print(f"Para el {dato.getModelo()} - {dato.getVers()} el monto a pagar para licitarlo es de ${dato.getCant_Cuotas_Licitar() * dato.valorCuota()}")
            
            if op == 4:
                
                i = [dato.getCod() for dato in datos].index(input("Ingrese código del plan:"))
                
                datos[i].setCuotasLicitar(int(input("Ingrese nueva cantidad de cuotas para licitar:")))
                print(f"Cantidad de cuotas a licitar:{datos[i].getCant_Cuotas_Licitar()}")
            
            print()
            print("1 - Actualizar el valor del vehículo de cada plan")
            print("2 - Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado")
            print("3 - Mostrar el monto que se debe haber pagado para licitar el vehículo")
            print("4 - Modificar la cantidad cuotas que debe tener pagas para licitar")
            print("5 - Salir")
            
            op = int(input("Ingrese opción:"))