import csv

ruta = "C:\\Users\\gabri\\Escritorio\\GIT_gsolaromerEduca\\Sola_Gabriel_Rec_DAPI_UT2_Parte2_2M\\class.csv"

def create_email(ruta):
    '''Función que recibe el nombre y apellido de cada alumno 
    y devuelve una dirección de correo en el dominio de Educación Navarra.
    
    Parámetros:
        - Ruta del archivo CSV que contiene los nombres y apellidos de los alumnos
    
    Salida:
        - Lista de direcciones de correo en el dominio de Educación Navarra'''
    
    correos = []
    with open(ruta, newline='', encoding="UTF-8") as csvfile:
       reader = csv.DictReader(csvfile)
       for fila in reader:
           nombre = fila['Nombre']

           apellido = fila['Apellido']

           primera_letra_nombre = nombre[0].lower()

           cinco_letras_apellido = apellido[:5].lower()

           correo = primera_letra_nombre + cinco_letras_apellido + "@educacion.navarra.es"

           correos.append(correo)

    return correos

lista_correos = create_email(ruta)

print(lista_correos)