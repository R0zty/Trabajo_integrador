# Facundo Uccelli 
# Facucce185@gmail.com
from ast import Try
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
    while True: 
        try:
           telefono = int(input('Ingrese numero de contacto a consultar: '))
           csvfile = open('prueba.csv')
           contactos = list(csv.DictReader(csvfile))
           contador = 0
           for contacto in contactos:
               if int(contacto['telefono']) == telefono:
                  contador += 1
                  print('Nombre del Contacto:', contacto['nombre'])
                  print('Numero del Contacto' , telefono['numero'])

           if contador == 1:
                  break
            
           elif contador == 0:
                print('No existe el contacto')
                break
            
           csvfile.close()
        except:  
          print('Error al ingresar datos')
        
    

def anadir():
    try:
        csvfile = open('prueba.csv')
        contactos = list(csv.DictReader(csvfile))
        csvfile.close()

    
        nuevo_telefono = int(input('Ingrese el telefono: '))
        nuevo_nombre = str(input('Ingrese el nombre: '))

        nuevo_contacto = {}
        contador = 0
        for contacto in contactos:
            if int(contacto['telefono']) == nuevo_telefono:
                contador += 1
                print('El numero ya existe para un contacto.')

            elif contador == 0:
                nuevo_contacto['telefono'] = nuevo_telefono
                nuevo_contacto['nombre'] = nuevo_nombre
                print('El contacto fue añadido.')

             
                with open('prueba.csv', 'a', newline='') as csvfile:
                    headers = ['telefono', 'nombre']
                    writer = csv.DictWriter(csvfile, fieldnames=headers)
                    writer.writerow(nuevo_contacto)

                print('El contacto fue añadido')
                break
                
    except:
        print('Error al ingresar datos, vuelve a intentar.')        
    

def modificar():
    try: 
       csvfile = open('prueba.csv')
       contactos = list(csv.DictReader(csvfile))

       contador = 0
       suma = 0
       contacto_borrar = int(input('Ingresar el numero a modificar: '))
       for contacto in contactos:
          contador += 1
          if int(contacto['telefono']) == contacto_borrar:
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

          nuevo_telefono = int(input('Ingrese el telefono: '))
          nuevo_nombre = str(input('Ingrese el nombre: '))
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
    except:
     print('Error al ingresar datos')
    
def borrar():
 try:
    csvfile = open('prueba.csv')
    contactos = list(csv.DictReader(csvfile))
    contador = 0
    suma = 0
    contacto_borrar = int(input('Ingresar el numero a borrar: '))
    for i in range(len(contactos)):
        if int(contactos[i]['telefono']) == contacto_borrar:       
        
                for k,v in contactos[i].items():
                    if int(v) == contacto_borrar:
                     del contactos[contador-1]
                     
                     print(f'{contactos} fue borrado de la agenda ')
                     
                     if suma == 0:
                        print('numero inexistente')
                        csvfile.close()

                        csvfile = open('prueba.csv', 'w', newline='')
                        header = ['telefono' , 'nombre']

                        writer = csv.DictWriter(csvfile, fieldnames=header)
                        writer.writeheader()
                        writer.writerows(contactos)
                        csvfile.close()
 except:
    print('Error al ingresar datos, intente de nuevo')


def salir():
    print('SALIR')        


if __name__ == "__main__":
    print('AGENDA DE CONTACTOS')

     

    consultando = True
    while consultando:
        print('AGENDA DE CONTACOS')
        print('<>'*20)
        print('1) Consultar')
        print('2) Anadir')
        print('3) Modificar')
        print('4) Eliminar')
        print('5) Salir')
        print('<>'*20)
        
            
        opcion = ""
        while opcion not in ("1", "2", "3", "4", "5"):
            opcion = input("--->")
            if opcion == "1":
             consultar()
            elif opcion == "2":
                anadir () 
            elif opcion == "3":
               modificar()
            elif opcion == "4":
                borrar()
            elif  opcion == "5":
                consultando = False
                print('Finalizo el programa ')
            else:
                print('La opcion ingresada es incorrecta, intente de nuevo')    
                
   