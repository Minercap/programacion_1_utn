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
            # Convertir a minúscula sumando 32 al valor ASCII
            resultado += chr(ord(caracter) + 32)
        else:
            # Si no es mayúscula, agregar el carácter tal cual
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
            # Convertir a mayúscula restando 32 al valor ASCII
            resultado += chr(ord(caracter) - 32)
        else:
            # Si no es minúscula, agregar el carácter tal cual
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

def calcular_promedio_estudiante(matriz_calificaciones: list, indice_estudiante: int) -> float:
    """
    Calcula el promedio de las calificaciones de un estudiante.

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.
        indice_estudiante (int): El índice del estudiante cuyo promedio se calculará.

    Returns:
        float: El promedio de las calificaciones del estudiante, redondeado a 2 decimales.
    """
    calificaciones = matriz_calificaciones[indice_estudiante]
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion
    promedio = suma / len(calificaciones)
    return redondear_a_dos_decimales(promedio)
        
def calcular_promedios_estudiantes(matriz_calificaciones):
    """
    Calcula el promedio de calificaciones de cada estudiante.

    Args:
        matriz_calificaciones (list): Matriz con las calificaciones de los estudiantes.

    Returns:
        list: Lista con los promedios de cada estudiante, redondeados a 2 decimales.
    """
    num_estudiantes = len(matriz_calificaciones)
    promedios = [0] * num_estudiantes  # Inicializar la lista de promedios con ceros

    for i in range(num_estudiantes):
        suma = 0
        for j in range(len(matriz_calificaciones[i])):  # Cambiado a for
            suma += matriz_calificaciones[i][j]
        promedio = suma / len(matriz_calificaciones[i])
        # Redondear a 2 decimales sin usar round
        promedio_redondeado = int(promedio * 100) / 100
        promedios[i] = promedio_redondeado  # Asignar el promedio redondeado al índice correspondiente

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
        list: Una lista de 10 elementos donde el índice 0 contiene la cantidad de veces que se repite la nota 1,
              el índice 1 la cantidad de veces que se repite la nota 2, y así sucesivamente hasta el índice 9
              para la nota 10.
    """
    # Inicializamos una lista de 10 ceros para contar las frecuencias de cada nota (del 1 al 10)
    # El índice 0 corresponde a la nota 1, el índice 1 a la nota 2, etc.
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

    # Si hubo error, vacía la lista para que el resto del programa lo detecte
    if flag == True:
        frecuencia_calificaciones = []

    return frecuencia_calificaciones
