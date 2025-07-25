"""
✨ Diccionarios Lab Solutions o11 by @elliotgaramendi 👨‍💻
📚 o11 Diccionarios en Python 🐍✨
"""

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# o11 Diccionarios Lab 📚✨
# ====================================================================


# --------------------------------------------------------------------
# o11.1 👤 Creador de Perfiles 📝✨
# --------------------------------------------------------------------
def create_profile(nombre, edad, email):
    """👤 Create user profile dictionary with validation.
    Returns dict with profile data or None if invalid."""
    # Validate nombre - must not be empty
    if not nombre or len(nombre.strip()) == 0:
        return None

    # Validate edad - must be non-negative integer
    if not isinstance(edad, int) or edad < 0:
        return None

    # Validate email - must contain "@"
    if not isinstance(email, str) or "@" not in email:
        return None

    # Create and return valid profile
    return {"nombre": nombre, "edad": edad, "email": email, "activo": True}


def test_o11_1():
    # o11.1.1: Datos válidos
    result = create_profile("Ana", 25, "ana@email.com")
    valid_profile = (
        isinstance(result, dict)
        and result.get("nombre") == "Ana"
        and result.get("edad") == 25
        and result.get("email") == "ana@email.com"
    )
    record_test("o11.1.1 datos válidos", valid_profile)

    # o11.1.2: Edad cero
    result = create_profile("Bebé", 0, "bebe@email.com")
    record_test("o11.1.2 edad cero", isinstance(result, dict))

    # o11.1.3: Estructura del diccionario
    result = create_profile("Test", 30, "test@email.com")
    keys_ok = isinstance(result, dict) and all(
        key in result for key in ["nombre", "edad", "email", "activo"]
    )
    record_test("o11.1.3 estructura correcta", keys_ok)

    # o11.1.4: Verificación de tipos
    result = create_profile("Juan", 20, "juan@test.com")
    record_test("o11.1.4 retorna dict", isinstance(result, dict))

    # o11.1.5: Datos inválidos
    invalid_cases = [
        create_profile("", 25, "test@email.com"),  # nombre vacío
        create_profile("Juan", -5, "juan@test.com"),  # edad negativa
        create_profile("Ana", 25, "email-sin-arroba"),  # email sin @
    ]
    all_none = all(result is None for result in invalid_cases)
    record_test("o11.1.5 datos inválidos", all_none)


# Run tests for o11.1 🚀
test_o11_1()


# --------------------------------------------------------------------
# o11.2 📊 Contador de Elementos 🔢🎯
# --------------------------------------------------------------------
def count_elements(lista):
    """📊 Count frequency of each element in list.
    Returns dict with element: count pairs."""
    # Handle empty list
    if not lista:
        return {}

    contador = {}

    # Count each element
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1

    return contador


def test_o11_2():
    # o11.2.1: Lista con repeticiones
    result = count_elements([1, 2, 2, 3, 3, 3])
    record_test("o11.2.1 con repeticiones", result == {1: 1, 2: 2, 3: 3})

    # o11.2.2: Lista de strings
    result = count_elements(["a", "b", "a", "c", "b", "a"])
    record_test("o11.2.2 strings", result == {"a": 3, "b": 2, "c": 1})

    # o11.2.3: Elementos únicos
    result = count_elements([1, 2, 3, 4])
    expected = {1: 1, 2: 1, 3: 1, 4: 1}
    record_test("o11.2.3 elementos únicos", result == expected)

    # o11.2.4: Verificación de tipos
    result = count_elements([1, 2, 1])
    record_test("o11.2.4 retorna dict", isinstance(result, dict))

    # o11.2.5: Lista vacía
    result = count_elements([])
    record_test("o11.2.5 lista vacía", result == {})


# Run tests for o11.2 🚀
test_o11_2()


# --------------------------------------------------------------------
# o11.3 🔍 Buscador de Información 🎯📋
# --------------------------------------------------------------------
def find_user_info(usuarios, nombre_buscar):
    """🔍 Find user info by name in list of user dictionaries.
    Returns user dict or None if not found."""
    # Handle empty list
    if not usuarios:
        return None

    # Convert search name to lowercase for case-insensitive search
    nombre_buscar_lower = nombre_buscar.lower()

    # Search for user
    for usuario in usuarios:
        if "nombre" in usuario:
            if usuario["nombre"].lower() == nombre_buscar_lower:
                return usuario

    # User not found
    return None


def test_o11_3():
    # Datos de prueba
    usuarios_test = [
        {"nombre": "Ana", "edad": 25, "ciudad": "Lima"},
        {"nombre": "Juan", "edad": 30, "ciudad": "Cusco"},
        {"nombre": "María", "edad": 22, "ciudad": "Arequipa"},
    ]

    # o11.3.1: Usuario encontrado
    result = find_user_info(usuarios_test, "Ana")
    found_ana = isinstance(result, dict) and result.get("nombre") == "Ana"
    record_test("o11.3.1 usuario encontrado", found_ana)

    # o11.3.2: Búsqueda case-insensitive
    result = find_user_info(usuarios_test, "juan")
    found_juan = isinstance(result, dict) and result.get("nombre") == "Juan"
    record_test("o11.3.2 case-insensitive", found_juan)

    # o11.3.3: Usuario no encontrado
    result = find_user_info(usuarios_test, "Pedro")
    record_test("o11.3.3 no encontrado", result is None)

    # o11.3.4: Verificación de tipos
    result = find_user_info(usuarios_test, "María")
    record_test("o11.3.4 retorna dict", isinstance(result, dict))

    # o11.3.5: Lista vacía
    result = find_user_info([], "cualquier")
    record_test("o11.3.5 lista vacía", result is None)


# Run tests for o11.3 🚀
test_o11_3()


# --------------------------------------------------------------------
# o11.4 🔄 Actualizador de Datos ✏️📊
# --------------------------------------------------------------------
def update_inventory(inventario, producto, cantidad):
    """🔄 Update inventory by adding/subtracting product quantity.
    Returns updated inventory dict."""
    # Check if product exists in inventory
    if producto in inventario:
        # Update existing product
        inventario[producto] += cantidad
    else:
        # Add new product
        inventario[producto] = cantidad

    # Ensure no negative quantities
    if inventario[producto] < 0:
        inventario[producto] = 0

    return inventario


def test_o11_4():
    # o11.4.1: Agregar a producto existente
    inv1 = {"manzanas": 10, "peras": 5}
    result = update_inventory(inv1, "manzanas", 5)
    record_test("o11.4.1 agregar existente", result["manzanas"] == 15)

    # o11.4.2: Producto nuevo
    inv2 = {"manzanas": 10}
    result = update_inventory(inv2, "naranjas", 8)
    record_test("o11.4.2 producto nuevo", result.get("naranjas") == 8)

    # o11.4.3: Restar cantidad
    inv3 = {"peras": 12}
    result = update_inventory(inv3, "peras", -7)
    record_test("o11.4.3 restar cantidad", result["peras"] == 5)

    # o11.4.4: Verificación de tipos
    inv4 = {"test": 5}
    result = update_inventory(inv4, "test", 2)
    record_test("o11.4.4 retorna dict", isinstance(result, dict))

    # o11.4.5: Restar más de lo disponible
    inv5 = {"uvas": 3}
    result = update_inventory(inv5, "uvas", -10)
    record_test("o11.4.5 no negativo", result["uvas"] == 0)


# Run tests for o11.4 🚀
test_o11_4()


# --------------------------------------------------------------------
# o11.5 🤝 Combinador de Diccionarios 🔗✨
# --------------------------------------------------------------------
def merge_configs(config1, config2, config3):
    """🤝 Merge three config dictionaries with priority.
    Returns merged dict with config3 > config2 > config1 priority."""
    # Create result dictionary
    resultado = {}

    # Update with configs in priority order (last one wins)
    resultado.update(config1)
    resultado.update(config2)
    resultado.update(config3)

    return resultado


def test_o11_5():
    # o11.5.1: Sin conflictos
    c1 = {"host": "localhost"}
    c2 = {"port": 8080}
    c3 = {"debug": True}
    result = merge_configs(c1, c2, c3)
    no_conflicts = (
        result.get("host") == "localhost"
        and result.get("port") == 8080
        and result.get("debug") == True
    )
    record_test("o11.5.1 sin conflictos", no_conflicts)

    # o11.5.2: Con conflictos de prioridad
    c1 = {"timeout": 30}
    c2 = {"timeout": 60}
    c3 = {"timeout": 90}
    result = merge_configs(c1, c2, c3)
    record_test("o11.5.2 prioridad config3", result["timeout"] == 90)

    # o11.5.3: Algunos diccionarios vacíos
    result = merge_configs({}, {"a": 1}, {})
    record_test("o11.5.3 algunos vacíos", result == {"a": 1})

    # o11.5.4: Verificación de tipos
    result = merge_configs({"x": 1}, {"y": 2}, {"z": 3})
    record_test("o11.5.4 retorna dict", isinstance(result, dict))

    # o11.5.5: Todos vacíos
    result = merge_configs({}, {}, {})
    record_test("o11.5.5 todos vacíos", result == {})


# Run tests for o11.5 🚀
test_o11_5()

# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# 📚 Diccionarios Lab o11 - Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")

print(
    "\n🎯 ¡Felicitaciones! Has completado todos los retos de diccionarios en Python 🐍✨"
)
print("✅ Dominas la creación y validación de diccionarios")
print("✅ Sabes contar y analizar elementos eficientemente")
print("✅ Puedes buscar información en colecciones de datos")
print("✅ Entiendes la actualización dinámica de contenido")
print("✅ Combinas información de múltiples fuentes con prioridades")
