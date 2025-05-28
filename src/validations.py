from .display import *
from .functions import *
from .inputs import *
from .search import *
from .sort import *

# Funciones:
# validar_calificacion >>> linea 14
# validar_genero >>> linea 30
# validar_legajo >>> linea 46
# validar_nombre >>> linea 62
# validar_numero_entero_positivo >>> linea 85

def validar_calificacion(calificacion: any)-> bool:
    """
    Valida si una calificación es un entero dentro del rango permitido (1-10).
    No solicita la entrada, solo devuelve True o False.

    Args:
        calificacion: La calificación a validar.

    Returns:
        bool: True si la calificación es válida, False en caso contrario.
    """
    es_valida = True # Flag inicializada como True
    if type(calificacion) != int or (calificacion < 1 or calificacion > 10):
        es_valida = False
    return es_valida

def validar_genero(genero: any)-> bool:
    """
    Valida si un género es uno de los valores permitidos ('F', 'M', 'X').
    No solicita la entrada, solo devuelve True o False.

    Args:
        genero (str): El género a validar.

    Returns:
        bool: True si el género es válido, False en caso contrario.
    """
    es_valido = True # Flag inicializada como True
    if type(genero) != str or (genero != 'F' and genero != 'M' and genero != 'X'):
        es_valido = False
    return es_valido

def validar_legajo(legajo: any)-> bool:
    """
    Valida si un legajo es un número entero de cinco cifras.
    No solicita la entrada, solo devuelve True o False.

    Args:
        legajo: El legajo a validar.

    Returns:
        bool: True si el legajo es válido, False en caso contrario.
    """
    es_valido = True  # Flag inicializada como True
    if type(legajo) != int or (legajo < 10000 or legajo > 99999):
        es_valido = False
    return es_valido

def validar_nombre(nombre: any)-> bool:
    """
    Valida si un nombre es una cadena de texto.
    No solicita la entrada, solo devuelve True o False.

    Args:
        nombre: El nombre a validar.

    Returns:
        bool: True si el nombre es válido, False en caso contrario.
    """
    es_valido = True  # Flag inicializada como True
    if type(nombre) != str or nombre == "": # Verifica si no es una cadena o está vacía
        es_valido = False
    else:
        for i in nombre:
            # Verificar si el carácter no está en el rango ASCII de letras mayúsculas (65-90),
            # letras minúsculas (97-122) o no es un espacio (32)
            if (ord(i) < 65 or (ord(i) > 90 and ord(i) < 97) or ord(i) > 122) and ord(i) != 32:
                es_valido = False
                break
    return es_valido

def validar_numero_entero_positivo(valor: any) -> bool:
    """
    Verifica si el valor ingresado es un número entero positivo.

    Args:
        valor (any): El dato a validar.

    Returns:
        bool: True si es un número entero positivo, False en caso contrario.
    """
    es_valido = True  # Flag inicializada como True
    if valor == "":
        es_valido = False
    else:
        for i in valor:
            if i < '0' or i > '9':  # Verifica si cada carácter no es un dígito
                es_valido = False
                break
        # Solo verifica si es positivo si todos los caracteres son dígitos
        if es_valido == True and int(valor) <= 0:  # Verifica si el número es menor o igual a 0
            es_valido = False
    return es_valido
