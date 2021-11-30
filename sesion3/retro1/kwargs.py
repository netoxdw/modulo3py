def agenda (**kwargs):
    contactos = sorted(kwargs)

    for contacto in contactos:
        print('contacto', kwargs[contacto])

