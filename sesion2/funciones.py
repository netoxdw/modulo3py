# def hola_mundo():
#     print('Hola mundo')
# hola_mundo()

# def saludo(perosna):
#     print(f'hola {perosna}')
# saludo('neto')

# def calcular_area (base, altura):
#     area = base * altura
#     return area
# b = 5
# h = 4
# area = calcular_area(b, h)

# def area_rectangulo(base, altura):
#     area = base * altura
#     return area


# area = area_rectangulo(5, 3)
# print(area)

# Reto 7

def mcm  (x, y):
    z = max(x, y)

    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        z += 1

x = 22
y = 8

print(f"El minimo comun multipo de {x} y {y} es {mcm(x, y)}")


