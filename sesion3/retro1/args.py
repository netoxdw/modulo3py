
def suma_multiplicacion(operacion, *args):
    """
    mi primer docstring
    """
    valor = 0
    if operacion == "*":
        valor=1
    for n in args:
        if operacion == "*":
            valor *= n

        elif operacion =="+":
            valor += n

    return valor

# suma= suma_multiplicacion("+", 5, 5, 5)
# multiplicacion= suma_multiplicacion("*", 5, 5, 5)

# print(f"resultado de la suma {suma}, resultado de la multiplicacion { multiplicacion}")

help(suma_multiplicacion)