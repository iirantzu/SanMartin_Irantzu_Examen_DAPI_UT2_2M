def funcion_general(check_DDBB):
    '''Función que permite chequar y corregir los datos de usuarios morosos almacenados en una base de datos de morosidad (DDBB).
    -Parametros:
    lista'''

lista = [{"nombre": "usr1_name", "apellidos": "usr1_surname", "nif": "usr1_nif"},
 {"nombre": "usr2_name", "apellidos": "usr2_surname", "nif": "usr2_nif"},
 {...},
 {"nombre": "usrn_name", "apellidos": "usrn_surname", "nif": "usrn_nif"}]

nombre = input("¿Cual es el nombre del moroso?\n")
apellido = input("Cual es el apellido del moroso?\n")
nif = input("Cual es el nif del moroso con el formato NNNNNNNNL (Donde N = Números y L = Letra en mayuscula)?\n")

def primera_función(check_username):
    '''Función que comprueba el nombre y apellidos estén en formato capitalizado o CamelCase
    -Parametros:
    nombre
    apellidos'''
nombre_corregido = (nombre.replace(nombre, nombre.title()))
apellido_corregido = (apellido.replace(apellido, apellido.title()))
print("Los datos correctos son " + str(nombre_corregido) + " " + str(apellido_corregido))

def segunda_función(check_nif):
    '''Funcion que hace la comprobación matematica para determinar si el número nif corresponde con la letra asociada
    -Parametro:
    nif_usuario'''

