from .functions import *
from .inputs import *
from .search import *
from .sort import *
from .validations import *

def mostrar_datos_ordenados(matriz_calificaciones:list, lista_nombres:list, lista_generos:list, lista_legajos:list, lista_promedios:list):
    """
    Muestra los datos de los estudiantes ordenados.

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.
        lista_nombres (list): La lista de nombres de los estudiantes.
        lista_generos (list): La lista de géneros de los estudiantes.
        lista_legajos (list): La lista de legajos de los estudiantes.
        lista_promedios (list): La lista de promedios de los estudiantes.
    """

    print("Datos de los estudiantes ordenados:")
    num_estudiantes = len(lista_nombres)
    for i in range(num_estudiantes):
        print(f"-------------------- Estudiante {i + 1} --------------------")
        print(f"  Nombre: {lista_nombres[i]}")
        print(f"  Género: {lista_generos[i]}")
        print(f"  Legajo: {lista_legajos[i]}")
        print(f"  Promedio: {lista_promedios[i]}")
        print("  Calificaciones:", matriz_calificaciones[i])
        
def mostrar_un_estudiante(matriz_calificaciones:list, lista_nombres:list, lista_generos:list, lista_legajos:list, indice:int):
    """
    Muestra los datos y calificaciones de un estudiante específico.

    Args:
        indice (int): Índice del estudiante a mostrar.
    """
    if 0 <= indice < len(lista_nombres):  # Validar que el índice esté en rango
        print(f"Estudiante {indice + 1}:")
        print(f"  Nombre: {lista_nombres[indice]}")
        print(f"  Género: {lista_generos[indice]}")
        print(f"  Legajo: {lista_legajos[indice]}")
        print("  Calificaciones:")
        
        j = 0  # Índice de las materias
        while j < len(matriz_calificaciones[indice]):
            print(f"    Materia_{j + 1}: {matriz_calificaciones[indice][j]}")
            j += 1  # Incrementar el índice de las materias
    else:
        print("Error: El índice del estudiante está fuera de rango.")
        
def mostrar_un_estudiante_con_promedio(matriz_calificaciones:list, lista_nombres:list, lista_generos:list, lista_legajos:list, lista_promedios:list, indice:int):
    """
    Muestra los datos y calificaciones de un estudiante específico.

    Args:
        indice (int): Índice del estudiante a mostrar.
    """
    if 0 <= indice < len(lista_nombres):  # Validar que el índice esté en rango
        print(f"Estudiante {indice + 1}:")
        print(f"  Nombre: {lista_nombres[indice]}")
        print(f"  Género: {lista_generos[indice]}")
        print(f"  Legajo: {lista_legajos[indice]}")
        print(f"  Promedio: {lista_promedios[indice]}")
        print("  Calificaciones:")
        
        j = 0  # Índice de las materias
        while j < len(matriz_calificaciones[indice]):
            print(f"    Materia_{j + 1}: {matriz_calificaciones[indice][j]}")
            j += 1  # Incrementar el índice de las materias
    else:
        print("Error: El índice del estudiante está fuera de rango.")
        
def mostrar_todos_los_estudiantes(matriz_calificaciones, lista_nombres, lista_generos, lista_legajos):
    """
    Muestra todos los estudiantes con sus datos y calificaciones, indicando las materias.

    Args:
        matriz_calificaciones (list): Matriz con las calificaciones de los estudiantes.
        lista_nombres (list): Lista con los nombres de los estudiantes.
        lista_generos (list): Lista con los géneros de los estudiantes.
        lista_legajos (list): Lista con los legajos de los estudiantes.
    """
    print("Listado de Estudiantes:")
    i = 0  # Índice del estudiante
    while i < len(lista_nombres):
        print(f"Estudiante {i + 1}:")
        print(f"  Nombre: {lista_nombres[i]}")
        print(f"  Género: {lista_generos[i]}")
        print(f"  Legajo: {lista_legajos[i]}")
        print("  Calificaciones:")
        
        j = 0  # Índice de las materias
        while j < len(matriz_calificaciones[i]):
            print(f"    Materia_{j + 1}: {matriz_calificaciones[i][j]}")
            j += 1  # Incrementar el índice de las materias
        
        print("-" * 30)
        i += 1  # Incrementar el índice del estudiante
        
def mostrar_todos_los_estudiantes_con_promedio(matriz_calificaciones, lista_nombres, lista_generos, lista_legajos, lista_promedios):
    """
    Muestra todos los estudiantes con sus datos y calificaciones, indicando las materias.

    Args:
        matriz_calificaciones (list): Matriz con las calificaciones de los estudiantes.
        lista_nombres (list): Lista con los nombres de los estudiantes.
        lista_generos (list): Lista con los géneros de los estudiantes.
        lista_legajos (list): Lista con los legajos de los estudiantes.
    """
    print("Listado de Estudiantes:")
    i = 0  # Índice del estudiante
    while i < len(lista_nombres):
        print(f"Estudiante {i + 1}:")
        print(f"  Nombre: {lista_nombres[i]}")
        print(f"  Género: {lista_generos[i]}")
        print(f"  Legajo: {lista_legajos[i]}")
        promedio_redondeado = redondear_a_dos_decimales(lista_promedios[i])  # Usar la función personalizada
        print(f"  Promedio: {promedio_redondeado}")
        print("  Calificaciones:")
        
        j = 0  # Índice de las materias
        while j < len(matriz_calificaciones[i]):
            print(f"    Materia_{j + 1}: {matriz_calificaciones[i][j]}")
            j += 1  # Incrementar el índice de las materias
        
        print("-" * 30)
        i += 1  # Incrementar el índice del estudiante

def mostrar_materia(promedios_materias: list, indice_materia: int):
    """
    Muestra el promedio de una materia específica.

    Args:
        promedios_materias (list): Lista de promedios de las materias.
        indice_materia (int): Índice de la materia a mostrar.
    """
    promedio_redondeado = redondear_a_dos_decimales(promedios_materias[indice_materia])  # Usar la función personalizada
    print(f"MATERIA_{indice_materia + 1}: Promedio = {promedio_redondeado}")


def mostrar_materias_mayor_promedio(promedios_materias: list):
    """
    Muestra las materias con el mayor promedio general.

    Args:
        promedios_materias (list): Una lista con los promedios generales de cada materia.
    """

    materias_mayor_promedio_indices = encontrar_materias_mayor_promedio(promedios_materias)
    max_promedio = promedios_materias[materias_mayor_promedio_indices[0]]  # Obtener el valor del mayor promedio

    print("Materia(s) con el mayor promedio general:")
    for indice in materias_mayor_promedio_indices:
        mostrar_materia(promedios_materias, indice)
    
def mostrar_un_estudiante_con_promedio(matriz_calificaciones: list, lista_nombres: list, lista_generos: list,
                          lista_legajos: list, lista_promedios: list, indice_estudiante: int):
    """
    Muestra la información de un estudiante específico.

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.
        lista_nombres (list): La lista de nombres de los estudiantes.
        lista_generos (list): La lista de géneros de los estudiantes.
        lista_legajos (list): La lista de legajos de los estudiantes.
        lista_promedios (list): La lista de promedios de los estudiantes.
        indice_estudiante (int): El índice del estudiante a mostrar.
    """

    print("------------------------------------")
    print(f"Estudiante {indice_estudiante + 1}:")
    print(f"  Nombre: {lista_nombres[indice_estudiante]}")
    print(f"  Género: {lista_generos[indice_estudiante]}")
    print(f"  Legajo: {lista_legajos[indice_estudiante]}")
    promedio_redondeado = redondear_a_dos_decimales(lista_promedios[indice_estudiante])  # Usar la función personalizada
    print(f"  Promedio: {promedio_redondeado}")
    print("  Calificaciones:")
    i = 0
    while i < len(matriz_calificaciones[indice_estudiante]):
        print(f"    Materia {i + 1}: {matriz_calificaciones[indice_estudiante][i]}")
        i += 1
    print("------------------------------------")
    
def mostrar_estudiantes_encontrados(matriz_calificaciones: list, lista_nombres: list, lista_generos: list,
                                   lista_legajos: list, lista_promedios: list, indices_estudiantes: list):
    """
    Muestra la información de todos los estudiantes encontrados en la búsqueda.

    Args:
        matriz_calificaciones (list): La matriz de calificaciones de los estudiantes.
        lista_nombres (list): La lista de nombres de los estudiantes.
        lista_generos (list): La lista de géneros de los estudiantes.
        lista_legajos (list): La lista de legajos de los estudiantes.
        lista_promedios (list): La lista de promedios de los estudiantes.
        indices_estudiantes (list): Una lista con los índices de los estudiantes a mostrar.
    """

    if not indices_estudiantes:
        print("No se encontraron estudiantes con el legajo especificado.")
    else:
        i = 0
        while i < len(indices_estudiantes):
            mostrar_un_estudiante_con_promedio(matriz_calificaciones, lista_nombres, lista_generos,
                                  lista_legajos, lista_promedios, indices_estudiantes[i])
            i += 1
            
def mostrar_frecuencia_calificaciones(frecuencias: list, numero_materia: int):
    """
    Muestra la frecuencia de cada calificación para una materia determinada.

    Args:
        frecuencias (list): La lista de frecuencias de calificaciones.
        numero_materia (int): El número de la materia.
    """
    if len(frecuencias) != 0:
        print(f"\n--- Frecuencia de calificaciones para MATERIA_{numero_materia} ---")
        i = 0
        while i < len(frecuencias):
            print(f"Nota {i + 1}: {frecuencias[i]} veces")
            i += 1
        print("-----------------------------------------------------")