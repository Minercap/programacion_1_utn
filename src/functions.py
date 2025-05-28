
# Funciones:
# inicializar_matriz >>> linea 12
# inicializar_lista >>> linea 30
# convertir_a_minusculas >>> linea 44
# convertir_a_mayusculas >>> linea 63
# redondear_a_dos_decimales >>> linea 82
# calcular_promedios_estudiantes >>> linea 94
# calcular_promedios_materias >>> linea 115
# contar_calificaciones_por_materia >>> linea 137

def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """
    Inicializa una matriz con las dimensiones dadas y un valor inicial.

    Args:
        cantidad_filas (int): El número de filas de la matriz.
        cantidad_columnas (int): El número de columnas de la matriz.
        valor_inicial (any): El valor con el que se inicializará cada elemento de la matriz.

    Returns:
        list: La matriz inicializada.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def inicializar_lista(tamaño: int, valor_inicial: int) -> list:
    """
    Inicializa una lista con un tamaño dado y un valor inicial.

    Args:
        tamaño (int): Tamaño de la lista.
        valor_inicial (int): Valor inicial para cada elemento de la lista.

    Returns:
        list: Lista inicializada.
    """
    lista = [valor_inicial] * tamaño
    return lista
        
def convertir_a_minusculas(cadena: str) -> str:
    """
    Convierte una cadena a minúsculas utilizando el código ASCII.

    Args:
        cadena (str): La cadena a convertir.

    Returns:
        str: La cadena convertida a minúsculas.
    """
    resultado = ""
    for caracter in cadena:
        # Verificar si el carácter está en mayúsculas (ASCII entre 65 y 90)
        if ord(caracter) >= 65 and ord(caracter) <= 90:
            resultado += chr(ord(caracter) + 32)
        else:
            resultado += caracter
    return resultado

def convertir_a_mayusculas(cadena: str) -> str:
    """
    Convierte una cadena a mayúsculas utilizando el código ASCII.

    Args:
        cadena (str): La cadena a convertir.

    Returns:
        str: La cadena convertida a mayúsculas.
    """
    resultado = ""
    for caracter in cadena:
        # Verificar si el carácter está en minúsculas (ASCII entre 97 y 122)
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
    return resultado

def redondear_a_dos_decimales(numero: float) -> float:
    """
    Redondea un número a 2 decimales.

    Args:
        numero (float): El número a redondear.

    Returns:
        float: El número redondeado a 2 decimales.
    """
    return int(numero * 100) / 100
        
def calcular_promedios_estudiantes(matriz_calificaciones):
    """
    Calcula el promedio de calificaciones de cada estudiante.

    Args:
        matriz_calificaciones (list): Matriz con las calificaciones de los estudiantes.

    Returns:
        list: Lista con los promedios de cada estudiante, redondeados a 2 decimales.
    """
    num_estudiantes = len(matriz_calificaciones)
    promedios = [0] * num_estudiantes
    for i in range(num_estudiantes):
        suma = 0
        for j in range(len(matriz_calificaciones[i])):
            suma += matriz_calificaciones[i][j]
        promedio = suma / len(matriz_calificaciones[i])
        promedio_redondeado = redondear_a_dos_decimales(promedio)
        promedios[i] = promedio_redondeado
    return promedios

def calcular_promedios_materias(matriz_calificaciones: list) -> list:
    """
    Calcula el promedio general de cada materia.

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.

    Returns:
        list: Una lista con los promedios generales de cada materia.
    """
    num_estudiantes = len(matriz_calificaciones)
    num_materias = len(matriz_calificaciones[0])
    promedios_materias = [0.0] * num_materias  # Inicializar con 0.0

    for j in range(num_materias):
        suma_calificaciones = 0
        for i in range(num_estudiantes):
            suma_calificaciones += matriz_calificaciones[i][j]
        promedios_materias[j] = suma_calificaciones / num_estudiantes

    return promedios_materias

def contar_calificaciones_por_materia(matriz_calificaciones: list, numero_materia: int) -> list:
    """
    Busca y cuenta la frecuencia de cada calificación (del 1 al 10) en una asignatura determinada.

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.
        numero_materia (int): El número de la materia (1 a 5), no el índice.

    Returns:
        list: Una lista de 10 elementos donde cada índice tiene la cantidad de veces que se ha dado esa calificación.
    """
    frecuencia_calificaciones = inicializar_lista(10, 0)
    flag = False
    indice_columna_materia = numero_materia - 1
    num_materias = len(matriz_calificaciones[0])
    if indice_columna_materia < 0 or indice_columna_materia >= num_materias:
        print(f"Error: El número de materia {numero_materia} es inválido. Debe ser entre 1 y {num_materias}.")
        flag = True
    else:
        i = 0
        while i < len(matriz_calificaciones):
            calificacion = matriz_calificaciones[i][indice_columna_materia]
            if 1 <= calificacion <= 10:
                frecuencia_calificaciones[calificacion - 1] += 1
            i += 1
    if flag == True:
        frecuencia_calificaciones = []

    return frecuencia_calificaciones
