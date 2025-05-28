from .display import *
from .functions import *
from .inputs import *
from .sort import *
from .validations import *

def encontrar_materias_mayor_promedio(promedios_materias: list) -> list:
    """
    Encuentra los índices de las materias con el mayor promedio general.

    Args:
        promedios_materias (list): Una lista con los promedios generales de cada materia.

    Returns:
        list: Una lista con los índices de las materias con el mayor promedio.
    """
    
    materias_mayor_promedio_indices = [0] * len(promedios_materias)
    cantidad_materias_mayor_promedio = 0

    if not promedios_materias:  # Manejar el caso de lista vacía
        return []

    max_promedio = promedios_materias[0]

    # Encontrar el mayor promedio
    for i in range(1, len(promedios_materias)):
        if promedios_materias[i] > max_promedio:
            max_promedio = promedios_materias[i]

    # Encontrar los índices de las materias con el mayor promedio
    for i in range(len(promedios_materias)):
        if promedios_materias[i] == max_promedio:
            materias_mayor_promedio_indices[cantidad_materias_mayor_promedio] = i
            cantidad_materias_mayor_promedio += 1

    # Ajustar el tamaño de la lista resultado
    resultado_final = [0] * cantidad_materias_mayor_promedio
    for i in range(cantidad_materias_mayor_promedio):
        resultado_final[i] = materias_mayor_promedio_indices[i]

    return resultado_final

def buscar_estudiante_por_legajo(lista_legajos: list, legajo_buscado: int) -> list:
    """
    Busca el índice del estudiante con un legajo específico.

    Args:
        lista_legajos (list): La lista de legajos de los estudiantes.
        legajo_buscado (int): El legajo a buscar.

    Returns:
        list: Una lista con el índice del estudiante que tiene el legajo buscado.
               Si no se encuentra el legajo, la lista estará vacía.
               Dado que los legajos son únicos, la lista contendrá como máximo un elemento.
    """

    indices_encontrados = [0]  # Inicializamos la lista con un valor por defecto
    indice_encontrado = -1  # Inicializamos con un valor que indica "no encontrado"
    i = 0
    while i < len(lista_legajos):
        if lista_legajos[i] == legajo_buscado:
            indice_encontrado = i
            break  # Salimos del bucle al encontrar el legajo
        i += 1

    if indice_encontrado != -1:
        indices_encontrados[0] = indice_encontrado
        return indices_encontrados[:1]  # Devolvemos una lista con el índice encontrado
    else:
        return []  # Devolvemos una lista vacía si no se encontró el legajo