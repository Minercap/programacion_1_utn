from .display import *
from .functions import *
from .search import *
from .sort import *
from .validations import *

# Funciones:
# cargar_nombres >>> linea 14
# cargar_generos >>> linea 31
# cargar_legajos >>> linea 49
# cargar_calificaciones >>> linea 90
# cargar_datos >>> linea 120

def cargar_nombres(lista_nombres: list):
    """
    Carga los nombres de los estudiantes en la lista, validando la entrada.

    Args:
        lista_nombres (list): La lista donde se guardarán los nombres.
    """
    num_estudiantes = len(lista_nombres)
    for i in range(num_estudiantes):
        while True:
            nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
            if validar_nombre(nombre) == True:
                lista_nombres[i] = nombre
                break
            else:
                print("Error: El nombre debe ser una cadena de texto.")

def cargar_generos(lista_generos: list):
    """
    Carga los géneros de los estudiantes en la lista, validando la entrada.

    Args:
        lista_generos (list): La lista donde se guardarán los géneros.
    """
    num_estudiantes = len(lista_generos)
    for i in range(num_estudiantes):
        while True:
            genero = input(f"Ingrese el género del estudiante {i + 1} (F/M/X): ")
            genero = convertir_a_mayusculas(genero)
            if validar_genero(genero) == True:
                lista_generos[i] = genero
                break
            else:
                print("Error: El género debe ser F, M o X.")

def cargar_legajos(lista_legajos: list):
    """
    Carga los legajos de los estudiantes en la lista, validando la entrada.

    Args:
        lista_legajos (list): La lista donde se guardarán los legajos.
    """
    num_estudiantes = len(lista_legajos)
    for i in range(num_estudiantes):  
        while True:
            legajo = input(f"Ingrese el legajo del estudiante {i + 1}: ")
            
            # Validar que el legajo no esté vacío, tenga 5 caracteres y todos sean dígitos
            if legajo != "" and len(legajo) == 5:
                es_valido = True
                for i in range(len(legajo)):
                    caracter = legajo[i]
                    if ord(caracter) < ord('0') or ord(caracter) > ord('9'):
                        es_valido = False
                        break
                if es_valido:
                    legajo = int(legajo)  
                    # Verificar si el legajo ya existe en la lista.
                    legajo_existe = False
                    legajo_existe = False
                    for j in range(len(lista_legajos)):
                        if legajo == lista_legajos[j]:
                            legajo_existe = True
                            break
                    if legajo_existe:
                        print("Error: El legajo ya existe. Ingrese un legajo único.")
                    elif validar_legajo(legajo):
                        lista_legajos[i] = legajo
                        break
                    else:
                        print("Error: El legajo no cumple con los criterios adicionales.")
                else:
                    print("Error: El legajo debe contener solo números.")
            else:
                print("Error: El legajo debe ser un número entero de 5 dígitos.")

def cargar_calificaciones(matriz_calificaciones: list):
    """
    Carga las calificaciones de los estudiantes en la matriz, validando la entrada.

    Args:
        matriz_calificaciones (list): La matriz donde se guardarán las calificaciones.
    """
    num_estudiantes = len(matriz_calificaciones)
    num_materias = len(matriz_calificaciones[0])

    for i in range(num_estudiantes):
        for j in range(num_materias):
            while True:
                calificacion = input(f"Ingrese la calificación del estudiante {i + 1} en la materia {j + 1}: ")
                
                # Validar que la calificación no esté vacía y sea un número entre 1 y 10
                if calificacion != "":
                    es_valido = True
                    for caracter in calificacion:
                        if ord(caracter) < ord('0') or ord(caracter) > ord('9'):  # Verifica si no es un dígito
                            es_valido = False
                            break
                    if es_valido and 1 <= int(calificacion) <= 10:  # Verifica el rango
                        matriz_calificaciones[i][j] = int(calificacion)
                        break
                    else:
                        print("Error: La calificación debe ser un número entero entre 1 y 10.")
                else:
                    print("Error: La calificación no puede estar vacía.")
              
def cargar_datos():
    """
    Carga todos los datos de los estudiantes, utilizando funciones auxiliares.

    Returns:
            La matriz de calificaciones, la lista de nombres,
            la lista de géneros y la lista de legajos.
    """
    num_estudiantes = input("Ingrese la cantidad de estudiantes: ")
    while validar_numero_entero_positivo(num_estudiantes) != True:
        print("Error: Debe ingresar un número entero positivo.")
        num_estudiantes = input("Ingrese la cantidad de estudiantes: ")

    num_estudiantes = int(num_estudiantes)

    num_materias = input("Ingrese la cantidad de materias: ")
    while validar_numero_entero_positivo(num_materias) != True:
        print("Error: Debe ingresar un número entero positivo.")
        num_materias = input("Ingrese la cantidad de materias: ")

    num_materias = int(num_materias)

    matriz_calificaciones = inicializar_matriz(num_estudiantes, num_materias, 0)
    lista_nombres = inicializar_lista(num_estudiantes, 0)
    lista_generos = inicializar_lista(num_estudiantes, 0)
    lista_legajos = inicializar_lista(num_estudiantes, 0)

    # Preguntar al usuario si desea cargar los datos manualmente
    opcion = input("¿Desea cargar los datos manualmente? (S/N): ")
    opcion = convertir_a_mayusculas(opcion)
    if opcion == "S":
        cargar_nombres(lista_nombres)
        cargar_generos(lista_generos)
        cargar_legajos(lista_legajos)
        cargar_calificaciones(matriz_calificaciones)
    else:
        # Hardcodeo de datos para pruebas
        lista_nombres = [
            "ana", "pedro", "luis", "maria", "sofia",
            "juan", "laura", "carlos", "elena", "martin",
            "isabel", "roberto", "clara", "javier", "lucia",
            "miguel", "paula", "fernando", "valeria", "sebastian",
            "agustina", "damian", "florencia", "gonzalo", "camila",
            "matias", "rocio", "facundo", "antonella", "nicolas"
        ]

        lista_generos = [
            "f", "m", "m", "f", "x",
            "m", "f", "x", "f", "m",
            "f", "x", "f", "m", "f",
            "m", "f", "m", "f", "m",
            "f", "m", "f", "x", "f",
            "m", "x", "m", "f", "m"
        ]

        lista_legajos = [
            10001, 20002, 30003, 40004, 50005,
            10010, 20020, 30030, 40040, 50050,
            10100, 20200, 30300, 40400, 50500,
            11000, 22000, 33000, 44000, 55000,
            12345, 67890, 13579, 24680, 98765,
            54321, 90123, 78901, 34567, 89012
        ]
        matriz_calificaciones = [
            [7, 9, 5, 8, 6],
            [6, 8, 7, 9, 5],
            [9, 7, 6, 8, 10],
            [5, 6, 9, 7, 8],
            [8, 5, 10, 6, 7],
            [1, 6, 8, 5, 9],
            [7, 8, 5, 10, 6],
            [6, 9, 7, 5, 8],
            [8, 7, 1, 9, 5],
            [5, 10, 6, 7, 8],
            [9, 5, 8, 6, 7],
            [7, 6, 9, 1, 5],
            [6, 8, 5, 7, 9],
            [10, 7, 9, 5, 6],
            [5, 9, 6, 8, 7],
            [8, 6, 7, 10, 5],
            [7, 5, 1, 6, 9],
            [9, 8, 6, 7, 5],
            [6, 10, 5, 9, 8],
            [5, 7, 8, 6, 1],
            [8, 9, 6, 5, 7],
            [7, 5, 9, 8, 6],
            [9, 6, 7, 5, 10],
            [6, 8, 1, 7, 5],
            [5, 10, 7, 6, 9],
            [10, 7, 5, 9, 8],
            [8, 5, 9, 1, 6],
            [6, 9, 8, 5, 7],
            [7, 8, 6, 9, 5],
            [5, 6, 9, 8, 1]
        ]

    return matriz_calificaciones, lista_nombres, lista_generos, lista_legajos