"""
✨ Sets Lab Solutions by @elliotgaramendi 👨‍💻
"""

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# s10 Sets Lab 🔗✨
# ====================================================================


# --------------------------------------------------------------------
# s10.1 🗑️ Eliminador de Duplicados 🔄✨
# --------------------------------------------------------------------
def remove_duplicates(lista):
    """🗑️ Remove duplicates from list using sets.
    Returns (unique_count, original_count, duplicate_percentage)"""
    # Validate input
    if not isinstance(lista, list):
        return (0, 0, 0.0)

    # Get original count
    original_count = len(lista)

    # Handle empty list
    if original_count == 0:
        return (0, 0, 0.0)

    # Convert to set to remove duplicates
    unique_set = set(lista)
    unique_count = len(unique_set)

    # Calculate duplicate percentage
    duplicates_removed = original_count - unique_count
    duplicate_percentage = (duplicates_removed / original_count) * 100

    return (unique_count, original_count, duplicate_percentage)


def test_s10_1():
    # s10.1.1: Lista con duplicados variados
    result = remove_duplicates([1, 2, 2, 3, 3, 3])
    record_test("s10.1.1 duplicados variados", result == (3, 6, 50.0))

    # s10.1.2: Todos elementos iguales
    result = remove_duplicates([1, 1, 1, 1])
    record_test("s10.1.2 todos iguales", result == (1, 4, 75.0))

    # s10.1.3: Sin duplicados
    result = remove_duplicates([1, 2, 3, 4, 5])
    record_test("s10.1.3 sin duplicados", result == (5, 5, 0.0))

    # s10.1.4: Verificación de tipos
    unicos, original, porcentaje = remove_duplicates([1, 2, 3])
    types_ok = (
        isinstance(unicos, int)
        and isinstance(original, int)
        and isinstance(porcentaje, float)
    )
    record_test("s10.1.4 tipos correctos", types_ok)

    # s10.1.5: Lista vacía
    result = remove_duplicates([])
    record_test("s10.1.5 lista vacía", result == (0, 0, 0.0))


# Run tests for s10.1 🚀
test_s10_1()


# --------------------------------------------------------------------
# s10.2 🤝 Analizador de Intersecciones 🔍📊
# --------------------------------------------------------------------
def find_common_elements(set1, set2):
    """🤝 Find common elements between two sets.
    Returns (common_elements, count_common, similarity_percentage)"""
    # Validate inputs
    if not isinstance(set1, set) or not isinstance(set2, set):
        return (set(), 0, 0.0)

    # Find common elements (intersection)
    common_elements = set1 & set2
    count_common = len(common_elements)

    # Calculate similarity percentage based on union
    union_set = set1 | set2
    total_unique = len(union_set)

    # Handle empty sets
    if total_unique == 0:
        similarity_percentage = 0.0
    else:
        similarity_percentage = (count_common / total_unique) * 100

    return (common_elements, count_common, similarity_percentage)


def test_s10_2():
    # s10.2.1: Sets con elementos comunes
    result = find_common_elements({1, 2, 3}, {2, 3, 4})
    record_test("s10.2.1 elementos comunes", result == ({2, 3}, 2, 50.0))

    # s10.2.2: Sets sin elementos comunes
    result = find_common_elements({1, 2}, {3, 4})
    record_test("s10.2.2 sin comunes", result == (set(), 0, 0.0))

    # s10.2.3: Sets idénticos
    result = find_common_elements({1, 2, 3}, {1, 2, 3})
    record_test("s10.2.3 sets idénticos", result == ({1, 2, 3}, 3, 100.0))

    # s10.2.4: Verificación de tipos
    comunes, total, porcentaje = find_common_elements({1, 2}, {2, 3})
    types_ok = (
        isinstance(comunes, set)
        and isinstance(total, int)
        and isinstance(porcentaje, float)
    )
    record_test("s10.2.4 tipos correctos", types_ok)

    # s10.2.5: Un set vacío
    result = find_common_elements(set(), {1, 2})
    record_test("s10.2.5 set vacío", result == (set(), 0, 0.0))


# Run tests for s10.2 🚀
test_s10_2()


# --------------------------------------------------------------------
# s10.3 ➕ Constructor de Uniones 🔗🌟
# --------------------------------------------------------------------
def combine_sets(lista_sets):
    """➕ Combine multiple sets into one.
    Returns (union_set, unique_elements, total_original_elements)"""
    # Validate input
    if not isinstance(lista_sets, list):
        return (set(), 0, 0)

    # Handle empty list
    if len(lista_sets) == 0:
        return (set(), 0, 0)

    # Initialize union set and count total elements
    union_set = set()
    total_original_elements = 0

    # Process each set
    for s in lista_sets:
        if isinstance(s, set):
            union_set |= s  # Union operation
            total_original_elements += len(s)

    unique_elements = len(union_set)

    return (union_set, unique_elements, total_original_elements)


def test_s10_3():
    # s10.3.1: Sets con solapamiento
    result = combine_sets([{1, 2}, {2, 3}, {3, 4}])
    record_test("s10.3.1 sets con solapamiento", result == ({1, 2, 3, 4}, 4, 6))

    # s10.3.2: Sets idénticos
    result = combine_sets([{1, 2, 3}, {1, 2, 3}])
    record_test("s10.3.2 sets idénticos", result == ({1, 2, 3}, 3, 6))

    # s10.3.3: Sets diferentes
    result = combine_sets([{1}, {2}, {3}])
    record_test("s10.3.3 sets diferentes", result == ({1, 2, 3}, 3, 3))

    # s10.3.4: Verificación de tipos
    union, unicos, total = combine_sets([{1, 2}, {3}])
    types_ok = (
        isinstance(union, set) and isinstance(unicos, int) and isinstance(total, int)
    )
    record_test("s10.3.4 tipos correctos", types_ok)

    # s10.3.5: Lista vacía
    result = combine_sets([])
    record_test("s10.3.5 lista vacía", result == (set(), 0, 0))


# Run tests for s10.3 🚀
test_s10_3()


# --------------------------------------------------------------------
# s10.4 ⚖️ Detector de Diferencias 🔍🎯
# --------------------------------------------------------------------
def find_differences(set1, set2):
    """⚖️ Find differences between two sets.
    Returns (only_in_set1, only_in_set2, symmetric_difference)"""
    # Validate inputs
    if not isinstance(set1, set) or not isinstance(set2, set):
        return (set(), set(), set())

    # Find elements only in set1
    only_in_set1 = set1 - set2

    # Find elements only in set2
    only_in_set2 = set2 - set1

    # Find symmetric difference (elements in either set but not both)
    symmetric_difference = set1 ^ set2

    return (only_in_set1, only_in_set2, symmetric_difference)


def test_s10_4():
    # s10.4.1: Sets con algunos comunes
    result = find_differences({1, 2, 3}, {3, 4, 5})
    record_test("s10.4.1 algunos comunes", result == ({1, 2}, {4, 5}, {1, 2, 4, 5}))

    # s10.4.2: Sets idénticos
    result = find_differences({1, 2, 3}, {1, 2, 3})
    record_test("s10.4.2 sets idénticos", result == (set(), set(), set()))

    # s10.4.3: Sets diferentes
    result = find_differences({1, 2}, {3, 4})
    record_test("s10.4.3 sets diferentes", result == ({1, 2}, {3, 4}, {1, 2, 3, 4}))

    # s10.4.4: Verificación de tipos
    solo1, solo2, simetrica = find_differences({1}, {2})
    types_ok = (
        isinstance(solo1, set) and isinstance(solo2, set) and isinstance(simetrica, set)
    )
    record_test("s10.4.4 tipos correctos", types_ok)

    # s10.4.5: Un set vacío
    result = find_differences(set(), {1, 2})
    record_test("s10.4.5 set vacío", result == (set(), {1, 2}, {1, 2}))


# Run tests for s10.4 🚀
test_s10_4()


# --------------------------------------------------------------------
# s10.5 ✅ Validador de Membresías 🔐🎯
# --------------------------------------------------------------------
def validate_membership(set_datos, lista_buscar):
    """✅ Validate which elements from list are in the set.
    Returns (found_elements, count_found, percentage_found)"""
    # Validate inputs
    if not isinstance(set_datos, set) or not isinstance(lista_buscar, list):
        return ([], 0, 0.0)

    # Handle empty search list
    if len(lista_buscar) == 0:
        return ([], 0, 0.0)

    # Find elements that are in the set (preserve order)
    found_elements = []
    for elemento in lista_buscar:
        if elemento in set_datos:
            found_elements.append(elemento)

    count_found = len(found_elements)

    # Calculate percentage
    percentage_found = (count_found / len(lista_buscar)) * 100

    # Round to 2 decimal places for consistency
    percentage_found = round(percentage_found, 2)

    return (found_elements, count_found, percentage_found)


def test_s10_5():
    # s10.5.1: Todos encontrados
    result = validate_membership({1, 2, 3, 4, 5}, [1, 3, 5])
    record_test("s10.5.1 todos encontrados", result == ([1, 3, 5], 3, 100.0))

    # s10.5.2: Algunos encontrados
    result = validate_membership({1, 2, 3}, [1, 4, 5])
    record_test("s10.5.2 algunos encontrados", result == ([1], 1, 33.33))

    # s10.5.3: Ninguno encontrado
    result = validate_membership({1, 2, 3}, [4, 5, 6])
    record_test("s10.5.3 ninguno encontrado", result == ([], 0, 0.0))

    # s10.5.4: Verificación de tipos
    encontrados, total, porcentaje = validate_membership({1, 2}, [1])
    types_ok = (
        isinstance(encontrados, list)
        and isinstance(total, int)
        and isinstance(porcentaje, float)
    )
    record_test("s10.5.4 tipos correctos", types_ok)

    # s10.5.5: Lista vacía
    result = validate_membership({1, 2, 3}, [])
    record_test("s10.5.5 lista vacía", result == ([], 0, 0.0))


# Run tests for s10.5 🚀
test_s10_5()


# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")
