def promedio(a, b):
    try:
        return (a+b)/2
    except NameError:
        print('Datos no validos')
        return 0
    except TypeError:
        print('Datos invalidos')
        return 0 
    except:
        print('ocurrio un errro')
        return 0

print(promedio(1, 5))
