
def crear_tarjeta(nombre, tarjeta, interes, deuda, deudatoal, pago, nueva_deuda):
    my_dic_tarjeta = {
        'Nombre':nombre,
        'Tarjeta': tarjeta,
        'Tasa de interes': interes,
        'Deuda': deuda,
        'Deuda total': deudatotal,
        'Pago mensual': pago,
        'Nueva deuda':nueva_deuda
    }
    return my_dic_tarjeta

print(f'Ingresa los siguientes datos.\n ¿Cual es su nombre')
name = input()
print('Tipo de tarjeta:')
tipo_tarjeta = input()
print('Tasa de interes')
ti = float(input ())
im = (ti/12)/100
print('Deuda:')
deudaparcial = float(input ())
deudatotal = deudaparcial * (1 + im)
print(f'Deuda total:{deudatotal}')
print('Monto de pago:')
pago = float(input())

if  pago <= deudatotal:
    print('Gracias por tu pago')
    diferencia = deudatotal - pago
    nueva_deuda = diferencia * (1+im)
    print(f'Nueva deuda: ${nueva_deuda}')
else:
    print('El pago es mayor a lo adeudado, por favor, ingresa nuevamente los datos')


print(crear_tarjeta(name, tipo_tarjeta, ti, deudaparcial, deudatotal, pago, nueva_deuda))




