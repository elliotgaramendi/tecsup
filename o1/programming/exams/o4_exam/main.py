# 🐍 EXAMEN FINAL PYTHON - SOLUCIONES COMPLETAS 🐍
# ═══════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════
# 1️⃣ ALGORITHMS & CODE
# ══════════════════════════════════════════════════════════════

# Reto 1.1: Calculadora de Propina
import math
import random
from datetime import datetime


def calculate_tip(bill, tip_percent):
    tip = bill * tip_percent / 100
    total = bill + tip
    return float(total)

# Reto 1.2: Conversor de Temperatura


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return round(fahrenheit, 1)


# ══════════════════════════════════════════════════════════════
# 2️⃣ CONDITIONALS
# ══════════════════════════════════════════════════════════════

# Reto 2.1: Clasificador de Edad
def classify_age(age):
    if age < 0:
        return 'inválido'
    elif age <= 12:
        return 'niño'
    elif age <= 17:
        return 'adolescente'
    elif age <= 64:
        return 'adulto'
    else:
        return 'senior'

# Reto 2.2: Calificación a Letra


def grade_to_letter(score):
    if score < 0 or score > 100:
        return 'X'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# ══════════════════════════════════════════════════════════════
# 3️⃣ LOOPS I
# ══════════════════════════════════════════════════════════════

# Reto 3.1: Suma de Rango
def sum_range(start, end):
    if start > end:
        return 0
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

# Reto 3.2: Contador de Vocales


def count_vowels(text):
    vowels = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# ══════════════════════════════════════════════════════════════
# 4️⃣ INTEGRATION
# ══════════════════════════════════════════════════════════════

# Reto 4.1: Validador de Contraseña
def is_valid_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit

# Reto 4.2: Calculadora de Descuento


def apply_discount(price):
    if price >= 300:
        discount = 0.15
    elif price >= 200:
        discount = 0.10
    elif price >= 100:
        discount = 0.05
    else:
        discount = 0

    final_price = price * (1 - discount)
    return round(final_price, 2)


# ══════════════════════════════════════════════════════════════
# 5️⃣ CONDITIONALS II
# ══════════════════════════════════════════════════════════════

# Reto 5.1: Acceso a Evento
def can_enter(age, has_ticket, is_vip):
    if is_vip:
        return True
    if age >= 18 and has_ticket:
        return True
    return False

# Reto 5.2: Estado del Clima


def weather_status(temp, humidity, wind):
    if temp > 35 or humidity < 20 or wind > 60:
        return 'peligro'
    return 'seguro'


# ══════════════════════════════════════════════════════════════
# 6️⃣ LOOPS II
# ══════════════════════════════════════════════════════════════

# Reto 6.1: Buscar Número
def find_number(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

# Reto 6.2: Filtrar Pares


def filter_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 != 0:
            continue
        evens.append(num)
    return evens


# ══════════════════════════════════════════════════════════════
# 7️⃣ LOOPS III
# ══════════════════════════════════════════════════════════════

# Reto 7.1: Enumerar con Índices
def enumerate_list(items):
    result = []
    for index, value in enumerate(items):
        result.append(f"{index}: {value}")
    return result

# Reto 7.2: Múltiplos con Step


def get_multiples(n, start, end):
    # Encontrar el primer múltiplo >= start
    if start % n == 0:
        first_multiple = start
    else:
        first_multiple = start + (n - start % n)

    return list(range(first_multiple, end, n))


# ══════════════════════════════════════════════════════════════
# 8️⃣ LISTS
# ══════════════════════════════════════════════════════════════

# Reto 8.1: Agregar Únicos
def add_unique(original, items_to_add):
    result = original.copy()
    for item in items_to_add:
        if item not in result:
            result.append(item)
    return result

# Reto 8.2: Extraer Sección


def extract_section(items, start, end):
    return items[start:end]


# ══════════════════════════════════════════════════════════════
# 9️⃣ TUPLES
# ══════════════════════════════════════════════════════════════

# Reto 9.1: Intercambiar Valores
def swap_values(a, b):
    return (b, a)

# Reto 9.2: Desempaquetar Fecha


def unpack_date(date_tuple):
    day, month, year = date_tuple
    return {'day': day, 'month': month, 'year': year}


# ══════════════════════════════════════════════════════════════
# 🔟 SETS
# ══════════════════════════════════════════════════════════════

# Reto 10.1: Elementos Únicos
def get_unique(items):
    return sorted(list(set(items)))

# Reto 10.2: Intersección de Listas


def common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    return sorted(list(common))


# ══════════════════════════════════════════════════════════════
# 1️⃣1️⃣ DICTIONARIES
# ══════════════════════════════════════════════════════════════

# Reto 11.1: Contar Ocurrencias
def count_items(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Reto 11.2: Encontrar Máximo


def get_max_player(scores):
    if not scores:
        return None

    max_player = None
    max_score = float('-inf')

    for player, score in scores.items():
        if score > max_score:
            max_score = score
            max_player = player

    return max_player


# ══════════════════════════════════════════════════════════════
# 1️⃣2️⃣ FUNCTIONS
# ══════════════════════════════════════════════════════════════

# Reto 12.1: Calculadora Básica
def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return None

# Reto 12.2: Estadísticas de Lista


def get_stats(numbers):
    if not numbers:
        return None

    avg = sum(numbers) / len(numbers)
    return {
        'avg': avg,
        'max': max(numbers),
        'min': min(numbers)
    }


# ══════════════════════════════════════════════════════════════
# 1️⃣3️⃣ DATE & TIME
# ══════════════════════════════════════════════════════════════


# Reto 13.1: Días Entre Fechas

def days_between(date1, date2):
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    difference = abs((d2 - d1).days)
    return difference

# Reto 13.2: Formatear Fecha


def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d/%m/%Y')


# ══════════════════════════════════════════════════════════════
# 1️⃣4️⃣ MODULES
# ══════════════════════════════════════════════════════════════


# Reto 14.1: Dado Aleatorio

def roll_dice():
    return random.randint(1, 6)

# Reto 14.2: Raíz Cuadrada


def square_root(n):
    result = math.sqrt(n)
    return round(result, 2)


# ══════════════════════════════════════════════════════════════
# 1️⃣5️⃣ FILES
# ══════════════════════════════════════════════════════════════

# Reto 15.1: Escribir Lista
def write_list_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            f.write(str(item) + '\n')
    return True

# Reto 15.2: Contar Líneas


def count_lines(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0


# ══════════════════════════════════════════════════════════════
# 🧪 TEST RUNNERS - VERIFICACIÓN DE TODAS LAS SOLUCIONES
# ══════════════════════════════════════════════════════════════

def run_all_tests():
    print("🐍" + "="*60 + "🐍")
    print("   EXAMEN FINAL PYTHON - VERIFICACIÓN DE SOLUCIONES")
    print("🐍" + "="*60 + "🐍\n")

    total_tests = 0
    passed_tests = 0

    # 1.1
    print("1️⃣.1️⃣ Calculadora de Propina")
    tests = [
        calculate_tip(100, 15) == 115.0,
        calculate_tip(200, 20) == 240.0,
        calculate_tip(50, 10) == 55.0,
        calculate_tip(80, 18) == 94.4,
        type(calculate_tip(100, 15)) == float
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 1.2
    print("\n1️⃣.2️⃣ Conversor de Temperatura")
    tests = [
        celsius_to_fahrenheit(0) == 32.0,
        celsius_to_fahrenheit(100) == 212.0,
        celsius_to_fahrenheit(37) == 98.6,
        celsius_to_fahrenheit(-40) == -40.0,
        type(celsius_to_fahrenheit(25)) == float
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 2.1
    print("\n2️⃣.1️⃣ Clasificador de Edad")
    tests = [
        classify_age(10) == 'niño',
        classify_age(15) == 'adolescente',
        classify_age(25) == 'adulto',
        classify_age(70) == 'senior',
        classify_age(-5) == 'inválido'
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 2.2
    print("\n2️⃣.2️⃣ Calificación a Letra")
    tests = [
        grade_to_letter(95) == 'A',
        grade_to_letter(82) == 'B',
        grade_to_letter(75) == 'C',
        grade_to_letter(55) == 'F',
        grade_to_letter(150) == 'X'
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 3.1
    print("\n3️⃣.1️⃣ Suma de Rango")
    tests = [
        sum_range(1, 5) == 15,
        sum_range(10, 15) == 75,
        sum_range(1, 100) == 5050,
        sum_range(5, 1) == 0,
        sum_range(7, 7) == 7
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 3.2
    print("\n3️⃣.2️⃣ Contador de Vocales")
    tests = [
        count_vowels("Python") == 1,
        count_vowels("Programación") == 5,
        count_vowels("XYZ") == 0,
        count_vowels("AEIOUaeiou") == 10,
        count_vowels("") == 0
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 4.1
    print("\n4️⃣.1️⃣ Validador de Contraseña")
    tests = [
        is_valid_password("Abc12345") == True,
        is_valid_password("abc12345") == False,
        is_valid_password("ABCDEFGH") == False,
        is_valid_password("Abcd") == False,
        is_valid_password("Pass123Word") == True
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 4.2
    print("\n4️⃣.2️⃣ Calculadora de Descuento")
    tests = [
        apply_discount(50) == 50.0,
        apply_discount(150) == 142.5,
        apply_discount(250) == 225.0,
        apply_discount(350) == 297.5,
        apply_discount(100) == 95.0
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 5.1
    print("\n5️⃣.1️⃣ Acceso a Evento")
    tests = [
        can_enter(25, True, False) == True,
        can_enter(16, True, False) == False,
        can_enter(16, False, True) == True,
        can_enter(20, False, False) == False,
        can_enter(30, True, True) == True
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 5.2
    print("\n5️⃣.2️⃣ Estado del Clima")
    tests = [
        weather_status(30, 50, 40) == 'seguro',
        weather_status(40, 50, 40) == 'peligro',
        weather_status(25, 15, 30) == 'peligro',
        weather_status(30, 50, 70) == 'peligro',
        weather_status(35, 20, 60) == 'seguro'
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 6.1
    print("\n6️⃣.1️⃣ Buscar Número")
    tests = [
        find_number([1, 2, 3, 4, 5], 3) == 2,
        find_number([10, 20, 30], 25) == -1,
        find_number([5, 5, 5], 5) == 0,
        find_number([7, 8, 9, 10], 10) == 3,
        find_number([], 5) == -1
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 6.2
    print("\n6️⃣.2️⃣ Filtrar Pares")
    tests = [
        filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6],
        filter_evens([1, 3, 5]) == [],
        filter_evens([2, 4, 6]) == [2, 4, 6],
        filter_evens([]) == [],
        filter_evens([10, 15, 20, 25, 30]) == [10, 20, 30]
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 7.1
    print("\n7️⃣.1️⃣ Enumerar con Índices")
    tests = [
        enumerate_list(["a", "b", "c"]) == ['0: a', '1: b', '2: c'],
        enumerate_list(["Python"]) == ['0: Python'],
        enumerate_list([]) == [],
        enumerate_list(["x", "y"]) == ['0: x', '1: y'],
        len(enumerate_list(["a", "b", "c", "d"])) == 4
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 7.2
    print("\n7️⃣.2️⃣ Múltiplos con Step")
    tests = [
        get_multiples(3, 0, 10) == [0, 3, 6, 9],
        get_multiples(5, 0, 20) == [0, 5, 10, 15],
        get_multiples(7, 7, 30) == [7, 14, 21, 28],
        get_multiples(10, 0, 100) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
        get_multiples(4, 0, 5) == [0, 4]
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 8.1
    print("\n8️⃣.1️⃣ Agregar Únicos")
    tests = [
        add_unique([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5],
        add_unique([1, 2], [1, 2]) == [1, 2],
        add_unique([], [1, 2, 3]) == [1, 2, 3],
        add_unique([5], [5, 5, 5]) == [5],
        add_unique([1, 2, 3], []) == [1, 2, 3]
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 8.2
    print("\n8️⃣.2️⃣ Extraer Sección")
    tests = [
        extract_section([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4],
        extract_section([10, 20, 30], 0, 2) == [10, 20],
        extract_section([1, 2, 3], 2, 5) == [3],
        extract_section([5, 6, 7, 8], 0, 4) == [5, 6, 7, 8],
        extract_section([1, 2, 3], 5, 10) == []
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 9.1
    print("\n9️⃣.1️⃣ Intercambiar Valores")
    tests = [
        swap_values(10, 20) == (20, 10),
        swap_values(5, 15) == (15, 5),
        swap_values("a", "b") == ("b", "a"),
        swap_values(100, 200) == (200, 100),
        type(swap_values(1, 2)) == tuple
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 9.2
    print("\n9️⃣.2️⃣ Desempaquetar Fecha")
    tests = [
        unpack_date((15, 8, 2008)) == {'day': 15, 'month': 8, 'year': 2008},
        unpack_date((1, 1, 2000)) == {'day': 1, 'month': 1, 'year': 2000},
        unpack_date((25, 12, 2025)) == {'day': 25, 'month': 12, 'year': 2025},
        unpack_date((10, 5, 1990))['month'] == 5,
        type(unpack_date((1, 1, 2000))) == dict
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 10.1
    print("\n🔟.1️⃣ Elementos Únicos")
    tests = [
        get_unique([1, 2, 2, 3, 4, 3, 5]) == [1, 2, 3, 4, 5],
        get_unique([1, 1, 1]) == [1],
        get_unique([]) == [],
        get_unique([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5],
        type(get_unique([1, 2, 3])) == list
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 10.2
    print("\n🔟.2️⃣ Intersección de Listas")
    tests = [
        common_items([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4],
        common_items([1, 2], [3, 4]) == [],
        common_items(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c'],
        common_items([5, 5, 5], [5]) == [5],
        common_items([], [1, 2, 3]) == []
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 11.1
    print("\n1️⃣1️⃣.1️⃣ Contar Ocurrencias")
    tests = [
        count_items(['a', 'b', 'a', 'c', 'b', 'a']) == {
            'a': 3, 'b': 2, 'c': 1},
        count_items([1, 1, 2, 2, 2, 3]) == {1: 2, 2: 3, 3: 1},
        count_items([]) == {},
        count_items(['x']) == {'x': 1},
        count_items(['z', 'z']) == {'z': 2}
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 11.2
    print("\n1️⃣1️⃣.2️⃣ Encontrar Máximo")
    tests = [
        get_max_player({'Elliot': 100, 'Fe': 150, 'Mijael': 120}) == 'Fe',
        get_max_player({'A': 50, 'B': 75}) == 'B',
        get_max_player({}) == None,
        get_max_player({'X': 100}) == 'X',
        get_max_player({'P1': 200, 'P2': 200}) in ['P1', 'P2']
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 12.1
    print("\n1️⃣2️⃣.1️⃣ Calculadora Básica")
    tests = [
        calculate(10, 5, '+') == 15,
        calculate(10, 5, '-') == 5,
        calculate(10, 5, '*') == 50,
        calculate(10, 5, '/') == 2.0,
        calculate(10, 5, '%') == None
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 12.2
    print("\n1️⃣2️⃣.2️⃣ Estadísticas de Lista")
    tests = [
        get_stats([1, 2, 3, 4, 5]) == {'avg': 3.0, 'max': 5, 'min': 1},
        get_stats([10]) == {'avg': 10.0, 'max': 10, 'min': 10},
        get_stats([]) == None,
        get_stats([5, 10, 15])['avg'] == 10.0 if get_stats(
            [5, 10, 15]) else False,
        get_stats([2, 8, 5])['max'] == 8 if get_stats([2, 8, 5]) else False
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 13.1
    print("\n1️⃣3️⃣.1️⃣ Días Entre Fechas")
    tests = [
        days_between('2026-01-01', '2026-01-10') == 9,
        days_between('2025-12-25', '2026-01-01') == 7,
        days_between('2026-01-15', '2026-01-15') == 0,
        days_between('2026-01-01', '2026-02-01') == 31,
        days_between('2026-01-10', '2026-01-01') == 9
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 13.2
    print("\n1️⃣3️⃣.2️⃣ Formatear Fecha")
    tests = [
        format_date('2026-01-15') == '15/01/2026',
        format_date('2025-12-25') == '25/12/2025',
        format_date('2026-03-08') == '08/03/2026',
        format_date('2026-10-01') == '01/10/2026',
        format_date('2000-01-01') == '01/01/2000'
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 14.1
    print("\n1️⃣4️⃣.1️⃣ Dado Aleatorio")
    tests = [
        1 <= roll_dice() <= 6,
        type(roll_dice()) == int,
        len(set([roll_dice() for _ in range(100)])) > 1,
        all(1 <= roll_dice() <= 6 for _ in range(20)),
        max([roll_dice() for _ in range(50)]) <= 6
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 14.2
    print("\n1️⃣4️⃣.2️⃣ Raíz Cuadrada")
    tests = [
        square_root(144) == 12.0,
        square_root(25) == 5.0,
        square_root(2) == 1.41,
        square_root(100) == 10.0,
        square_root(9) == 3.0
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 15.1
    print("\n1️⃣5️⃣.1️⃣ Escribir Lista")
    test1 = write_list_to_file(['a', 'b', 'c'], 'test1.txt') == True
    test2 = write_list_to_file(['x'], 'test2.txt') == True
    test3 = write_list_to_file([], 'test3.txt') == True

    # Verificar contenido
    try:
        with open('test1.txt', 'r') as f:
            test4 = f.read() == 'a\nb\nc\n'
    except:
        test4 = False

    test5 = write_list_to_file(['1', '2'], 'test4.txt') == True

    tests = [test1, test2, test3, test4, test5]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # 15.2
    print("\n1️⃣5️⃣.2️⃣ Contar Líneas")
    # Crear archivos de prueba
    with open('test_3lines.txt', 'w') as f:
        f.write('line1\nline2\nline3\n')
    with open('test_empty.txt', 'w') as f:
        f.write('')
    with open('test_1line.txt', 'w') as f:
        f.write('single line')

    tests = [
        count_lines('test_3lines.txt') == 3,
        count_lines('test_empty.txt') == 0,
        count_lines('nonexistent.txt') == 0,
        count_lines('test_1line.txt') == 1,
        type(count_lines('test_3lines.txt')) == int
    ]
    for i, result in enumerate(tests, 1):
        total_tests += 1
        if result:
            passed_tests += 1
        print(f"   Test {i}: {'✅' if result else '❌'}")

    # Resumen final
    print("\n" + "="*62)
    print(f"🎯 RESULTADO FINAL: {passed_tests}/{total_tests} tests pasados")
    print(f"📊 Porcentaje: {(passed_tests/total_tests)*100:.1f}%")

    retos_completos = passed_tests // 5
    print(f"🏆 Retos completos (5/5 tests): {retos_completos}/30")

    if retos_completos >= 26:
        print("🌟 ¡EXCELENCIA TOTAL! 🌟")
    elif retos_completos >= 21:
        print("🥇 ¡APROBADO SOBRESALIENTE! 🥇")
    elif retos_completos >= 16:
        print("🥈 ¡APROBADO NOTABLE! 🥈")
    elif retos_completos >= 13:
        print("🥉 ¡APROBADO BÁSICO! 🥉")
    else:
        print("📚 Sigue practicando, ¡tú puedes! 📚")

    print("="*62)


# ══════════════════════════════════════════════════════════════
# 🚀 EJECUTAR TODOS LOS TESTS
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    run_all_tests()
