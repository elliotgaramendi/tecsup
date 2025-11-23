"""
🐍 PYTHON NIVEL 2 - SOLUCIONES COMPLETAS
========================================
Instrucciones: Descomenta el reto que deseas ejecutar
"""

# ============================================================================
# o2.1: CONDICIONALES II - LÓGICA AVANZADA
# ============================================================================


def o2_1_1_access_system():
    """🎫 Sistema de Acceso"""
    print("=" * 50)
    print("🎫 Sistema de Acceso")
    print("=" * 50)

    age = 25
    has_invitation = False

    # Solution
    access = (18 <= age <= 65) and has_invitation

    print(f"Edad: {age}, Invitación: {has_invitation}")
    print(f"Acceso: {'Permitido ✅' if access else 'Denegado ❌'}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (age=25, invite=False): {access == False}")
    print(f"Test 2 (type check): {type(access) == bool}")

    # Additional tests
    test_cases = [
        (25, True, True),
        (17, True, False),
        (70, True, False),
    ]

    for age, inv, expected in test_cases:
        result = (18 <= age <= 65) and inv
        print(f"Test (age={age}, invite={inv}): {result == expected}")


def o2_1_2_premium_validator():
    """🎮 Validador de Usuario Premium"""
    print("=" * 50)
    print("🎮 Validador de Usuario Premium")
    print("=" * 50)

    level = 35
    paid = True

    # Solution
    is_premium = (level >= 50) or paid
    discount = 20 if is_premium else 0

    print(f"Nivel: {level}, Membresía: {paid}")
    print(f"Premium: {is_premium} | Descuento: {discount}%")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (level=35, paid=True): {is_premium == True}")
    print(f"Test 2 (discount): {discount == 20}")
    print(f"Test 3 (type check): {type(is_premium) == bool}")

    # Additional tests
    test_cases = [
        (60, False, True),
        (30, False, False),
    ]

    for lvl, pd, expected in test_cases:
        result = (lvl >= 50) or pd
        print(f"Test (level={lvl}, paid={pd}): {result == expected}")


def o2_1_3_smart_traffic_light():
    """🚦 Semáforo Inteligente"""
    print("=" * 50)
    print("🚦 Semáforo Inteligente")
    print("=" * 50)

    light = 'verde'
    cars = 3

    # Solution
    can_cross = (light == 'verde') and (cars == 0)

    print(f"Semáforo: {light} | Carros: {cars}")
    print(f"¿Puede cruzar?: {'Sí ✅' if can_cross else 'No ❌'}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (verde, 3 cars): {can_cross == False}")
    print(f"Test 2 (type check): {type(can_cross) == bool}")

    # Additional tests
    test_cases = [
        ('verde', 0, True),
        ('rojo', 0, False),
        ('amarillo', 0, False),
    ]

    for lt, cr, expected in test_cases:
        result = (lt == 'verde') and (cr == 0)
        print(f"Test (light={lt}, cars={cr}): {result == expected}")


def o2_1_4_danger_detector():
    """⚠️ Detector de Peligro"""
    print("=" * 50)
    print("⚠️ Detector de Peligro")
    print("=" * 50)

    temp = 35
    humidity = 15
    gas = False

    # Solution
    danger = (temp > 40) or (humidity < 20) or gas
    danger_count = int(temp > 40) + int(humidity < 20) + int(gas)

    print(f"Temp: {temp}°C | Humedad: {humidity}% | Gas: {gas}")
    print(f"Peligro: {'SÍ ⚠️' if danger else 'NO ✅'}")
    print(f"Señales de peligro: {danger_count}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (danger): {danger == True}")
    print(f"Test 2 (count): {danger_count == 1}")
    print(f"Test 3 (type check): {type(danger) == bool}")

    # Additional tests
    test_cases = [
        (45, 25, False, True),
        (30, 30, False, False),
    ]

    for t, h, g, expected in test_cases:
        result = (t > 40) or (h < 20) or g
        print(f"Test (temp={t}, hum={h}, gas={g}): {result == expected}")


def o2_1_5_complete_security():
    """🔐 Sistema de Seguridad Completo"""
    print("=" * 50)
    print("🔐 Sistema de Seguridad Completo")
    print("=" * 50)

    age = 25
    code = '1234'
    admin = False
    valid_code = '1234'

    # Solution
    full_access = ((18 <= age <= 60) and (code == valid_code)) or admin

    print(f"Edad: {age} | Código: {code} | Admin: {admin}")
    print(f"Acceso: {'TOTAL ✅' if full_access else 'DENEGADO ❌'}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (age=25, code=1234, admin=False): {full_access == True}")
    print(f"Test 2 (type check): {type(full_access) == bool}")

    # Additional tests
    test_cases = [
        (70, '1234', False, False),
        (25, '0000', False, False),
        (70, '0000', True, True),
    ]

    for a, c, ad, expected in test_cases:
        result = ((18 <= a <= 60) and (c == valid_code)) or ad
        print(f"Test (age={a}, code={c}, admin={ad}): {result == expected}")


# ============================================================================
# o2.2: BUCLES II - CONTROL DE FLUJO
# ============================================================================

def o2_2_1_ingredient_finder():
    """🔍 Búsqueda con Break"""
    print("=" * 50)
    print("🔍 Búsqueda de Ingredientes")
    print("=" * 50)

    pantry = ['harina', 'aceite', 'pimienta', 'arroz', 'pasta', 'tomate', 'sal',
              'vinagre', 'azucar', 'cafe', 'te', 'leche', 'huevos', 'queso',
              'mantequilla', 'pan', 'agua', 'jugo', 'yogur', 'cereal']
    target = 'sal'

    # Solution
    found = False
    iterations = 0
    position = -1

    for i, item in enumerate(pantry):
        iterations += 1
        if item == target:
            found = True
            position = i
            break

    print(f"Buscando: {target}")
    print(f"Encontrado: {'Sí ✅' if found else 'No ❌'}")
    print(f"Iteraciones: {iterations}")
    print(f"Posición: {position}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (found): {found == True}")
    print(f"Test 2 (iterations): {iterations == 7}")
    print(f"Test 3 (position): {position == 6}")
    print(f"Test 4 (type check): {type(found) == bool}")


def o2_2_2_even_filter():
    """⏭️ Filtrar con Continue"""
    print("=" * 50)
    print("⏭️ Filtrar Pares (sin múltiplos de 10)")
    print("=" * 50)

    # Solution
    even_count = 0
    evens_list = []

    for i in range(1, 21):
        if i % 10 == 0:
            continue
        if i % 2 == 0:
            even_count += 1
            evens_list.append(i)

    print(f"Pares (sin múltiplos de 10): {even_count}")
    print(f"Lista: {evens_list}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (count): {even_count == 8}")
    print(f"Test 2 (list): {evens_list == [2, 4, 6, 8, 12, 14, 16, 18]}")
    print(f"Test 3 (10 not in): {10 not in evens_list}")
    print(f"Test 4 (type check): {type(even_count) == int}")


def o2_2_3_star_pattern():
    """🎨 Patrón de Asteriscos"""
    print("=" * 50)
    print("🎨 Patrón de Asteriscos")
    print("=" * 50)

    height = 5

    # Solution
    pattern = ''
    total_stars = 0

    for row in range(1, height + 1):
        for col in range(row):
            pattern += '*'
            total_stars += 1
        pattern += '\n'

    print(pattern)
    print(f"Total de estrellas: {total_stars}")

    # Test cases
    print("--- Test Cases ---")
    print(f"Test 1 (newlines): {pattern.count(chr(10)) == 4}")
    print(f"Test 2 (total stars): {total_stars == 15}")
    print(f"Test 3 (star count): {pattern.count('*') == 15}")
    print(f"Test 4 (type check): {type(pattern) == str}")


def o2_2_4_multiplication_tables():
    """📊 Tabla de Multiplicar"""
    print("=" * 50)
    print("📊 Tablas de Multiplicar")
    print("=" * 50)

    # Solution
    total_operations = 0
    table_1_sum = 0
    table_3_sum = 0
    table_5_sum = 0

    for num in range(1, 6):
        print(f"\nTabla del {num}:")
        for mult in range(1, 11):
            product = num * mult
            total_operations += 1
            print(f"{num} x {mult} = {product}")

            if num == 1:
                table_1_sum += product
            elif num == 3:
                table_3_sum += product
            elif num == 5:
                table_5_sum += product

    print(f"\nTotal de operaciones: {total_operations}")
    print(f"Suma tabla 3: {table_3_sum}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (operations): {total_operations == 50}")
    print(f"Test 2 (table 3): {table_3_sum == 165}")
    print(f"Test 3 (table 5): {table_5_sum == 275}")
    print(f"Test 4 (type check): {type(total_operations) == int}")


def o2_2_5_sum_until_limit():
    """🎲 Suma hasta Límite"""
    print("=" * 50)
    print("🎲 Suma hasta Límite")
    print("=" * 50)

    limit = 500

    # Solution
    total_sum = 0
    last_num = 0

    for i in range(1, 101):
        if total_sum + i > limit:
            break
        total_sum += i
        last_num = i

    print(f"Límite: {limit}")
    print(f"Suma final: {total_sum}")
    print(f"Último número: {last_num}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (last_num): {last_num == 31}")
    print(f"Test 2 (total_sum): {total_sum == 496}")
    print(f"Test 3 (type check): {type(total_sum) == int}")

    # Additional test
    total_sum2, last_num2 = 0, 0
    for i in range(1, 101):
        if total_sum2 + i > 1000:
            break
        total_sum2 += i
        last_num2 = i
    print(f"Test 4 (limit=1000): {last_num2 == 44}")


# ============================================================================
# o2.3: BUCLES III - ITERACIÓN AVANZADA
# ============================================================================

def o2_3_1_fruit_enumerator():
    """📇 Lista con Índices"""
    print("=" * 50)
    print("📇 Enumerador de Frutas")
    print("=" * 50)

    fruits = ['manzana', 'pera', 'uva', 'fresa', 'kiwi']

    # Solution
    enumerate_output = []

    for index, fruit in enumerate(fruits):
        line = f"{index}: {fruit}"
        enumerate_output.append(line)

    print("Frutas con índice:")
    for line in enumerate_output:
        print(line)

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (first): {enumerate_output[0] == '0: manzana'}")
    print(f"Test 2 (third): {enumerate_output[2] == '2: uva'}")
    print(f"Test 3 (length): {len(enumerate_output) == 5}")
    print(f"Test 4 (type check): {type(enumerate_output) == list}")


def o2_3_2_custom_step_counter():
    """⏩ Saltos Personalizados"""
    print("=" * 50)
    print("⏩ Contador con Saltos (Múltiplos de 5)")
    print("=" * 50)

    # Solution
    multiples = []
    total_sum = 0
    count = 0

    for i in range(0, 31, 5):
        multiples.append(i)
        total_sum += i
        count += 1

    print(f"Múltiplos de 5: {multiples}")
    print(f"Suma total: {total_sum}")
    print(f"Cantidad: {count}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (list): {multiples == [0, 5, 10, 15, 20, 25, 30]}")
    print(f"Test 2 (sum): {total_sum == 105}")
    print(f"Test 3 (count): {count == 7}")
    print(f"Test 4 (type check): {type(multiples) == list}")


def o2_3_3_even_odd_separator():
    """🔄 Separar Pares e Impares"""
    print("=" * 50)
    print("🔄 Separador de Pares e Impares")
    print("=" * 50)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Solution
    even_list = []
    odd_list = []
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
            even_sum += num
        else:
            odd_list.append(num)
            odd_sum += num

    print(f"Pares: {even_list} | Suma: {even_sum}")
    print(f"Impares: {odd_list} | Suma: {odd_sum}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (evens): {even_list == [2, 4, 6, 8, 10]}")
    print(f"Test 2 (odds): {odd_list == [1, 3, 5, 7, 9]}")
    print(f"Test 3 (even_sum): {even_sum == 30}")
    print(f"Test 4 (odd_sum): {odd_sum == 25}")
    print(f"Test 5 (type check): {type(even_list) == list}")


def o2_3_4_for_else_finder():
    """🔍 Búsqueda con For-Else"""
    print("=" * 50)
    print("🔍 Búsqueda con For-Else")
    print("=" * 50)

    languages = ['Java', 'C++', 'Ruby', 'Go', 'JavaScript']
    search = 'Python'

    # Solution
    found = False
    else_executed = False

    for lang in languages:
        if lang == search:
            found = True
            break
    else:
        else_executed = True

    print(f"Buscando: {search}")
    print(f"Encontrado: {found}")
    print(f"Else ejecutado: {else_executed}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (not found): {found == False}")
    print(f"Test 2 (else executed): {else_executed == True}")
    print(f"Test 3 (type check): {type(found) == bool}")

    # Additional test - found case
    found2 = False
    for lang in languages:
        if lang == 'Java':
            found2 = True
            break
    print(f"Test 4 (Java found): {found2 == True}")


def o2_3_5_range_analyzer():
    """📊 Análisis de Rango"""
    print("=" * 50)
    print("📊 Análisis de Rango")
    print("=" * 50)

    # Solution
    even_count = 0
    odd_count = 0
    mult_3_count = 0
    mult_5_count = 0
    total_sum = 0

    for i in range(1, 21):
        total_sum += i

        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if i % 3 == 0:
            mult_3_count += 1

        if i % 5 == 0:
            mult_5_count += 1

    print(f"Pares: {even_count} | Impares: {odd_count}")
    print(f"Múltiplos de 3: {mult_3_count} | Múltiplos de 5: {mult_5_count}")
    print(f"Suma total: {total_sum}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (evens): {even_count == 10}")
    print(f"Test 2 (odds): {odd_count == 10}")
    print(f"Test 3 (mult 3): {mult_3_count == 6}")
    print(f"Test 4 (mult 5): {mult_5_count == 4}")
    print(f"Test 5 (sum): {total_sum == 210}")


# ============================================================================
# o2.4: LISTAS - COLECCIONES DINÁMICAS
# ============================================================================

def o2_4_1_dynamic_list_builder():
    """➕ Construir Lista Dinámica"""
    print("=" * 50)
    print("➕ Constructor de Lista Dinámica")
    print("=" * 50)

    # Solution
    languages = []
    languages.append('Python')
    languages.append('JavaScript')
    languages.append('Java')
    languages.append('C++')
    languages.append('Ruby')

    print(f"Lista: {languages}")
    print(f"Primero: {languages[0]}")
    print(f"Último: {languages[-1]}")
    print(f"Total: {len(languages)}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (first): {languages[0] == 'Python'}")
    print(f"Test 2 (last): {languages[-1] == 'Ruby'}")
    print(f"Test 3 (length): {len(languages) == 5}")
    print(f"Test 4 (contains): {'Java' in languages}")
    print(f"Test 5 (type check): {type(languages) == list}")


def o2_4_2_list_slicer():
    """✂️ Slicing Maestro"""
    print("=" * 50)
    print("✂️ Cortador de Listas")
    print("=" * 50)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Solution
    first_3 = numbers[0:3]
    last_3 = numbers[-3:]
    middle = numbers[3:8]

    print(f"Primeros 3: {first_3}")
    print(f"Últimos 3: {last_3}")
    print(f"Medio (3-7): {middle}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (first 3): {first_3 == [1, 2, 3]}")
    print(f"Test 2 (last 3): {last_3 == [8, 9, 10]}")
    print(f"Test 3 (middle): {middle == [4, 5, 6, 7, 8]}")
    print(f"Test 4 (middle length): {len(middle) == 5}")
    print(f"Test 5 (type check): {type(first_3) == list}")


def o2_4_3_list_sorter():
    """🔄 Ordenar y Revertir"""
    print("=" * 50)
    print("🔄 Ordenador de Listas")
    print("=" * 50)

    original = [5, 2, 8, 1, 9, 3]

    # Solution
    ascending = original.copy()
    ascending.sort()

    descending = original.copy()
    descending.sort(reverse=True)

    print(f"Original: {original}")
    print(f"Ascendente: {ascending}")
    print(f"Descendente: {descending}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (original intact): {original == [5, 2, 8, 1, 9, 3]}")
    print(f"Test 2 (ascending): {ascending == [1, 2, 3, 5, 8, 9]}")
    print(f"Test 3 (descending): {descending == [9, 8, 5, 3, 2, 1]}")
    print(f"Test 4 (original first): {original[0] == 5}")
    print(f"Test 5 (type check): {type(ascending) == list}")


def o2_4_4_duplicate_remover():
    """🗑️ Eliminar Duplicados"""
    print("=" * 50)
    print("🗑️ Eliminador de Duplicados")
    print("=" * 50)

    original = [1, 2, 2, 3, 4, 3, 5, 1]

    # Solution
    unique = []

    for item in original:
        if item not in unique:
            unique.append(item)

    print(f"Original: {original}")
    print(f"Sin duplicados: {unique}")
    print(f"Elementos únicos: {len(unique)}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (original): {original == [1, 2, 2, 3, 4, 3, 5, 1]}")
    print(f"Test 2 (unique): {unique == [1, 2, 3, 4, 5]}")
    print(f"Test 3 (length): {len(unique) == 5}")
    print(f"Test 4 (first): {unique[0] == 1}")
    print(f"Test 5 (type check): {type(unique) == list}")


def o2_4_5_list_methods_master():
    """🔧 Métodos de Lista Completos"""
    print("=" * 50)
    print("🔧 Maestro de Métodos de Lista")
    print("=" * 50)

    # Solution
    ingredients = ['sal', 'pimienta', 'azucar']
    print(f"Inicial: {ingredients}")

    ingredients.append('aceite')
    print(f"Después de append: {ingredients}")

    ingredients.remove('azucar')
    print(f"Después de remove: {ingredients}")

    ingredients.insert(1, 'vinagre')
    print(f"Después de insert: {ingredients}")

    ingredients.pop()
    print(f"Después de pop: {ingredients}")

    print(f"\nLista final: {ingredients}")
    print(f"Total elementos: {len(ingredients)}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (contains vinagre): {'vinagre' in ingredients}")
    print(f"Test 2 (no azucar): {'azucar' not in ingredients}")
    print(f"Test 3 (length): {len(ingredients) == 3}")
    print(f"Test 4 (position 1): {ingredients[1] == 'vinagre'}")
    print(f"Test 5 (type check): {type(ingredients) == list}")


# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def main():
    """Menú principal para ejecutar retos individuales"""

    retos = {
        # o2.1: Condicionales II
        '2.1.1': ('🎫 Sistema de Acceso', o2_1_1_access_system),
        '2.1.2': ('🎮 Validador Premium', o2_1_2_premium_validator),
        '2.1.3': ('🚦 Semáforo Inteligente', o2_1_3_smart_traffic_light),
        '2.1.4': ('⚠️ Detector de Peligro', o2_1_4_danger_detector),
        '2.1.5': ('🔐 Seguridad Completa', o2_1_5_complete_security),

        # o2.2: Bucles II
        '2.2.1': ('🔍 Búsqueda con Break', o2_2_1_ingredient_finder),
        '2.2.2': ('⏭️ Filtrar con Continue', o2_2_2_even_filter),
        '2.2.3': ('🎨 Patrón de Asteriscos', o2_2_3_star_pattern),
        '2.2.4': ('📊 Tablas de Multiplicar', o2_2_4_multiplication_tables),
        '2.2.5': ('🎲 Suma hasta Límite', o2_2_5_sum_until_limit),

        # o2.3: Bucles III
        '2.3.1': ('📇 Lista con Índices', o2_3_1_fruit_enumerator),
        '2.3.2': ('⏩ Saltos Personalizados', o2_3_2_custom_step_counter),
        '2.3.3': ('🔄 Separar Pares/Impares', o2_3_3_even_odd_separator),
        '2.3.4': ('🔍 Búsqueda For-Else', o2_3_4_for_else_finder),
        '2.3.5': ('📊 Análisis de Rango', o2_3_5_range_analyzer),

        # o2.4: Listas
        '2.4.1': ('➕ Constructor de Lista', o2_4_1_dynamic_list_builder),
        '2.4.2': ('✂️ Slicing Maestro', o2_4_2_list_slicer),
        '2.4.3': ('🔄 Ordenar y Revertir', o2_4_3_list_sorter),
        '2.4.4': ('🗑️ Eliminar Duplicados', o2_4_4_duplicate_remover),
        '2.4.5': ('🔧 Métodos de Lista', o2_4_5_list_methods_master),
    }

    print("\n" + "=" * 60)
    print("🐍 PYTHON NIVEL 2 - SOLUCIONES")
    print("=" * 60)
    print("\nRetos disponibles:\n")

    # Mostrar por temas
    print("📝 o2.1: Condicionales II")
    for key in ['2.1.1', '2.1.2', '2.1.3', '2.1.4', '2.1.5']:
        print(f"  {key} - {retos[key][0]}")

    print("\n🔄 o2.2: Bucles II")
    for key in ['2.2.1', '2.2.2', '2.2.3', '2.2.4', '2.2.5']:
        print(f"  {key} - {retos[key][0]}")

    print("\n⚡ o2.3: Bucles III")
    for key in ['2.3.1', '2.3.2', '2.3.3', '2.3.4', '2.3.5']:
        print(f"  {key} - {retos[key][0]}")

    print("\n📊 o2.4: Listas")
    for key in ['2.4.1', '2.4.2', '2.4.3', '2.4.4', '2.4.5']:
        print(f"  {key} - {retos[key][0]}")

    print("\n" + "=" * 60)

    while True:
        opcion = input(
            "\n🎯 Ingresa el número del reto (ej: 2.1.1) o 'q' para salir: ").strip()

        if opcion.lower() == 'q':
            print("\n👋 ¡Hasta luego! Sigue practicando 🐍✨")
            break

        if opcion in retos:
            print("\n")
            retos[opcion][1]()  # Ejecutar función del reto
            print("\n" + "=" * 60)
            input("Presiona ENTER para continuar...")
        else:
            print("❌ Reto no encontrado. Intenta de nuevo.")


# ============================================================================
# EJECUCIÓN DIRECTA
# ============================================================================

if __name__ == "__main__":
    # Descomenta UNA de estas líneas para ejecutar un reto específico:

    # --- o2.1: Condicionales II ---
    # o2_1_1_access_system()
    # o2_1_2_premium_validator()
    # o2_1_3_smart_traffic_light()
    # o2_1_4_danger_detector()
    # o2_1_5_complete_security()

    # --- o2.2: Bucles II ---
    # o2_2_1_ingredient_finder()
    # o2_2_2_even_filter()
    # o2_2_3_star_pattern()
    # o2_2_4_multiplication_tables()
    # o2_2_5_sum_until_limit()

    # --- o2.3: Bucles III ---
    # o2_3_1_fruit_enumerator()
    # o2_3_2_custom_step_counter()
    # o2_3_3_even_odd_separator()
    # o2_3_4_for_else_finder()
    # o2_3_5_range_analyzer()

    # --- o2.4: Listas ---
    # o2_4_1_dynamic_list_builder()
    # o2_4_2_list_slicer()
    # o2_4_3_list_sorter()
    # o2_4_4_duplicate_remover()
    # o2_4_5_list_methods_master()

    # --- Menú Interactivo (recomendado) ---
    main()
