class Zoologico:
    def __init__(self, nombre = None, ubicacion = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []    
    
    # GET & SET #
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setZona(self, zonas):
        self._zonas = zonas
    
    def getZona(self):
        return self._zonas

    # METODOS #

    def agregarZonas(self, nzona):        
        self._zonas.append(nzona)
    
    def cantidadTotalAnimales(self):
        total = 0
        for i in range(len(self._zonas)):
            total += self._zonas[i].cantidadAnimales()
        return total
