

class Ventana:
    
    def __init__(self, title: str = "", xsi: int = 0, ysi: int = 0, xid: int = 1, yid: int = 1):
        
        self.__title = title
        self.__xsi = xsi
        self.__ysi = ysi
        self.__xid = xid
        self.__yid = yid
        
        self.__validarPuntos()
    
    def __validarPuntos(self) -> None:
        
         if (self.__xsi < 0 or self.__ysi < 0 or
             self.__xid > 500 or self.__yid > 500 or
             self.__xsi > self.__xid or self.__ysi > self.__yid):
             
             print("Las coordenadas de los puntos no son válidas")
        
    def getTitulo(self):
        
        return self.__title
    
    def mostrar(self):
        
        print(f"Titulo: {self.__title}  Vértice superior X e Y izquierdo:({self.__xsi},{self.__ysi}) - Vértice inferior X e Y derecho:({self.__xid},{self.__yid})")

    def alto(self):

        return self.__yid - self.__xsi

    def ancho(self):
        
        return self.__xsi + self.__xid

    def moverDerecha(self, desplazamiento = 1):
        
        self.__xsi += desplazamiento
        self.__xid += desplazamiento
        
        self.__validarPuntos()
    
    def moverIzquierda(self, desplazamiento = 1):
        
        self.__xsi -= desplazamiento
        self.__xid -= desplazamiento

        self.__validarPuntos()
    
    def bajar(self,desplazamiento = 1):
        
        self.__ysi -= desplazamiento
        self.__yid -= desplazamiento
        
        self.__validarPuntos()
    
    def subir(self, desplazamiento = 1):
        
        self.__ysi += desplazamiento
        self.__yid += desplazamiento
        
        self.__validarPuntos()