# class vehiculo:
#     def argumentos(self):
#         print(f'el {self.tipo} tiene {self.ruedas} rudeas')
#         print(f'velocidad  {self.velocidad}')
#         print(f'viaja por {self.medio}')


# barco = vehiculo()
# barco.tipo = 'barco'
# barco.ruedas = 0
# barco.velocidad = 'lento'
# barco.medio = 'agua'
# barco.argumentos()


# Avion = vehiculo()
# Avion.tipo = 'Avion'
# Avion.ruedas=3
# Avion.velocidad='rapido'
# Avion.medio = 'aire'
# Avion.argumentos()

# auto = vehiculo()
# auto.tipo = 'auto'
# auto.ruedas=4
# auto.velocidad='media'
# auto.medio = 'asfalto'
# auto.argumentos()

class vehiculo:
    def __init__(self, ruedas = 0, velocidad = 'media', medio = 'asfalto' ):
        self.__ruedas = ruedas
        self.__velocidad = velocidad
        self.__medio = medio

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

class Vehiculo_acuatico(vehiculo):
    def __init__(self, velocidad='no se mueve'):
        super().__init__(0, 'agua', velocidad)
    def undirse(self):
        print("El vehiculo se undió")

class Vehiculo_aereo(vehiculo):
    def __init__(self, ruedas=0, velocidad='no se mueve'):
        super().__init__(ruedas, 'aire', velocidad)
    def despegar(self):
        print("El vehiculo está despegando")

barco = Vehiculo_acuatico(velocidad='lenta')

avion = Vehiculo_aereo(ruedas=4,velocidad='rapida')

auto = Vehiculo_terrestre(ruedas=4,velocidad='media')

# barco.argumentos()
# avion.argumentos()
# auto.argumentos()
# print(auto)

auto.estacionarse()
avion.despegar()
barco.undirse()