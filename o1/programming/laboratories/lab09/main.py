# **📝 Guía de Retos - Listas en Python 🐍✨**
# Soluciones completas de todos los retos

print("🌟 ¡Bienvenido a la Guía de Retos de Listas en Python! 🌟")
print("=" * 60)

# =============================================================================
# RETO 1: Creador de Lista de Compras 🛒📝
# =============================================================================

print("\n🛒 RETO 1: Creador de Lista de Compras")
print("-" * 40)


def reto1_lista_compras():
    """Reto 1: Creador de Lista de Compras 🛒📝"""

    # Caso de prueba 1: ["pan","leche","huevos","queso"]
    compras = []
    compras.append("pan")
    compras.append("leche")
    compras.append("huevos")
    compras.append("queso")

    first_product = compras[0]  # Primer elemento
    last_product = compras[-1]  # Último elemento
    total_products = len(compras)  # Total de productos

    print(f"📝 Lista de compras: {compras}")
    print(f"🥖 Primer producto: {first_product}")
    print(f"🧀 Último producto: {last_product}")
    print(f"📊 Total de productos: {total_products}")

    # Verificar casos de prueba
    print("\n🧪 Casos de prueba:")
    print(
        "🧪 ",
        first_product == "pan" and last_product == "queso" and total_products == 4,
    )

    # Probar otros casos
    casos = [
        ["manzanas", "arroz", "pollo", "agua"],
        ["pasta", "tomate", "cebolla", "ajo"],
        ["yogur", "cereales", "bananas", "miel"],
        ["salmón", "limón", "papa", "aceite"],
    ]

    resultados_esperados = [
        ("manzanas", "agua", 4),
        ("pasta", "ajo", 4),
        ("yogur", "miel", 4),
        ("salmón", "aceite", 4),
    ]

    for i, caso in enumerate(casos):
        esperado = resultados_esperados[i]
        first = caso[0]
        last = caso[-1]
        total = len(caso)
        resultado = (
            first == esperado[0] and last == esperado[1] and total == esperado[2]
        )
        print("🧪 ", resultado)


reto1_lista_compras()

# =============================================================================
# RETO 2: Analizador de Números 🔢📊
# =============================================================================

print("\n\n🔢 RETO 2: Analizador de Números")
print("-" * 40)


def reto2_analizador_numeros():
    """Reto 2: Analizador de Números 🔢📊"""

    # Caso de prueba 1: [5,2,8,1,9]
    numeros = [5, 2, 8, 1, 9]

    max_number = max(numeros)  # Número mayor
    min_number = min(numeros)  # Número menor
    average = sum(numeros) / len(numeros)  # Promedio

    print(f"🔢 Lista de números: {numeros}")
    print(f"⬆️  Número mayor: {max_number}")
    print(f"⬇️  Número menor: {min_number}")
    print(f"📊 Promedio: {average}")

    # Verificar casos de prueba
    print("\n🧪 Casos de prueba:")
    print("🧪 ", max_number == 9 and min_number == 1 and average == 5.0)

    # Probar otros casos
    casos_numeros = [
        [10, 15, 3, 7, 12],  # mayor=15, menor=3, promedio=9.4
        [4, 4, 4, 4],  # mayor=4, menor=4, promedio=4.0
        [20, 30, 10],  # mayor=30, menor=10, promedio=20.0
        [6, 8, 2, 9, 5],  # mayor=9, menor=2, promedio=6.0
    ]

    resultados_esperados = [(15, 3, 9.4), (4, 4, 4.0), (30, 10, 20.0), (9, 2, 6.0)]

    for i, caso in enumerate(casos_numeros):
        esperado = resultados_esperados[i]
        max_num = max(caso)
        min_num = min(caso)
        avg = sum(caso) / len(caso)
        resultado = (
            max_num == esperado[0] and min_num == esperado[1] and avg == esperado[2]
        )
        print("🧪 ", resultado)


reto2_analizador_numeros()

# =============================================================================
# RETO 3: Explorador de Slicing 🍰✂️
# =============================================================================

print("\n\n🍰 RETO 3: Explorador de Slicing")
print("-" * 40)


def reto3_explorador_slicing():
    """Reto 3: Explorador de Slicing 🍰✂️"""

    # Caso de prueba 1: [1,2,3,4,5,6,7,8]
    lista = [1, 2, 3, 4, 5, 6, 7, 8]

    first_three = lista[:3]  # Primeros 3 elementos
    last_two = lista[-2:]  # Últimos 2 elementos
    middle_slice = lista[2:6]  # Elementos del índice 2 al 5
    even_positions = lista[::2]  # Elementos en posiciones pares

    print(f"📝 Lista original: {lista}")
    print(f"✂️  Primeros 3: {first_three}")
    print(f"✂️  Últimos 2: {last_two}")
    print(f"✂️  Del medio (2-5): {middle_slice}")
    print(f"✂️  Posiciones pares: {even_positions}")

    # Verificar casos de prueba
    print("\n🧪 Casos de prueba:")
    resultado1 = (
        first_three == [1, 2, 3]
        and last_two == [7, 8]
        and middle_slice == [3, 4, 5, 6]
        and even_positions == [1, 3, 5, 7]
    )
    print("🧪 ", resultado1)

    # Probar otros casos
    casos = [
        [10, 20, 30, 40, 50, 60, 70, 80],
        ["a", "b", "c", "d", "e", "f", "g", "h"],
        [5, 15, 25, 35, 45, 55, 65, 75],
        [2, 4, 6, 8, 10, 12, 14, 16],
    ]

    resultados_esperados = [
        ([10, 20, 30], [70, 80], [30, 40, 50, 60], [10, 30, 50, 70]),
        (["a", "b", "c"], ["g", "h"], ["c", "d", "e", "f"], ["a", "c", "e", "g"]),
        ([5, 15, 25], [65, 75], [25, 35, 45, 55], [5, 25, 45, 65]),
        ([2, 4, 6], [14, 16], [6, 8, 10, 12], [2, 6, 10, 14]),
    ]

    for i, caso in enumerate(casos):
        esperado = resultados_esperados[i]
        first3 = caso[:3]
        last2 = caso[-2:]
        middle = caso[2:6]
        pares = caso[::2]
        resultado = (
            first3 == esperado[0]
            and last2 == esperado[1]
            and middle == esperado[2]
            and pares == esperado[3]
        )
        print("🧪 ", resultado)


reto3_explorador_slicing()

# =============================================================================
# RETO 4: Buscador y Contador 🔍📊
# =============================================================================

print("\n\n🔍 RETO 4: Buscador y Contador")
print("-" * 40)


def reto4_buscador_contador():
    """Reto 4: Buscador y Contador 🔍📊"""

    # Caso de prueba 1: [1,2,3,2,4,2], buscar1=2, buscar2=5
    lista = [1, 2, 3, 2, 4, 2]
    buscar1 = 2
    buscar2 = 5

    element1_exists = buscar1 in lista  # ¿Existe elemento1?
    element1_count = lista.count(buscar1)  # ¿Cuántas veces aparece?
    element1_index = lista.index(buscar1)  # ¿En qué posición está?
    element2_exists = buscar2 in lista  # ¿Existe elemento2?

    print(f"📝 Lista: {lista}")
    print(f"🔍 Buscar elemento: {buscar1}")
    print(f"✅ ¿Existe {buscar1}?: {element1_exists}")
    print(f"📊 Apariciones de {buscar1}: {element1_count}")
    print(f"📍 Primera posición de {buscar1}: {element1_index}")
    print(f"❌ ¿Existe {buscar2}?: {element2_exists}")

    # Verificar casos de prueba
    print("\n🧪 Casos de prueba:")
    resultado1 = (
        element1_exists == True
        and element1_count == 3
        and element1_index == 1
        and element2_exists == False
    )
    print("🧪 ", resultado1)

    # Probar otros casos
    casos = [
        (
            ["a", "b", "c", "b", "d"],
            "b",
            "e",
        ),  # existe1=True, count1=2, index1=1, existe2=False
        (
            [10, 20, 10, 30, 10],
            10,
            40,
        ),  # existe1=True, count1=3, index1=0, existe2=False
        ([5, 7, 5, 8, 9], 5, 8),  # existe1=True, count1=2, index1=0, existe2=True
        ([1, 1, 1, 1], 1, 2),  # existe1=True, count1=4, index1=0, existe2=False
    ]

    resultados_esperados = [
        (True, 2, 1, False),
        (True, 3, 0, False),
        (True, 2, 0, True),
        (True, 4, 0, False),
    ]

    for i, caso in enumerate(casos):
        lista_caso, elem1, elem2 = caso
        esperado = resultados_esperados[i]

        existe1 = elem1 in lista_caso
        count1 = lista_caso.count(elem1)
        index1 = lista_caso.index(elem1) if existe1 else -1
        existe2 = elem2 in lista_caso

        resultado = (
            existe1 == esperado[0]
            and count1 == esperado[1]
            and index1 == esperado[2]
            and existe2 == esperado[3]
        )
        print("🧪 ", resultado)


reto4_buscador_contador()

# =============================================================================
# RETO 5: Organizador de Datos 🗂️📋
# =============================================================================

print("\n\n🗂️ RETO 5: Organizador de Datos")
print("-" * 40)


def reto5_organizador_datos():
    """Reto 5: Organizador de Datos 🗂️📋"""

    # Caso de prueba 1: inicial=["a","b","c"], agregar=["d","e"], eliminar="b"
    inicial = ["a", "b", "c"]
    agregar = ["d", "e"]
    eliminar = "b"

    # Crear una copia para no modificar la original
    final_list = inicial.copy()

    # Agregar elementos
    for elemento in agregar:
        final_list.append(elemento)

    # Eliminar elemento
    if eliminar in final_list:
        final_list.remove(eliminar)

    total_elements = len(final_list)  # Contar elementos finales
    element_removed = eliminar  # Elemento que se eliminó

    print(f"📝 Lista inicial: {inicial}")
    print(f"➕ Elementos a agregar: {agregar}")
    print(f"➖ Elemento a eliminar: {eliminar}")
    print(f"🗂️ Lista final: {final_list}")
    print(f"📊 Total de elementos: {total_elements}")
    print(f"❌ Elemento eliminado: {element_removed}")
    print(f"✅ ¿'{element_removed}' ya no está?: {element_removed not in final_list}")

    # Verificar casos de prueba
    print("\n🧪 Casos de prueba:")
    resultado1 = (
        final_list == ["a", "c", "d", "e"]
        and total_elements == 4
        and element_removed not in final_list
    )
    print("🧪 ", resultado1)

    # Probar otros casos
    casos = [
        ([1, 2, 3], [4, 5], 2),  # final=[1,3,4,5], total=4
        (["x", "y"], ["z", "w"], "x"),  # final=["y","z","w"], total=3
        ([10, 20], [30, 40], 10),  # final=[20,30,40], total=3
        (
            ["red", "blue"],
            ["green", "yellow"],
            "red",
        ),  # final=["blue","green","yellow"], total=3
    ]

    resultados_esperados = [
        ([1, 3, 4, 5], 4),
        (["y", "z", "w"], 3),
        ([20, 30, 40], 3),
        (["blue", "green", "yellow"], 3),
    ]

    for i, caso in enumerate(casos):
        lista_inicial, elementos_agregar, elemento_eliminar = caso
        esperado = resultados_esperados[i]

        # Procesar caso
        lista_temp = lista_inicial.copy()
        for elem in elementos_agregar:
            lista_temp.append(elem)
        if elemento_eliminar in lista_temp:
            lista_temp.remove(elemento_eliminar)

        total = len(lista_temp)
        no_esta = elemento_eliminar not in lista_temp

        resultado = lista_temp == esperado[0] and total == esperado[1] and no_esta
        print("🧪 ", resultado)


reto5_organizador_datos()

# =============================================================================
# RESUMEN FINAL 🎯
# =============================================================================

print("\n" + "=" * 60)
print("🎉 ¡FELICITACIONES! Has completado todos los retos de Listas 🎉")
print("=" * 60)

print("\n🏆 HABILIDADES DOMINADAS:")
print("✅ Crear y manipular listas con append() y remove()")
print("✅ Analizar datos con max(), min(), sum() y len()")
print("✅ Usar slicing para extraer porciones específicas")
print("✅ Buscar y contar elementos con in, count() e index()")
print("✅ Modificar listas dinámicamente según necesidades")

print("\n🚀 PRÓXIMO PASO:")
print("¡Ahora puedes combinar listas con bucles for para")
print("procesar datos de manera más eficiente y poderosa!")

print("\n💪 ¡Sigue practicando y construyendo proyectos increíbles! 🐍✨")
