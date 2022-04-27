from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    # GET & SET #

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    
    def isVenenoso(self):
        return self._venenoso

    # METODOS #

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        newFrog = Anfibio(nombre, edad, "selva", genero , "rojo", True)
        cls.ranas += 1
        return newFrog

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        newSalamander = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return newSalamander
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)  