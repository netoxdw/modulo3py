# Calculadora de intereses de una tarjeta de credito

print('Ingrese los siguientes datos.')
print('Nombre de la tarjeta:')
tarjeta = input ()
print('Tasa de interes en :')
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

# my_dict_tarjeta = {
#     'Tarjeta': tarjeta,
#     'Tasa de interes': ti,
#     'Credito':deudaparcial,
#     'Deuda':deudatotal,
#     'Pago mensual': pago
# }

# print(my_dict_tarjeta)