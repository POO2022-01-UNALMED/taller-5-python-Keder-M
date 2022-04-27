from zooAnimales.animal import Animal
class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantiadAletas = cantidadAletas
        Pez._listado.append(self) 

    # GET & SET #
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantiadAletas

    def setCantiadAletas(self, cantidadAletas):
        self._cantiadAletas = cantidadAletas

    # METODOS #

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        newSalmon = Pez(nombre, edad, "oceano", genero, "rojo", 6,)
        cls.salmones += 1
        return newSalmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        newCod = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return newCod
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado) 

    