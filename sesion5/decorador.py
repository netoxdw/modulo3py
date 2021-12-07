def tres_veces(funcion):
    def nueva_funcion ():
        for _ in range(3):
            a = funcion()
        return a
    return nueva_funcion

@tres_veces
def hola_mundo():
    print('Hola mundo')

hola_mundo()

def triple(funcion):
    def nueva_funcion(*args,**kwargs):
        a =''
        for _ in range(3):
            a = funcion(*args, **kwargs)
        return a
    return nueva_funcion

@triple
def hola_mundo():
    print("hola mundo :)")


hola_mundo()