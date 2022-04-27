class Animal:
    _totalAnimales = 0
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

# GET & SET #

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero
    
    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona = zona
    
    def getZona(self):
        return self._zona
    
# METODOS #

    def movimiento():
        pass
    
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return ("Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\nAves : " + str(Ave.cantidadAves()) + '\nReptiles : ' + str(Reptil.cantidadReptiles()) + '\nPeces : ' + str(Pez.cantidadPeces()) + '\nAnfibios : ' + str(Anfibio.cantidadAnfibios()))
    
    def toString(self):
        if self._zona is None:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()
        else:            
            return "Mi nombre es" + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
