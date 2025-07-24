"""
✨ Tuplas Lab Solutions o8 by @elliotgaramendi 👨‍💻
📦 o8 Tuplas en Python 🐍✨
"""

import math

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# o8 Tuplas Lab 📦✨
# ====================================================================


# --------------------------------------------------------------------
# o8.1 📍 Creador de Coordenadas 🗺️✨
# --------------------------------------------------------------------
def create_coordinates(lista_puntos):
    """📍 Convert list of points to coordinate tuples.
    Returns (coordinate_tuples, farthest_point, max_distance)"""
    # Handle empty list
    if not lista_puntos:
        return ((), (0, 0), 0.0)

    # Convert each point to tuple
    coordenadas = tuple(tuple(punto) for punto in lista_puntos)

    # Find the farthest point from origin
    max_distancia = 0.0
    punto_mas_lejano = (0, 0)

    for punto in lista_puntos:
        x, y = punto[0], punto[1]
        distancia = math.sqrt(x**2 + y**2)

        if distancia > max_distancia:
            max_distancia = distancia
            punto_mas_lejano = (x, y)

    # If only one point, that's the farthest
    if len(lista_puntos) == 1:
        punto_mas_lejano = tuple(lista_puntos[0])
        max_distancia = math.sqrt(lista_puntos[0][0] ** 2 + lista_puntos[0][1] ** 2)

    return (coordenadas, punto_mas_lejano, max_distancia)


def test_o8_1():
    # o8.1.1: Múltiples puntos
    result = create_coordinates([[1, 2], [3, 4], [0, 5]])
    print(result)
    record_test(
        "o8.1.1 múltiples puntos", result == (((1, 2), (3, 4), (0, 5)), (3, 4), 5.0)
    )

    # o8.1.2: Un solo punto
    result = create_coordinates([[3, 4]])
    record_test("o8.1.2 un solo punto", result == (((3, 4),), (3, 4), 5.0))

    # o8.1.3: Punto en origen
    result = create_coordinates([[0, 0], [1, 1]])
    expected_distance = round(math.sqrt(2), 2)
    coords, farthest, distance = result
    coords_ok = coords == ((0, 0), (1, 1))
    farthest_ok = farthest == (1, 1)
    distance_ok = round(distance, 2) == expected_distance
    record_test("o8.1.3 punto en origen", coords_ok and farthest_ok and distance_ok)

    # o8.1.4: Verificación de tipos
    coords, farthest, distance = create_coordinates([[1, 2]])
    types_ok = (
        isinstance(coords, tuple)
        and isinstance(farthest, tuple)
        and isinstance(distance, float)
    )
    record_test("o8.1.4 tipos correctos", types_ok)

    # o8.1.5: Lista vacía
    result = create_coordinates([])
    record_test("o8.1.5 lista vacía", result == ((), (0, 0), 0.0))


# Run tests for o8.1 🚀
test_o8_1()


# --------------------------------------------------------------------
# o8.2 🔢 Analizador de Estadísticas 📊🎯
# --------------------------------------------------------------------
def analyze_data(numeros):
    """🔢 Analyze list of numbers and return immutable statistics.
    Returns (data_tuple, min, max, average, median)"""
    # Handle empty list
    if not numeros:
        return ((), 0, 0, 0.0, 0.0)

    # Convert to tuple (immutable)
    tupla_datos = tuple(numeros)

    # Calculate basic statistics
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)

    # Calculate median
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)

    if n % 2 == 1:
        # Odd number of elements
        mediana = numeros_ordenados[n // 2]
    else:
        # Even number of elements
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2.0

    return (tupla_datos, minimo, maximo, promedio, mediana)


def test_o8_2():
    # o8.2.1: Lista impar de números
    result = analyze_data([3, 1, 4, 1, 5])
    record_test("o8.2.1 lista impar", result == ((3, 1, 4, 1, 5), 1, 5, 2.8, 3))

    # o8.2.2: Lista par de números
    result = analyze_data([2, 4, 6, 8])
    record_test("o8.2.2 lista par", result == ((2, 4, 6, 8), 2, 8, 5.0, 5.0))

    # o8.2.3: Un solo número
    result = analyze_data([42])
    record_test("o8.2.3 un solo número", result == ((42,), 42, 42, 42.0, 42))

    # o8.2.4: Verificación de tipos
    tupla_datos, minimo, maximo, promedio, mediana = analyze_data([1, 2, 3])
    types_ok = isinstance(tupla_datos, tuple) and isinstance(promedio, float)
    record_test("o8.2.4 tipos correctos", types_ok)

    # o8.2.5: Lista vacía
    result = analyze_data([])
    record_test("o8.2.5 lista vacía", result == ((), 0, 0, 0.0, 0.0))


# Run tests for o8.2 🚀
test_o8_2()


# --------------------------------------------------------------------
# o8.3 🎁 Desempaquetador de Información 📤✨
# --------------------------------------------------------------------
def unpack_student_data(estudiantes_tuplas):
    """🎁 Unpack student tuples and generate organized report.
    Returns (names_tuple, average_age, best_student, max_grade)"""
    # Handle empty list
    if not estudiantes_tuplas:
        return ((), 0.0, "", 0)

    nombres = []
    edades = []
    mejor_estudiante = ""
    nota_maxima = -1

    # Unpack each student tuple
    for nombre, edad, nota in estudiantes_tuplas:
        nombres.append(nombre)
        edades.append(edad)

        # Find best student (first one in case of tie)
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_estudiante = nombre

    # Convert names to tuple
    nombres_tupla = tuple(nombres)

    # Calculate average age
    promedio_edad = sum(edades) / len(edades)

    return (nombres_tupla, promedio_edad, mejor_estudiante, nota_maxima)


def test_o8_3():
    # o8.3.1: Múltiples estudiantes
    result = unpack_student_data([("Ana", 20, 85), ("Luis", 22, 90), ("María", 19, 88)])
    expected = (("Ana", "Luis", "María"), 20.33, "Luis", 90)
    # Check with rounding for average
    nombres, promedio, mejor, nota = result
    check = (
        nombres == expected[0]
        and round(promedio, 2) == expected[1]
        and mejor == expected[2]
        and nota == expected[3]
    )
    record_test("o8.3.1 múltiples estudiantes", check)

    # o8.3.2: Un estudiante
    result = unpack_student_data([("Carlos", 21, 75)])
    record_test("o8.3.2 un estudiante", result == (("Carlos",), 21.0, "Carlos", 75))

    # o8.3.3: Empate en notas
    result = unpack_student_data([("Ana", 20, 90), ("Luis", 22, 90)])
    record_test("o8.3.3 empate en notas", result == (("Ana", "Luis"), 21.0, "Ana", 90))

    # o8.3.4: Verificación de tipos
    nombres, promedio, mejor, nota = unpack_student_data([("Test", 20, 80)])
    types_ok = isinstance(nombres, tuple) and isinstance(promedio, float)
    record_test("o8.3.4 tipos correctos", types_ok)

    # o8.3.5: Lista vacía
    result = unpack_student_data([])
    record_test("o8.3.5 lista vacía", result == ((), 0.0, "", 0))


# Run tests for o8.3 🚀
test_o8_3()


# --------------------------------------------------------------------
# o8.4 🔗 Combinador de Tuplas 🤝📦
# --------------------------------------------------------------------
def combine_tuples(tupla1, tupla2, tupla3):
    """🔗 Combine three tuples in different ways.
    Returns (concatenation, interleaved, unique_elements)"""
    # Concatenation: simple join
    concatenacion = tupla1 + tupla2 + tupla3

    # Interleaving: alternate elements until shortest tuple is exhausted
    min_len = min(len(tupla1), len(tupla2), len(tupla3))
    intercalado = []

    for i in range(min_len):
        intercalado.append(tupla1[i])
        intercalado.append(tupla2[i])
        intercalado.append(tupla3[i])

    intercalado = tuple(intercalado)

    # Unique elements: remove duplicates maintaining order
    elementos_unicos = []
    seen = set()

    for elemento in concatenacion:
        if elemento not in seen:
            elementos_unicos.append(elemento)
            seen.add(elemento)

    elementos_unicos = tuple(elementos_unicos)

    return (concatenacion, intercalado, elementos_unicos)


def test_o8_4():
    # o8.4.1: Tuplas del mismo tamaño
    result = combine_tuples((1, 2), (3, 4), (5, 6))
    record_test(
        "o8.4.1 mismo tamaño",
        result == ((1, 2, 3, 4, 5, 6), (1, 3, 5, 2, 4, 6), (1, 2, 3, 4, 5, 6)),
    )

    # o8.4.2: Tuplas con duplicados
    result = combine_tuples((1, 2), (2, 3), (3, 1))
    record_test(
        "o8.4.2 con duplicados",
        result == ((1, 2, 2, 3, 3, 1), (1, 2, 3, 2, 3, 1), (1, 2, 3)),
    )

    # o8.4.3: Tuplas de diferente tamaño
    result = combine_tuples((1,), (2, 3), (4, 5, 6))
    record_test(
        "o8.4.3 diferente tamaño",
        result == ((1, 2, 3, 4, 5, 6), (1, 2, 4), (1, 2, 3, 4, 5, 6)),
    )

    # o8.4.4: Verificación de tipos
    concat, inter, unicos = combine_tuples((1,), (2,), (3,))
    types_ok = (
        isinstance(concat, tuple)
        and isinstance(inter, tuple)
        and isinstance(unicos, tuple)
    )
    record_test("o8.4.4 tipos correctos", types_ok)

    # o8.4.5: Tuplas vacías
    result = combine_tuples((), (1,), ())
    record_test("o8.4.5 tuplas vacías", result == ((1,), (), (1,)))


# Run tests for o8.4 🚀
test_o8_4()


# --------------------------------------------------------------------
# o8.5 📚 Indexador y Contador 🔍📊
# --------------------------------------------------------------------
def analyze_tuple_content(tupla_datos, elemento_buscar):
    """📚 Analyze tuple content and find element information.
    Returns (total_elements, occurrences, first_index, last_index)"""
    # Get total elements
    total_elementos = len(tupla_datos)

    # Count occurrences
    apariciones = tupla_datos.count(elemento_buscar)

    # Find first index
    try:
        primer_indice = tupla_datos.index(elemento_buscar)
    except ValueError:
        primer_indice = -1

    # Find last index
    ultimo_indice = -1
    if apariciones > 0:
        # Search from the end
        for i in range(len(tupla_datos) - 1, -1, -1):
            if tupla_datos[i] == elemento_buscar:
                ultimo_indice = i
                break

    return (total_elementos, apariciones, primer_indice, ultimo_indice)


def test_o8_5():
    # o8.5.1: Elemento múltiples veces
    result = analyze_tuple_content((1, 2, 3, 2, 4, 2), 2)
    record_test("o8.5.1 múltiples veces", result == (6, 3, 1, 5))

    # o8.5.2: Elemento una vez
    result = analyze_tuple_content(("a", "b", "c"), "b")
    record_test("o8.5.2 una vez", result == (3, 1, 1, 1))

    # o8.5.3: Elemento no encontrado
    result = analyze_tuple_content((1, 2, 3), 4)
    record_test("o8.5.3 no encontrado", result == (3, 0, -1, -1))

    # o8.5.4: Verificación de tipos
    total, apariciones, primero, ultimo = analyze_tuple_content((1, 2, 3), 2)
    types_ok = all(isinstance(x, int) for x in [total, apariciones, primero, ultimo])
    record_test("o8.5.4 tipos correctos", types_ok)

    # o8.5.5: Tupla vacía
    result = analyze_tuple_content((), 1)
    record_test("o8.5.5 tupla vacía", result == (0, 0, -1, -1))


# Run tests for o8.5 🚀
test_o8_5()

# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# 📦 Tuplas Lab o8 - Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")

print("\n🎯 ¡Felicitaciones! Has completado todos los retos de tuplas en Python 🐍✨")
print("✅ Dominas la creación de tuplas inmutables")
print("✅ Sabes desempaquetar información estructurada")
print("✅ Puedes combinar y manipular tuplas")
print("✅ Entiendes el análisis de contenido con métodos count() e index()")
print("✅ Conviertes entre tipos según necesidades")
