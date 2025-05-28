from src.display import *
from src.functions import *
from src.inputs import *
from src.search import *
from src.sort import *
from src.validations import *

# Menú principal
def menu_principal():
    matriz_calificaciones = []  # Inicializar las estructuras de datos
    lista_nombres = []
    lista_generos = []
    lista_legajos = []
    lista_promedios = []
    datos_cargados = False  # Flag para verificar si los datos han sido cargados

    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar datos")
        print("2. Mostrar todos los datos")
        print("3. Calcular promedios")
        print("4. Ordenar y mostrar por promedio")
        print("5. Mostrar materias con mayor promedio")
        print("6. Buscar estudiante por legajo")
        print("7. Repeticion de calificaciones por materia")
        print("8. Salir")

        opcion = input("Ingrese la opción deseada: ")

        match opcion:
            case "1":
                matriz_calificaciones, lista_nombres, lista_generos, lista_legajos = cargar_datos()
                datos_cargados = True
            case "2":
                if datos_cargados == True:
                    print("\n--- Mostrar Todos los Estudiantes ---")
                    mostrar_todos_los_estudiantes(matriz_calificaciones, lista_nombres, lista_generos, lista_legajos)
                else:
                    print("Error: Primero debe cargar los datos.")
            case "3":
                if datos_cargados == True:
                    lista_promedios = calcular_promedios_estudiantes(matriz_calificaciones)
                else:
                    print("Error: Primero debe cargar los datos.")
            case "4":
                if datos_cargados == True:
                    if len(lista_promedios) > 0:  # Verificar si los promedios han sido calculados
                        print("\n--- Ordenar Datos (Descendente) ---")
                        primer_modo = 1  # Descendente
                        ordenar_datos(matriz_calificaciones, lista_nombres, lista_generos, lista_legajos, lista_promedios, primer_modo)
                        mostrar_todos_los_estudiantes_con_promedio(matriz_calificaciones, lista_nombres, lista_generos, lista_legajos, lista_promedios)
                    else:
                        print("Error: Primero debe calcular los promedios (opción 3).")
                else:
                    print("Error: Primero debe cargar los datos.")
            case "5":
                if datos_cargados == True:
                    if len(lista_promedios) > 0:  # Verificar si los promedios han sido calculados
                        print("\n--- Materia con el promedio más alto ---")
                        promedios_materias = calcular_promedios_materias(matriz_calificaciones)
                        mostrar_materias_mayor_promedio(promedios_materias)
                    else:
                        print("Error: Primero debe calcular los promedios (opción 3).")
                else:
                    print("Error: Primero debe cargar los datos.")
            case "6":
                if datos_cargados:
                    if len(lista_promedios) > 0:  # Verificar si los promedios han sido calculados
                        print("\n--- Buscar un estudiante por legajo ---")
                        while True:
                            legajo_buscar = input("Ingrese el legajo a buscar: ")
                            if validar_numero_entero_positivo(legajo_buscar):  # Usar la función personalizada
                                legajo_buscar = int(legajo_buscar)
                                break
                            else:
                                print("Error: Debe ingresar un número entero positivo válido.")
                        indices_encontrados = buscar_estudiante_por_legajo(lista_legajos, legajo_buscar)
                        if indices_encontrados:
                            mostrar_estudiantes_encontrados(
                                matriz_calificaciones, lista_nombres, lista_generos,
                                lista_legajos, lista_promedios, indices_encontrados
                            )
                        else:
                            print("No se encontró ningún estudiante con el legajo ingresado.")
                    else:
                        print("Error: Primero debe calcular los promedios (opción 3).")
                else:
                    print("Error: Primero debe cargar los datos.")  
            case "7":
                if datos_cargados == True:
                    flag = False
                    cantidad_materias = len(matriz_calificaciones[0])
                    while flag == False:
                        print("Ingrese el número de la materia (1 a " + str(cantidad_materias) + "): ")
                        num_materia = input()
                        if validar_numero_entero_positivo(num_materia) == True:
                            num_materia = int(num_materia)
                            if num_materia >= 1 and num_materia <= cantidad_materias:
                                flag = True
                            else:
                                print("Error: El número de materia debe estar entre 1 y " + str(cantidad_materias) + ".")
                        else:
                            print("Entrada inválida. Por favor, ingrese un número entero para la materia.")
                    frecuencia = contar_calificaciones_por_materia(matriz_calificaciones, num_materia)
                    if len(frecuencia) != 0:
                        mostrar_frecuencia_calificaciones(frecuencia, num_materia)
                else:
                    print("Error: Primero debe cargar los datos.")
                    
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                   
probando = menu_principal()