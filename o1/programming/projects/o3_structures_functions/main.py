"""
🐍 PYTHON NIVEL 3 - COMPLETE SOLUTIONS
======================================
Instructions: Uncomment the challenge you want to run
"""

# ============================================================================
# o3.1: TUPLES - IMMUTABLE SEQUENCES
# ============================================================================


def o3_1_1_geographic_coordinates():
    """📍 Geographic Coordinates"""
    print("=" * 50)
    print("📍 Coordenadas Geográficas")
    print("=" * 50)

    # Solution
    coords = (-12.0464, -77.0428)
    lat, lon = coords

    print(f"Coordenadas: {coords}")
    print(f"Latitud: {lat}, Longitud: {lon}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (coords[0]): {coords[0] == -12.0464}")
    print(f"Test 2 (coords[1]): {coords[1] == -77.0428}")
    print(f"Test 3 (lat unpacked): {lat == -12.0464}")
    print(f"Test 4 (length): {len(coords) == 2}")
    print(f"Test 5 (type check): {type(coords) == tuple}")


def o3_1_2_birth_date():
    """📅 Birth Date"""
    print("=" * 50)
    print("📅 Fecha de Nacimiento")
    print("=" * 50)

    # Solution
    birthdate = (15, 8, 2010)
    day, month, year = birthdate
    formatted = f"{day}/{month}/{year}"

    print(f"Fecha de nacimiento: {formatted}")
    print(f"Día: {day}, Mes: {month}, Año: {year}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (day): {birthdate[0] == 15}")
    print(f"Test 2 (month): {birthdate[1] == 8}")
    print(f"Test 3 (year): {birthdate[2] == 2010}")
    print(f"Test 4 (formatted): {formatted == '15/8/2010'}")
    print(f"Test 5 (type check): {type(birthdate) == tuple}")


def o3_1_3_rgb_colors():
    """🎨 RGB Colors"""
    print("=" * 50)
    print("🎨 Colores RGB")
    print("=" * 50)

    # Solution
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red_sum = sum(red)
    colors = [red, green, blue]

    print(f"Rojo: {red}")
    print(f"Verde: {green}")
    print(f"Azul: {blue}")
    print(f"Suma componentes rojo: {red_sum}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (red[0]): {red[0] == 255}")
    print(f"Test 2 (green[1]): {green[1] == 255}")
    print(f"Test 3 (red_sum): {red_sum == 255}")
    print(f"Test 4 (colors length): {len(colors) == 3}")
    print(f"Test 5 (type check): {type(red) == tuple}")


def o3_1_4_player_stats():
    """📊 Player Statistics"""
    print("=" * 50)
    print("📊 Estadísticas de Jugador")
    print("=" * 50)

    # Solution
    player = ('Elliot', 25, 1500, 92)
    name, age, points, level = player
    max_value = max(age, points, level)
    average = (points + level) / 2

    print(f"Jugador: {name}")
    print(f"Edad: {age}, Puntos: {points}, Nivel: {level}")
    print(f"Valor máximo: {max_value}")
    print(f"Promedio puntos/nivel: {average}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (name): {player[0] == 'Elliot'}")
    print(f"Test 2 (points): {player[2] == 1500}")
    print(f"Test 3 (max_value): {max_value == 1500}")
    print(f"Test 4 (average): {average == 796.0}")
    print(f"Test 5 (type check): {type(player) == tuple}")


def o3_1_5_value_swap():
    """🔄 Value Swap"""
    print("=" * 50)
    print("🔄 Intercambio de Valores")
    print("=" * 50)

    # Solution
    a = 10
    b = 20
    initial = (a, b)

    # Swap using tuple unpacking
    a, b = b, a

    final = (a, b)
    result = (a, b)

    print(f"Inicial: a={initial[0]}, b={initial[1]}")
    print(f"Final: a={a}, b={b}")
    print(f"Resultado: {result}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (initial): {initial == (10, 20)}")
    print(f"Test 2 (final): {final == (20, 10)}")
    print(f"Test 3 (result): {result == (20, 10)}")
    print(f"Test 4 (sum): {a + b == 30}")
    print(f"Test 5 (type check): {type(result) == tuple}")


# ============================================================================
# o3.2: DICTIONARIES - KEY-VALUE STRUCTURES
# ============================================================================

def o3_2_1_user_profile():
    """👤 User Profile"""
    print("=" * 50)
    print("👤 Perfil de Usuario")
    print("=" * 50)

    # Solution
    user = {
        'name': 'Doky',
        'age': 5,
        'email': 'doky@email.com',
        'city': 'Lima'
    }
    name = user['name']
    age = user['age']

    # Modify age
    user['age'] = 6

    # Add country
    user['country'] = 'Peru'

    print(f"Usuario: {user['name']}")
    print(f"Edad: {user['age']}")
    print(f"Perfil completo: {user}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (name): {user['name'] == 'Doky'}")
    print(f"Test 2 (age modified): {user['age'] == 6}")
    print(f"Test 3 (email): {user['email'] == 'doky@email.com'}")
    print(f"Test 4 (length): {len(user) == 5}")
    print(f"Test 5 (type check): {type(user) == dict}")


def o3_2_2_product_inventory():
    """📦 Product Inventory"""
    print("=" * 50)
    print("📦 Inventario de Productos")
    print("=" * 50)

    # Solution
    inventory = {
        'manzanas': 50,
        'peras': 30,
        'uvas': 20
    }

    # Add naranjas
    inventory['naranjas'] = 15

    # Update peras
    inventory['peras'] = 35

    # Calculate totals
    total_items = sum(inventory.values())
    products = list(inventory.keys())

    print(f"Inventario: {inventory}")
    print(f"Total items: {total_items}")
    print(f"Productos: {products}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (manzanas): {inventory['manzanas'] == 50}")
    print(f"Test 2 (peras updated): {inventory['peras'] == 35}")
    print(f"Test 3 (total_items): {total_items == 115}")
    print(f"Test 4 (length): {len(inventory) == 4}")
    print(f"Test 5 (type check): {type(inventory) == dict}")


def o3_2_3_student_grades():
    """📚 Student Grades"""
    print("=" * 50)
    print("📚 Notas de Estudiantes")
    print("=" * 50)

    # Solution
    grades = {
        'Elliot': 18,
        'Fe': 16,
        'Mijael': 19
    }

    average = sum(grades.values()) / len(grades)
    max_grade = max(grades.values())
    min_grade = min(grades.values())

    # Count approved (>=14)
    approved_count = sum(1 for grade in grades.values() if grade >= 14)

    # Find top student
    top_student = max(grades, key=grades.get)

    print(f"Notas: {grades}")
    print(f"Promedio: {average:.2f}")
    print(f"Mejor nota: {max_grade} ({top_student})")
    print(f"Aprobados: {approved_count}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (Elliot grade): {grades['Elliot'] == 18}")
    print(f"Test 2 (average): {17.5 < average < 17.7}")
    print(f"Test 3 (max_grade): {max_grade == 19}")
    print(f"Test 4 (approved): {approved_count == 3}")
    print(f"Test 5 (type check): {type(grades) == dict}")


def o3_2_4_dictionary_iteration():
    """🔄 Dictionary Iteration"""
    print("=" * 50)
    print("🔄 Iteración de Diccionario")
    print("=" * 50)

    # Solution
    skills = {
        'fuerza': 85,
        'velocidad': 92,
        'inteligencia': 78
    }

    keys_list = list(skills.keys())
    values_list = list(skills.values())
    formatted = [f"{key}: {value}" for key, value in skills.items()]

    print("Habilidades:")
    for item in formatted:
        print(item)

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (fuerza): {skills['fuerza'] == 85}")
    print(
        f"Test 2 (keys_list): {keys_list == ['fuerza', 'velocidad', 'inteligencia']}")
    print(f"Test 3 (values_list): {values_list == [85, 92, 78]}")
    print(f"Test 4 (formatted[0]): {formatted[0] == 'fuerza: 85'}")
    print(f"Test 5 (type check): {type(skills) == dict}")


def o3_2_5_nested_dictionary():
    """🏗️ Nested Dictionary"""
    print("=" * 50)
    print("🏗️ Diccionario Anidado")
    print("=" * 50)

    # Solution
    menu = {
        'pizza': {
            'name': 'Margarita',
            'price': 25.50,
            'ingredients': ['masa', 'tomate', 'queso']
        },
        'pasta': {
            'name': 'Carbonara',
            'price': 25.00,
            'ingredients': ['pasta', 'salsa', 'queso']
        }
    }

    total_price = menu['pizza']['price'] + menu['pasta']['price']
    total_ingredients = len(
        menu['pizza']['ingredients']) + len(menu['pasta']['ingredients'])
    pizza_name = menu['pizza']['name']

    print(f"Menú: {list(menu.keys())}")
    print(f"Pizza: {pizza_name} - ${menu['pizza']['price']}")
    print(f"Total precio: ${total_price}")
    print(f"Total ingredientes: {total_ingredients}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (pizza price): {menu['pizza']['price'] == 25.50}")
    print(
        f"Test 2 (pasta ingredients): {menu['pasta']['ingredients'] == ['pasta', 'salsa', 'queso']}")
    print(f"Test 3 (total_price): {total_price == 50.50}")
    print(f"Test 4 (menu length): {len(menu) == 2}")
    print(f"Test 5 (type check): {type(menu) == dict}")


# ============================================================================
# o3.3: SETS - UNIQUE COLLECTIONS
# ============================================================================

def o3_3_1_unique_elements():
    """🎯 Unique Elements"""
    print("=" * 50)
    print("🎯 Elementos Únicos")
    print("=" * 50)

    # Solution
    numbers = [1, 2, 2, 3, 4, 3, 5]
    unique_set = set(numbers)
    count = len(unique_set)
    sorted_list = sorted(unique_set)

    print(f"Lista original: {numbers}")
    print(f"Set único: {unique_set}")
    print(f"Lista ordenada: {sorted_list}")
    print(f"Cantidad única: {count}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (unique_set): {unique_set == {1, 2, 3, 4, 5}}")
    print(f"Test 2 (length): {len(unique_set) == 5}")
    print(f"Test 3 (contains 3): {3 in unique_set}")
    print(f"Test 4 (sorted_list): {sorted_list == [1, 2, 3, 4, 5]}")
    print(f"Test 5 (type check): {type(unique_set) == set}")


def o3_3_2_set_union():
    """➕ Set Union"""
    print("=" * 50)
    print("➕ Unión de Conjuntos")
    print("=" * 50)

    # Solution
    group1 = {'Ana', 'Luis', 'Pedro'}
    group2 = {'María', 'Luis', 'Carlos'}
    all_friends = group1 | group2
    count = len(all_friends)
    sorted_friends = sorted(all_friends)

    print(f"Grupo 1: {group1}")
    print(f"Grupo 2: {group2}")
    print(f"Todos los amigos: {all_friends}")
    print(f"Total: {count}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (length): {len(all_friends) == 5}")
    print(f"Test 2 (contains Luis): {'Luis' in all_friends}")
    print(f"Test 3 (contains Ana): {'Ana' in all_friends}")
    print(
        f"Test 4 (sorted): {sorted_friends == ['Ana', 'Carlos', 'Luis', 'María', 'Pedro']}")
    print(f"Test 5 (type check): {type(all_friends) == set}")


def o3_3_3_set_intersection():
    """🔍 Set Intersection"""
    print("=" * 50)
    print("🔍 Intersección de Conjuntos")
    print("=" * 50)

    # Solution
    toys1 = {'pelota', 'hueso', 'cuerda'}
    toys2 = {'pelota', 'disco', 'hueso'}
    common_toys = toys1 & toys2
    count = len(common_toys)
    has_common = len(common_toys) > 0

    print(f"Juguetes 1: {toys1}")
    print(f"Juguetes 2: {toys2}")
    print(f"En común: {common_toys}")
    print(f"Cantidad común: {count}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (common_toys): {common_toys == {'pelota', 'hueso'}}")
    print(f"Test 2 (length): {len(common_toys) == 2}")
    print(f"Test 3 (contains pelota): {'pelota' in common_toys}")
    print(f"Test 4 (not disco): {'disco' not in common_toys}")
    print(f"Test 5 (type check): {type(common_toys) == set}")


def o3_3_4_set_difference():
    """➖ Set Difference"""
    print("=" * 50)
    print("➖ Diferencia de Conjuntos")
    print("=" * 50)

    # Solution
    current = {'Python', 'JavaScript', 'HTML'}
    desired = {'Python', 'React', 'Node'}
    to_learn = desired - current
    extra_skills = current - desired
    total_to_learn = len(to_learn)

    print(f"Actuales: {current}")
    print(f"Deseadas: {desired}")
    print(f"Debe aprender: {to_learn}")
    print(f"Habilidades extra: {extra_skills}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (to_learn): {to_learn == {'React', 'Node'}}")
    print(f"Test 2 (length): {len(to_learn) == 2}")
    print(f"Test 3 (extra_skills): {extra_skills == {'JavaScript', 'HTML'}}")
    print(f"Test 4 (not Python): {'Python' not in to_learn}")
    print(f"Test 5 (type check): {type(to_learn) == set}")


def o3_3_5_multiple_set_operations():
    """🔄 Multiple Set Operations"""
    print("=" * 50)
    print("🔄 Operaciones Múltiples de Sets")
    print("=" * 50)

    # Solution
    recipe1 = {'sal', 'pimienta', 'aceite'}
    recipe2 = {'sal', 'ajo', 'cebolla'}
    recipe3 = {'sal', 'tomate', 'aceite'}

    all_ingredients = recipe1 | recipe2 | recipe3
    common_to_all = recipe1 & recipe2 & recipe3
    unique_to_recipe1 = recipe1 - (recipe2 | recipe3)

    print(f"Todos los ingredientes: {all_ingredients}")
    print(f"Común a todas: {common_to_all}")
    print(f"Únicos de receta 1: {unique_to_recipe1}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (all length): {len(all_ingredients) == 6}")
    print(f"Test 2 (common): {common_to_all == {'sal'}}")
    print(f"Test 3 (common length): {len(common_to_all) == 1}")
    print(f"Test 4 (contains sal): {'sal' in all_ingredients}")
    print(f"Test 5 (type check): {type(all_ingredients) == set}")


# ============================================================================
# o3.4: FUNCTIONS - REUSABLE CODE
# ============================================================================

def o3_4_1_greeting_function():
    """👋 Greeting Function"""
    print("=" * 50)
    print("👋 Función de Saludo")
    print("=" * 50)

    # Solution
    def greet(name):
        return f"Hola, {name}!"

    result1 = greet('Elliot')
    result2 = greet('Fernanda')
    result3 = greet('Fe')

    print(result1)
    print(result2)
    print(result3)

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (Elliot): {result1 == 'Hola, Elliot!'}")
    print(f"Test 2 (Fernanda): {result2 == 'Hola, Fernanda!'}")
    print(f"Test 3 (Fe): {result3 == 'Hola, Fe!'}")
    print(f"Test 4 (type check): {type(result1) == str}")

    # Additional test
    print(f"Test 5 (callable): {callable(greet)}")


def o3_4_2_calculator_function():
    """➕ Calculator Function"""
    print("=" * 50)
    print("➕ Función Calculadora")
    print("=" * 50)

    # Solution
    def calculate(a, b, operation):
        if operation == 'suma':
            return a + b
        elif operation == 'resta':
            return a - b
        elif operation == 'multiplicación':
            return a * b
        elif operation == 'división':
            return a / b
        else:
            return None

    result1 = calculate(10, 5, 'suma')
    result2 = calculate(10, 5, 'resta')
    result3 = calculate(10, 5, 'multiplicación')
    result4 = calculate(10, 5, 'división')

    print(f"10 + 5 = {result1}")
    print(f"10 - 5 = {result2}")
    print(f"10 * 5 = {result3}")
    print(f"10 / 5 = {result4}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (suma): {result1 == 15}")
    print(f"Test 2 (resta): {result2 == 5}")
    print(f"Test 3 (multiplicación): {result3 == 50}")
    print(f"Test 4 (división): {result4 == 2.0}")
    print(f"Test 5 (type check): {type(result1) == int}")


def o3_4_3_statistics_function():
    """📊 Statistics Function"""
    print("=" * 50)
    print("📊 Función de Estadísticas")
    print("=" * 50)

    # Solution
    def get_stats(numbers):
        min_val = min(numbers)
        max_val = max(numbers)
        avg_val = sum(numbers) / len(numbers)
        sum_val = sum(numbers)
        return (min_val, max_val, avg_val, sum_val)

    numbers = [1, 2, 3, 4, 5]
    stats = get_stats(numbers)
    min_val, max_val, avg_val, sum_val = stats

    print(f"Números: {numbers}")
    print(f"Mínimo: {min_val}")
    print(f"Máximo: {max_val}")
    print(f"Promedio: {avg_val}")
    print(f"Suma: {sum_val}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (stats tuple): {stats == (1, 5, 3.0, 15)}")
    print(f"Test 2 (min): {min_val == 1}")
    print(f"Test 3 (max): {max_val == 5}")
    print(f"Test 4 (avg): {avg_val == 3.0}")
    print(f"Test 5 (type check): {type(stats) == tuple}")


def o3_4_4_profile_with_default():
    """🔄 Profile Function with Default"""
    print("=" * 50)
    print("🔄 Función Perfil con Valor por Defecto")
    print("=" * 50)

    # Solution
    def create_profile(name, age, city='Lima'):
        return {
            'name': name,
            'age': age,
            'city': city
        }

    profile1 = create_profile('Ana', 25)
    profile2 = create_profile('Luis', 30, 'Cusco')

    print(f"Perfil 1: {profile1}")
    print(f"Perfil 2: {profile2}")

    # Test cases
    print("\n--- Test Cases ---")
    print(
        f"Test 1 (profile1): {profile1 == {'name': 'Ana', 'age': 25, 'city': 'Lima'}}")
    print(
        f"Test 2 (profile2): {profile2 == {'name': 'Luis', 'age': 30, 'city': 'Cusco'}}")
    print(f"Test 3 (profile1 city): {profile1['city'] == 'Lima'}")
    print(f"Test 4 (profile2 city): {profile2['city'] == 'Cusco'}")
    print(f"Test 5 (type check): {type(profile1) == dict}")


def o3_4_5_complex_list_processor():
    """🎯 Complex List Processor"""
    print("=" * 50)
    print("🎯 Procesador Complejo de Listas")
    print("=" * 50)

    # Solution
    def process_list(items, operation='count'):
        if operation == 'count':
            return len(items)
        elif operation == 'sum':
            return sum(items)
        elif operation == 'average':
            return sum(items) / len(items)
        elif operation == 'unique':
            return list(set(items))
        else:
            return None

    numbers = [1, 2, 3, 4, 5]
    result1 = process_list(numbers, 'count')
    result2 = process_list(numbers, 'sum')
    result3 = process_list(numbers, 'average')
    result4 = process_list([1, 2, 2, 3], 'unique')

    print(f"Count: {result1}")
    print(f"Sum: {result2}")
    print(f"Average: {result3}")
    print(f"Unique: {result4}")

    # Test cases
    print("\n--- Test Cases ---")
    print(f"Test 1 (count): {result1 == 5}")
    print(f"Test 2 (sum): {result2 == 15}")
    print(f"Test 3 (average): {result3 == 3.0}")
    print(f"Test 4 (unique): {sorted(result4) == [1, 2, 3]}")
    print(f"Test 5 (type check): {type(result1) == int}")


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main menu to run individual challenges"""

    challenges = {
        # o3.1: Tuples
        '3.1.1': ('📍 Coordenadas Geográficas', o3_1_1_geographic_coordinates),
        '3.1.2': ('📅 Fecha de Nacimiento', o3_1_2_birth_date),
        '3.1.3': ('🎨 Colores RGB', o3_1_3_rgb_colors),
        '3.1.4': ('📊 Estadísticas de Jugador', o3_1_4_player_stats),
        '3.1.5': ('🔄 Intercambio de Valores', o3_1_5_value_swap),

        # o3.2: Dictionaries
        '3.2.1': ('👤 Perfil de Usuario', o3_2_1_user_profile),
        '3.2.2': ('📦 Inventario de Productos', o3_2_2_product_inventory),
        '3.2.3': ('📚 Notas de Estudiantes', o3_2_3_student_grades),
        '3.2.4': ('🔄 Iteración de Diccionario', o3_2_4_dictionary_iteration),
        '3.2.5': ('🏗️ Diccionario Anidado', o3_2_5_nested_dictionary),

        # o3.3: Sets
        '3.3.1': ('🎯 Elementos Únicos', o3_3_1_unique_elements),
        '3.3.2': ('➕ Unión de Conjuntos', o3_3_2_set_union),
        '3.3.3': ('🔍 Intersección de Conjuntos', o3_3_3_set_intersection),
        '3.3.4': ('➖ Diferencia de Conjuntos', o3_3_4_set_difference),
        '3.3.5': ('🔄 Operaciones Múltiples', o3_3_5_multiple_set_operations),

        # o3.4: Functions
        '3.4.1': ('👋 Función de Saludo', o3_4_1_greeting_function),
        '3.4.2': ('➕ Función Calculadora', o3_4_2_calculator_function),
        '3.4.3': ('📊 Función de Estadísticas', o3_4_3_statistics_function),
        '3.4.4': ('🔄 Función con Default', o3_4_4_profile_with_default),
        '3.4.5': ('🎯 Procesador Complejo', o3_4_5_complex_list_processor),
    }

    print("\n" + "=" * 60)
    print("🐍 PYTHON NIVEL 3 - SOLUCIONES")
    print("=" * 60)
    print("\nRetos disponibles:\n")

    # Show by topics
    print("📦 o3.1: Tuplas")
    for key in ['3.1.1', '3.1.2', '3.1.3', '3.1.4', '3.1.5']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n📚 o3.2: Diccionarios")
    for key in ['3.2.1', '3.2.2', '3.2.3', '3.2.4', '3.2.5']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n🎯 o3.3: Sets")
    for key in ['3.3.1', '3.3.2', '3.3.3', '3.3.4', '3.3.5']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n⚡ o3.4: Funciones")
    for key in ['3.4.1', '3.4.2', '3.4.3', '3.4.4', '3.4.5']:
        print(f"  {key} - {challenges[key][0]}")

    print("\n" + "=" * 60)

    while True:
        option = input(
            "\n🎯 Ingresa el número del reto (ej: 3.1.1) o 'q' para salir: ").strip()

        if option.lower() == 'q':
            print("\n👋 ¡Hasta luego! Sigue practicando 🐍✨")
            break

        if option in challenges:
            print("\n")
            challenges[option][1]()  # Execute challenge function
            print("\n" + "=" * 60)
            input("Presiona ENTER para continuar...")
        else:
            print("❌ Reto no encontrado. Intenta de nuevo.")


# ============================================================================
# DIRECT EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Uncomment ONE of these lines to run a specific challenge:

    # --- o3.1: Tuples ---
    # o3_1_1_geographic_coordinates()
    # o3_1_2_birth_date()
    # o3_1_3_rgb_colors()
    # o3_1_4_player_stats()
    # o3_1_5_value_swap()

    # --- o3.2: Dictionaries ---
    # o3_2_1_user_profile()
    # o3_2_2_product_inventory()
    # o3_2_3_student_grades()
    # o3_2_4_dictionary_iteration()
    # o3_2_5_nested_dictionary()

    # --- o3.3: Sets ---
    # o3_3_1_unique_elements()
    # o3_3_2_set_union()
    # o3_3_3_set_intersection()
    # o3_3_4_set_difference()
    # o3_3_5_multiple_set_operations()

    # --- o3.4: Functions ---
    # o3_4_1_greeting_function()
    # o3_4_2_calculator_function()
    # o3_4_3_statistics_function()
    # o3_4_4_profile_with_default()
    # o3_4_5_complex_list_processor()

    # --- Interactive Menu (recommended) ---
    main()
