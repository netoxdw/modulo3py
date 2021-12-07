class vehiculo:
    def __init__(self, ruedas = 0, velocidad = 'media', medio = 'asfalto' ):
        self.__ruedas = ruedas
        self.__velocidad = velocidad
        self.__medio = medio

    def avanzar(self):
        print(f'El vehiculo se mueve a{self.__velocidad}')

    def __str__(self):
        return f'ruedas{self.__ruedas} velocidad:{self.__velocidad} medio:{self.__medio}'
    def argumentos(self):
        print(f'el vehiculo tiene {self.__ruedas} ruedas')
        print(f'el vehiculo se mueve a velocidad {self.__velocidad}')
        print(f'el vehiculo se mueve por {self.__medio}')

class Vehiculo_terrestre(vehiculo):
    def __init__(self, ruedas=0, velocidad='no se mueve'):
        super().__init__(ruedas, 'tierra', velocidad)
    def estacionarse(self):
        print("El vehiculo está estacionado")
    def avanzar(self):
        print('El vehiculo avanza por la carretera')

class Vehiculo_acuatico(vehiculo):
    def __init__(self, velocidad='no se mueve'):
        super().__init__(0, 'agua', velocidad)
    def undirse(self):
        print("El vehiculo se undió")
    def avanzar(self):
        print('El vehiculo avanza por el mar')

class Vehiculo_aereo(vehiculo):
    def __init__(self, ruedas=0, velocidad='no se mueve'):
        super().__init__(ruedas, 'aire', velocidad)
    def despegar(self):
        print("El vehiculo está despegando")
    def avanzar(self):
        print('El vehiculo avanza por el cielo')

barco = Vehiculo_acuatico(velocidad='lenta')

avion = Vehiculo_aereo(ruedas=4,velocidad='rapida')

auto = Vehiculo_terrestre(ruedas=4,velocidad='media')

auto.avanzar()
barco.avanzar()
avion.avanzar()