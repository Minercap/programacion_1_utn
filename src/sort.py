from .display import *
from .functions import *
from .inputs import *
from .search import *
from .validations import *

def ordenar_datos(matriz_calificaciones: list, lista_nombres: list, lista_generos: list, lista_legajos: list, lista_promedios: list, primer_modo: int = 1):
    """
    Ordena los datos de los estudiantes por promedio (ASC o DESC) y, secundariamente, por nombre (ASC).

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.
        lista_nombres (list): La lista de nombres de los estudiantes.
        lista_generos (list): La lista de géneros de los estudiantes.
        lista_legajos (list): La lista de legajos de los estudiantes.
        lista_promedios (list): La lista de promedios de los estudiantes.
        primer_modo (int, optional): 1 para ascendente, 2 para descendente del promedio.
    """
    for i in range(len(lista_promedios) - 1):
        for j in range(i + 1, len(lista_promedios)):
            # Criterio principal: promedio
            if (lista_promedios[i] < lista_promedios[j] and primer_modo == 1) or \
               (lista_promedios[i] > lista_promedios[j] and primer_modo == 2):
                # Intercambiar datos del estudiante
                lista_nombres[i], lista_nombres[j] = lista_nombres[j], lista_nombres[i]
                lista_legajos[i], lista_legajos[j] = lista_legajos[j], lista_legajos[i]
                lista_promedios[i], lista_promedios[j] = lista_promedios[j], lista_promedios[i]
                lista_generos[i], lista_generos[j] = lista_generos[j], lista_generos[i]
                matriz_calificaciones[i], matriz_calificaciones[j] = matriz_calificaciones[j], matriz_calificaciones[i]
            # Criterio secundario: nombre (ascendente)
            elif lista_promedios[i] == lista_promedios[j] and lista_nombres[i] > lista_nombres[j]:
                # Intercambiar datos del estudiante
                lista_nombres[i], lista_nombres[j] = lista_nombres[j], lista_nombres[i]
                lista_legajos[i], lista_legajos[j] = lista_legajos[j], lista_legajos[i]
                lista_promedios[i], lista_promedios[j] = lista_promedios[j], lista_promedios[i]
                lista_generos[i], lista_generos[j] = lista_generos[j], lista_generos[i]
                matriz_calificaciones[i], matriz_calificaciones[j] = matriz_calificaciones[j], matriz_calificaciones[i]