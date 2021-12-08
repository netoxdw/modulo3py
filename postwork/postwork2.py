# Funcion crear_tarjeta que devuelve un diccionario
def crear_tarjeta(nombre, cliente,
tipo_tarjeta, t_tarjeta,
tasa_interes, ti,
deuda, deuda_total,
monto_pago, pago
):
    tarjeta = {}
    tarjeta [nombre] = cliente
    tarjeta [tipo_tarjeta] = t_tarjeta
    tarjeta [tasa_interes] = ti
    tarjeta [deuda] = deuda_total
    tarjeta [monto_pago] = pago

    return tarjeta

# Solicitud de datos
print('Ingrese los siguientes datos')
print('Nombre:')
Nombre = input()

print('Tipo de tarjeta:')
Tarjeta = input()

print('Tasa de inetres:')
ti =float(input())
im = (ti/12)/100

print('Deuda:')
deuda_parcial = float(input())
deuda_total = deuda_parcial * (1 + im)

print('Monto de pago:')
pago = float(input())

mi_tarjeta =  crear_tarjeta(
    'Cliente', Nombre,
    'Tipo de tarejta', Tarjeta,
    'Tasa de interes', ti,
    'Deuda total', deuda_total,
    'pago', pago
)
print(mi_tarjeta)


