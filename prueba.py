# Facundo Uccelli 
# Facucce185@gmail.com
import csv
import os

'''               Agenda de telefonos
 este programa le permitira,
 1) Consultar Contactos
 2) Añadir contactos
 3) Modificar contactos
 4) Eliminar Contactos'''


csvfile = open('prueba.csv')
contactos = list(csv.DictReader(csvfile))

def consultar():
    telefono = input('Ingrese su telefono: ')
    csvfile = open('prueba.csv')
    contactos = list(csv.DictReader(csvfile))
    contador = 0
    for contacto in contactos:
        if contacto['telefono'] == telefono:
            contador += 1
            print('Nombre del Contacto:', contacto['nombre'])
            print('Numero de telefono:', contacto['telefono'])
    if contador == 0:
        print('Numero no existente')
            
def anadir():
    csvfile = open('prueba.csv')
    contactos = list(csv.DictReader(csvfile))

    nuevo_telefono = input('Ingrese el telefono: ')
    nuevo_nombre = input('Ingrese el nombre: ')
    nuevo_contacto = {}
    contador = 0
    for contacto in contactos:
        if contacto['telefono'] == nuevo_telefono:
            contador += 1
            print('El numero ya existe para un contacto.')
    if contador == 0:
        nuevo_contacto['telefono'] = nuevo_telefono
        nuevo_contacto['nombre'] = nuevo_nombre
        print('El contacto fue añadido.')

    csvfile.close()

    with open('prueba.csv', 'r') as csvfile:
        file_has_data = csvfile.read(1)

    with open('prueba.csv', 'a', newline='') as csvfile:
        headers = ['telefono', 'nombre']
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        if not file_has_data:
            writer.writeheader()

        writer.writerow(nuevo_contacto)
        csvfile.close()

def modificar():
    csvfile = open('prueba.csv')
    contactos = list(csv.DictReader(csvfile))

    contador = 0
    suma = 0
    contacto_borrar = (input('Ingresar el numero a modificar: '))
    for contacto in contactos:
        contador += 1
        if contacto['telefono'] == contacto_borrar:
            suma += 1
            del contactos[contador-1]
    if suma == 0:
        print('Numero no existente')

    csvfile.close()

    csvfile = open('prueba.csv', 'w', newline='')
    header = ['telefono', 'nombre']

    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(contactos)
    csvfile.close()

    nuevo_telefono = input('Ingrese el telefono: ')
    nuevo_nombre = input('Ingrese el nombre: ')
    nuevo_contacto = {}

    nuevo_contacto['telefono'] = nuevo_telefono
    nuevo_contacto['nombre'] = nuevo_nombre

    print('El contacto fue modificado.')

    with open('prueba.csv', 'r') as csvfile:
        file_has_data = csvfile.read(1)

    with open('prueba.csv', 'a', newline='') as csvfile:
        headers = ['telefono', 'nombre']
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        if not file_has_data:
            writer.writeheader()

        writer.writerow(nuevo_contacto)
        csvfile.close()

    
def borrar():
    csvfile = open('prueba.csv')
    contactos = list(csv.DictReader(csvfile))
    contador = 0
    suma = 0
    contacto_borrar = (input('Ingresar el numero a borrar: '))
    for contacto in contactos:
        contador += 1
        if contacto['telefono'] == contacto_borrar:
            suma += 1
            del contactos[contador-1]
            print('El contacto fue borrado.')
    if suma == 0:
        print('Numero no existente')

    csvfile.close()

    csvfile = open('prueba.csv', 'w', newline='')
    header = ['telefono', 'nombre']

    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(contactos)
    csvfile.close()

def salir():
    print('SALIR')        


if __name__ == "__main__":
    print('AGENDA DE CONTACTOS')

    opcion = 0

   
    while opcion != 5:
        print()
        print('AGENDA DE CONTACOS')
        print('<>'*20)
        print('1) Consultar')
        print('2) Anadir')
        print('3) Modificar')
        print('4) Eliminar')
        print('5) Salir')
        print('<>'*20)

        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            consultar()
        if opcion == 2:
            anadir() 
        if opcion == 3:
            modificar()
        if opcion == 4:
            borrar()
        if opcion == 5:
            salir()