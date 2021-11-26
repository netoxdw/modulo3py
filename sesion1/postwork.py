# Calculadora de intereses de una tarjeta de credito

print('Ingrese los siguientes datos.')

print('Nombre de la tarjeta:')
tarjeta = input ()


print('Tasa de interes:')
ti = float(input ())/100
im = ti/12

print('Deuda:')
deudaparcial = float(input ())
deudatotal = deudaparcial * (1 + im)

print(f'Deuda total:{deudatotal}')

print('Monto de pago:')
pago = float(input())

if  pago <= deudatotal:
    print('Gracias por tu pago')
else:
    print('El pago es mayor a lo adeudado')

diferencia = deudatotal - pago
nueva_deuda = diferencia * (1+im)
print(f'Nueva deuda: ${nueva_deuda}')


