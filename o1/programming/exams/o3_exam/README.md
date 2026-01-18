# 🐍 Examen Python Nivel 3 - Estructuras de Datos y Funciones 🐍

```
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║        ████████╗███████╗███████╗████████╗                  ║
    ║        ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝                  ║
    ║           ██║   █████╗  ███████╗   ██║                     ║
    ║           ██║   ██╔══╝  ╚════██║   ██║                     ║
    ║           ██║   ███████╗███████║   ██║                     ║
    ║           ╚═╝   ╚══════╝╚══════╝   ╚═╝                     ║
    ║                                                            ║
    ║         🐍 PYTHON ADVANCED STRUCTURES EXAM 🐍               ║
    ║                                                            ║
    ║         ✨ Demuestra todo lo que has aprendido ✨           ║
    ║                                                            ║
    ║      🚀 ¡TÚ PUEDES LOGRARLO, PROGRAMADOR! 🚀                ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
```

---

## 📋 Instrucciones Generales

¡Bienvenido al examen de Python Nivel 3, futuro desarrollador! 🐍✨ Este examen valida tu dominio de estructuras de datos avanzadas y funciones. Cada reto es una oportunidad para demostrar tus habilidades profesionales.

**📌 Recomendaciones Importantes:**
- 🔍 Lee cuidadosamente cada problema antes de comenzar
- 📐 Sigue la estructura del código base proporcionado
- ✅ Prueba tu código con todos los casos de prueba
- 💭 Recuerda los tips útiles para cada ejercicio
- 🎯 Mantén la calma y confía en tu conocimiento
- **🏆 ¡ADELANTE PROGRAMADOR! Demuestra todo lo aprendido 💪**

**⏰ Tiempo estimado:** 90 minutos  
**📊 Total de retos:** 12 (3 por tema)

---

## 📦 Tema 1: Tuplas - Datos Inmutables

### o1.1: 🎮 Posición del Jugador

**📖 Historia:** Elliot ⚡ está jugando un videojuego donde su personaje tiene una posición en el mapa. La posición (x=150, y=200) nunca debe cambiar accidentalmente durante el juego, así que usa una tupla para proteger esos datos.

**📝 Descripción:** Tu programa debe crear una tupla con coordenadas x, y y extraer cada valor en variables separadas para validar la posición.

**⚙️ Funcionalidades:**
- Crear tupla `position` con valores (150, 200)
- Extraer x usando índice `position[0]`
- Extraer y usando índice `position[1]`
- Desempaquetar tupla en variables `x` y `y`
- Validar que es tupla y no se puede modificar

**✅ Casos de prueba:**

| Input                       | Expected Output   |
| --------------------------- | ----------------- |
| `x` (acceso índice)         | `150`             |
| `y` (acceso índice)         | `200`             |
| `player_x` (desempaquetado) | `150`             |
| `player_y` (desempaquetado) | `200`             |
| `type(position)`            | `<class 'tuple'>` |

**💻 Código base:**

```python
# Player Position 🎮
position = ()  # your code here 💻
x = 0  # your code here 💻 (access position[0])
y = 0  # your code here 💻 (access position[1])
player_x = 0  # your code here 💻 (unpack position)
player_y = 0  # your code here 💻 (unpack position)

print(f"Posición del jugador: {position}")
print(f"X: {x}, Y: {y}")

# Test cases
print(x == 150)
print(y == 200)
print(player_x == 150)
print(player_y == 200)
print(type(position) == tuple)
```

**💡 Tips:**
- 🔹 Crear: `position = (150, 200)`
- 🔹 Acceder por índice: `x = position[0]`
- 🔹 Desempaquetar: `player_x, player_y = position`
- 🔹 Las tuplas son inmutables

**🚀 Motivación:** ¡Elliot protege la posición de su personaje! ⚡🎮

---

### o1.2: 🎂 Cumpleaños de Fernanda

**📖 Historia:** Fernanda 🧙‍♀️ guarda su cumpleaños en una tupla porque nunca cambia: nació el 12 de marzo de 2008. Necesita separar el día, mes y año para mostrarlos individualmente y calcular su edad.

**📝 Descripción:** Tu programa trabaja con una tupla de fecha y extrae componentes para cálculos.

**⚙️ Funcionalidades:**
- Crear tupla `birthday` con (12, 3, 2008)
- Extraer `day`, `month`, `year` desempaquetando
- Calcular edad (2026 - year)
- Formatear fecha como "DD/MM/YYYY"
- Validar tipo de dato

**✅ Casos de prueba:**

| Input            | Expected Output   |
| ---------------- | ----------------- |
| `day`            | `12`              |
| `month`          | `3`               |
| `year`           | `2008`            |
| `age`            | `18`              |
| `type(birthday)` | `<class 'tuple'>` |

**💻 Código base:**

```python
# Fernanda's Birthday 🎂
birthday = ()  # your code here 💻 (12, 3, 2008)
day = 0  # your code here 💻
month = 0  # your code here 💻
year = 0  # your code here 💻
age = 0  # your code here 💻 (2026 - year)
formatted = ''  # your code here 💻 (format as DD/MM/YYYY)

print(f"Cumpleaños de Fernanda: {formatted}")
print(f"Edad: {age} años")

# Test cases
print(day == 12)
print(month == 3)
print(year == 2008)
print(age == 18)
print(type(birthday) == tuple)
```

**💡 Tips:**
- 🔹 Desempaquetar: `day, month, year = birthday`
- 🔹 Edad: `2026 - year`
- 🔹 Formatear: `f"{day}/{month}/{year}"`
- 🔹 Las tuplas son perfectas para fechas

**🚀 Motivación:** ¡Fernanda celebra con datos inmutables! 🧙‍♀️🎂

---

### o1.3: 🏆 Ranking de Jugadores

**📖 Historia:** Chocolate 🐕 organiza un torneo de videojuegos. Los 3 primeros lugares son: ('Mijael', 'Fe', 'Elliot'). Necesita intercambiar el 1er y 2do lugar porque Fe ganó realmente, y crear un nuevo ranking.

**📝 Descripción:** Tu programa intercambia posiciones en una tupla creando una nueva (las tuplas son inmutables).

**⚙️ Funcionalidades:**
- Crear tupla `ranking` con 3 nombres
- Extraer primer y segundo lugar
- Crear nuevo ranking intercambiando posiciones
- Validar que hay 2 tuplas diferentes
- Comparar rankings

**✅ Casos de prueba:**

| Input               | Expected Output   |
| ------------------- | ----------------- |
| `first`             | `'Mijael'`        |
| `second`            | `'Fe'`            |
| `new_ranking[0]`    | `'Fe'`            |
| `new_ranking[1]`    | `'Mijael'`        |
| `type(new_ranking)` | `<class 'tuple'>` |

**💻 Código base:**

```python
# Player Ranking 🏆
ranking = ()  # your code here 💻 ('Mijael', 'Fe', 'Elliot')
first = ''  # your code here 💻
second = ''  # your code here 💻
third = ''  # your code here 💻
new_ranking = ()  # your code here 💻 (swap first and second)

print(f"Ranking original: {ranking}")
print(f"Ranking corregido: {new_ranking}")

# Test cases
print(first == 'Mijael')
print(second == 'Fe')
print(new_ranking[0] == 'Fe')
print(new_ranking[1] == 'Mijael')
print(type(new_ranking) == tuple)
```

**💡 Tips:**
- 🔹 Desempaquetar: `first, second, third = ranking`
- 🔹 Nuevo ranking: `(second, first, third)`
- 🔹 No puedes modificar tuplas, creas nuevas
- 🔹 Las tuplas son inmutables

**🚀 Motivación:** ¡Chocolate corrige el ranking! 🐕🏆

---

## 📚 Tema 2: Diccionarios - Datos Estructurados

### o2.1: 🎒 Mochila de Aventurero

**📖 Historia:** Doky 🐕 va de aventura y lleva una mochila con items: {'poción': 3, 'espada': 1, 'escudo': 1}. Durante la aventura encuentra 2 pociones más y pierde el escudo. Actualiza su inventario.

**📝 Descripción:** Tu programa modifica valores de un diccionario según eventos del juego.

**⚙️ Funcionalidades:**
- Crear diccionario `backpack` con 3 items
- Sumar 2 al valor de 'poción'
- Eliminar 'escudo' del diccionario
- Calcular total de items
- Validar cambios

**✅ Casos de prueba:**

| Input                  | Expected Output  |
| ---------------------- | ---------------- |
| `backpack['poción']`   | `5`              |
| `backpack['espada']`   | `1`              |
| `'escudo' in backpack` | `False`          |
| `total_items`          | `6` (5 + 1)      |
| `type(backpack)`       | `<class 'dict'>` |

**💻 Código base:**

```python
# Adventurer Backpack 🎒
backpack = {}  # your code here 💻 (poción: 3, espada: 1, escudo: 1)

# Your code here 💻 (add 2 to poción)
# Your code here 💻 (remove escudo)

total_items = 0  # your code here 💻 (sum all values)

print(f"Mochila: {backpack}")
print(f"Total items: {total_items}")

# Test cases
print(backpack['poción'] == 5)
print(backpack['espada'] == 1)
print('escudo' not in backpack)
print(total_items == 6)
print(type(backpack) == dict)
```

**💡 Tips:**
- 🔹 Modificar: `backpack['poción'] += 2`
- 🔹 Eliminar: `del backpack['escudo']`
- 🔹 Sumar valores: `sum(backpack.values())`
- 🔹 Los diccionarios son mutables

**🚀 Motivación:** ¡Doky gestiona su inventario! 🐕🎒

---

### o2.2: 🏪 Tienda de Amorosa

**📖 Historia:** Amorosa 💖 tiene una tienda con precios: {'manzana': 2.5, 'pera': 3.0, 'uva': 4.5}. Un cliente compra 3 manzanas y 2 uvas. Calcula el total a pagar y encuentra el producto más caro.

**📝 Descripción:** Tu programa realiza cálculos con valores de un diccionario.

**⚙️ Funcionalidades:**
- Crear diccionario `prices` con 3 productos
- Calcular costo de 3 manzanas
- Calcular costo de 2 uvas
- Sumar total de la compra
- Encontrar producto más caro (nombre y precio)

**✅ Casos de prueba:**

| Input            | Expected Output  |
| ---------------- | ---------------- |
| `apple_cost`     | `7.5` (3 × 2.5)  |
| `grape_cost`     | `9.0` (2 × 4.5)  |
| `total`          | `16.5`           |
| `most_expensive` | `'uva'`          |
| `type(prices)`   | `<class 'dict'>` |

**💻 Código base:**

```python
# Amorosa's Store 🏪
prices = {}  # your code here 💻 (manzana: 2.5, pera: 3.0, uva: 4.5)
apple_cost = 0  # your code here 💻 (3 × price)
grape_cost = 0  # your code here 💻 (2 × price)
total = 0  # your code here 💻
most_expensive = ''  # your code here 💻 (product name)
max_price = 0  # your code here 💻

print(f"Precios: {prices}")
print(f"Total de compra: ${total}")
print(f"Producto más caro: {most_expensive} (${max_price})")

# Test cases
print(apple_cost == 7.5)
print(grape_cost == 9.0)
print(total == 16.5)
print(most_expensive == 'uva')
print(type(prices) == dict)
```

**💡 Tips:**
- 🔹 Calcular: `prices['manzana'] * 3`
- 🔹 Total: `apple_cost + grape_cost`
- 🔹 Máximo: `max(prices, key=prices.get)`
- 🔹 Precio máximo: `max(prices.values())`

**🚀 Motivación:** ¡Amorosa vende con éxito! 💖🏪

---

### o2.3: 📊 Estadísticas del Equipo

**📖 Historia:** Fe 👨‍🍳 entrena un equipo de deportistas. Tiene sus puntuaciones: {'Elliot': 85, 'Fernanda': 92, 'Mijael': 78}. Necesita calcular el promedio del equipo y identificar al mejor y peor jugador.

**📝 Descripción:** Tu programa analiza un diccionario para obtener estadísticas.

**⚙️ Funcionalidades:**
- Crear diccionario `scores` con 3 jugadores
- Calcular promedio de puntuaciones
- Encontrar puntuación máxima y mínima
- Identificar nombre del mejor jugador
- Contar cuántos aprobaron (≥80)

**✅ Casos de prueba:**

| Input          | Expected Output  |
| -------------- | ---------------- |
| `average`      | `85.0`           |
| `best_player`  | `'Fernanda'`     |
| `worst_player` | `'Mijael'`       |
| `max_score`    | `92`             |
| `type(scores)` | `<class 'dict'>` |

**💻 Código base:**

```python
# Team Statistics 📊
scores = {}  # your code here 💻 (Elliot: 85, Fernanda: 92, Mijael: 78)
average = 0  # your code here 💻
max_score = 0  # your code here 💻
min_score = 0  # your code here 💻
best_player = ''  # your code here 💻
worst_player = ''  # your code here 💻
approved = 0  # your code here 💻 (count >= 80)

print(f"Puntuaciones: {scores}")
print(f"Promedio: {average}")
print(f"Mejor: {best_player} ({max_score})")
print(f"Aprobados: {approved}")

# Test cases
print(average == 85.0)
print(best_player == 'Fernanda')
print(worst_player == 'Mijael')
print(max_score == 92)
print(type(scores) == dict)
```

**💡 Tips:**
- 🔹 Promedio: `sum(scores.values()) / len(scores)`
- 🔹 Mejor: `max(scores, key=scores.get)`
- 🔹 Peor: `min(scores, key=scores.get)`
- 🔹 Contar: usa bucle con condición

**🚀 Motivación:** ¡Fe analiza el rendimiento del equipo! 👨‍🍳📊

---

## 🎯 Tema 3: Sets - Colecciones Únicas

### o3.1: 🎲 Números de Lotería

**📖 Historia:** Mijael 🧑‍💻 compró 3 boletos de lotería con números repetidos: [5, 12, 5, 23, 12, 45, 5]. Necesita saber cuántos números únicos tiene realmente para calcular sus probabilidades.

**📝 Descripción:** Tu programa convierte una lista con duplicados en un set único.

**⚙️ Funcionalidades:**
- Crear lista `tickets` con números duplicados
- Convertir a set para obtener únicos
- Contar números únicos
- Convertir set de vuelta a lista ordenada
- Validar tipo de datos

**✅ Casos de prueba:**

| Input                  | Expected Output   |
| ---------------------- | ----------------- |
| `unique_numbers`       | `{5, 12, 23, 45}` |
| `count`                | `4`               |
| `sorted_list`          | `[5, 12, 23, 45]` |
| `5 in unique_numbers`  | `True`            |
| `type(unique_numbers)` | `<class 'set'>`   |

**💻 Código base:**

```python
# Lottery Numbers 🎲
tickets = [5, 12, 5, 23, 12, 45, 5]
unique_numbers = set()  # your code here 💻
count = 0  # your code here 💻
sorted_list = []  # your code here 💻

print(f"Boletos originales: {tickets}")
print(f"Números únicos: {unique_numbers}")
print(f"Cantidad única: {count}")
print(f"Ordenados: {sorted_list}")

# Test cases
print(unique_numbers == {5, 12, 23, 45})
print(count == 4)
print(sorted_list == [5, 12, 23, 45])
print(5 in unique_numbers)
print(type(unique_numbers) == set)
```

**💡 Tips:**
- 🔹 Convertir: `set(tickets)`
- 🔹 Contar: `len(unique_numbers)`
- 🔹 Ordenar: `sorted(unique_numbers)`
- 🔹 Sets eliminan duplicados automáticamente

**🚀 Motivación:** ¡Mijael calcula sus probabilidades! 🧑‍💻🎲

---

### o3.2: 👥 Amigos en Común

**📖 Historia:** Chocolate 🐕 y Doky 🐕 quieren saber qué amigos tienen en común. Chocolate conoce a: {'Ana', 'Luis', 'Pedro', 'María'}. Doky conoce a: {'Carlos', 'Luis', 'María', 'José'}. ¿Quiénes son sus amigos en común?

**📝 Descripción:** Tu programa usa intersección de sets para encontrar elementos comunes.

**⚙️ Funcionalidades:**
- Crear set `chocolate_friends` con 4 amigos
- Crear set `doky_friends` con 4 amigos
- Calcular intersección (amigos en común)
- Contar cuántos son
- Validar que ambos son sets

**✅ Casos de prueba:**

| Input              | Expected Output     |
| ------------------ | ------------------- |
| `common`           | `{'Luis', 'María'}` |
| `count`            | `2`                 |
| `'Luis' in common` | `True`              |
| `'Ana' in common`  | `False`             |
| `type(common)`     | `<class 'set'>`     |

**💻 Código base:**

```python
# Friends in Common 👥
chocolate_friends = set()  # your code here 💻 (Ana, Luis, Pedro, María)
doky_friends = set()  # your code here 💻 (Carlos, Luis, María, José)
common = set()  # your code here 💻 (intersection)
count = 0  # your code here 💻
only_chocolate = set()  # your code here 💻 (chocolate - doky)

print(f"Amigos de Chocolate: {chocolate_friends}")
print(f"Amigos de Doky: {doky_friends}")
print(f"Amigos en común: {common}")
print(f"Solo de Chocolate: {only_chocolate}")

# Test cases
print(common == {'Luis', 'María'})
print(count == 2)
print('Luis' in common)
print('Ana' not in common)
print(type(common) == set)
```

**💡 Tips:**
- 🔹 Intersección: `chocolate_friends & doky_friends`
- 🔹 Diferencia: `chocolate_friends - doky_friends`
- 🔹 Contar: `len(common)`
- 🔹 `&` encuentra elementos en AMBOS sets

**🚀 Motivación:** ¡Chocolate y Doky encuentran amigos comunes! 🐕👥

---

### o3.3: 🎯 Objetivos Cumplidos

**📖 Historia:** Fernanda 🧙‍♀️ tenía 5 objetivos del año: {'estudiar', 'ejercicio', 'leer', 'viajar', 'programar'}. Ya cumplió 3: {'estudiar', 'leer', 'programar'}. ¿Cuáles le faltan por cumplir?

**📝 Descripción:** Tu programa usa diferencia de sets para encontrar elementos faltantes.

**⚙️ Funcionalidades:**
- Crear set `goals` con 5 objetivos
- Crear set `completed` con 3 cumplidos
- Calcular diferencia (faltantes)
- Contar cuántos cumplió y cuántos faltan
- Calcular porcentaje de progreso

**✅ Casos de prueba:**

| Input             | Expected Output           |
| ----------------- | ------------------------- |
| `pending`         | `{'ejercicio', 'viajar'}` |
| `completed_count` | `3`                       |
| `pending_count`   | `2`                       |
| `progress`        | `60.0` (3/5 × 100)        |
| `type(pending)`   | `<class 'set'>`           |

**💻 Código base:**

```python
# Completed Goals 🎯
goals = set()  # your code here 💻 (estudiar, ejercicio, leer, viajar, programar)
completed = set()  # your code here 💻 (estudiar, leer, programar)
pending = set()  # your code here 💻 (goals - completed)
completed_count = 0  # your code here 💻
pending_count = 0  # your code here 💻
progress = 0  # your code here 💻 (percentage)

print(f"Objetivos: {goals}")
print(f"Completados: {completed}")
print(f"Pendientes: {pending}")
print(f"Progreso: {progress}%")

# Test cases
print(pending == {'ejercicio', 'viajar'})
print(completed_count == 3)
print(pending_count == 2)
print(progress == 60.0)
print(type(pending) == set)
```

**💡 Tips:**
- 🔹 Diferencia: `goals - completed`
- 🔹 Contar: `len(completed)`, `len(pending)`
- 🔹 Porcentaje: `(completed_count / len(goals)) * 100`
- 🔹 La diferencia muestra lo que falta

**🚀 Motivación:** ¡Fernanda revisa su progreso! 🧙‍♀️🎯

---

## ⚡ Tema 4: Funciones - Código Reutilizable

### o4.1: 🎉 Generador de Mensajes

**📖 Historia:** Elliot ⚡ organiza una fiesta y necesita generar mensajes de invitación personalizados. Crea una función `create_invitation(name, event)` que retorna "¡Hola {name}! Estás invitado a {event}".

**📝 Descripción:** Tu programa define una función básica con parámetros y retorno de string.

**⚙️ Funcionalidades:**
- Definir función `create_invitation(name, event)`
- Recibir 2 parámetros: name y event
- Retornar string formateado con invitación
- Llamar función con 3 nombres diferentes
- Validar que la función existe y retorna strings

**✅ Casos de prueba:**

| Input                                   | Expected Output                           |
| --------------------------------------- | ----------------------------------------- |
| `create_invitation('Fe', 'cumpleaños')` | `'¡Hola Fe! Estás invitado a cumpleaños'` |
| `invite1`                               | `'¡Hola Fe! Estás invitado a cumpleaños'` |
| `invite2`                               | `'¡Hola Mijael! Estás invitado a fiesta'` |
| `callable(create_invitation)`           | `True`                                    |
| `type(invite1)`                         | `<class 'str'>`                           |

**💻 Código base:**

```python
# Invitation Generator 🎉

# Your code here 💻 (define create_invitation function)

invite1 = ''  # your code here 💻 (call with 'Fe', 'cumpleaños')
invite2 = ''  # your code here 💻 (call with 'Mijael', 'fiesta')
invite3 = ''  # your code here 💻 (call with 'Fernanda', 'cena')

print(invite1)
print(invite2)
print(invite3)

# Test cases
print(invite1 == '¡Hola Fe! Estás invitado a cumpleaños')
print(invite2 == '¡Hola Mijael! Estás invitado a fiesta')
print(invite3 == '¡Hola Fernanda! Estás invitado a cena')
print(callable(create_invitation))
print(type(invite1) == str)
```

**💡 Tips:**
- 🔹 Definir: `def create_invitation(name, event):`
- 🔹 Retornar: `return f"¡Hola {name}! Estás invitado a {event}"`
- 🔹 Llamar: `create_invitation('Fe', 'cumpleaños')`
- 🔹 `callable()` verifica si es función

**🚀 Motivación:** ¡Elliot invita a todos con código! ⚡🎉

---

### o4.2: 🧮 Calculadora de Descuentos

**📖 Historia:** Amorosa 💖 está organizando una mega venta de San Valentín en su tienda. Quiere sorprender a sus clientes con descuentos especiales, pero necesita asegurarse de que nadie intente hackear el sistema poniendo descuentos del 500% y llevarse dinero gratis. ¡Necesita una función que calcule los descuentos de forma segura y justa para todos!

**📝 Descripción:** Crea una función que reciba un precio y un porcentaje de descuento, calcule el precio final después del descuento, y valide que el descuento sea válido (entre 0 y 100). Si el descuento no es válido, retorna el precio original sin cambios.

**⚙️ Funcionalidades:**
- Definir función `apply_discount(price, discount_percent)`
- Validar que discount esté entre 0 y 100
- Calcular precio final: `price * (1 - discount/100)`
- Retornar precio original si descuento inválido
- Probar con diferentes descuentos

**✅ Casos de prueba:**

| Input                           | Expected Output   |
| ------------------------------- | ----------------- |
| `apply_discount(100, 20)`       | `80.0`            |
| `apply_discount(200, 50)`       | `100.0`           |
| `apply_discount(150, 0)`        | `150.0`           |
| `apply_discount(100, 150)`      | `100` (invalid)   |
| `type(apply_discount(100, 20))` | `<class 'float'>` |

**💻 Código base:**

```python
# Discount Calculator 🧮

# Your code here 💻 (define apply_discount function)

result1 = 0  # your code here 💻 (100, 20%)
result2 = 0  # your code here 💻 (200, 50%)
result3 = 0  # your code here 💻 (150, 0%)
result4 = 0  # your code here 💻 (100, 150% - invalid)

print(f"$100 con 20%: ${result1}")
print(f"$200 con 50%: ${result2}")
print(f"$150 con 0%: ${result3}")
print(f"$100 con 150%: ${result4}")

# Test cases
print(result1 == 80.0)
print(result2 == 100.0)
print(result3 == 150.0)
print(result4 == 100)
print(type(result1) == float)
```

**💡 Tips:**
- 🔹 Validar primero: `if discount_percent < 0 or discount_percent > 100:`
- 🔹 Retornar original: `return price`
- 🔹 Calcular descuento: `price * (1 - discount_percent / 100)`
- 🔹 Usar if-else para validación

**🚀 Motivación:** ¡Amorosa protege su tienda con código! 💖🧮

---

### o4.3: 🎮 Calculadora de Nivel

**📖 Historia:** Chocolate 🐕 está jugando su videojuego favorito y cada vez que derrota enemigos gana puntos de experiencia (XP). Descubrió que cada 100 puntos de XP sube 1 nivel. Ahora quiere crear una función mágica que le diga en qué nivel está según sus puntos totales. ¡Así podrá presumirle a Doky lo fuerte que está su personaje!

**📝 Descripción:** Crea una función que reciba puntos de experiencia y calcule el nivel del jugador. Cada 100 puntos equivale a 1 nivel. También debe calcular cuántos puntos le faltan para el siguiente nivel. Si los puntos son negativos, debe retornar nivel 0.

**⚙️ Funcionalidades:**
- Definir función `calculate_level(xp_points)`
- Calcular nivel: `xp_points // 100`
- Calcular XP faltante para siguiente nivel
- Validar que XP no sea negativo
- Retornar tupla con (nivel, xp_faltante)

**✅ Casos de prueba:**

| Input                  | Expected Output |
| ---------------------- | --------------- |
| `calculate_level(250)` | `(2, 50)`       |
| `calculate_level(0)`   | `(0, 100)`      |
| `calculate_level(99)`  | `(0, 1)`        |
| `calculate_level(500)` | `(5, 0)`        |
| `calculate_level(-50)` | `(0, 100)`      |

**💻 Código base:**

```python
# Level Calculator 🎮

# Your code here 💻 (define calculate_level function)
# The function should return a tuple: (level, xp_to_next_level)

level1, xp1 = (0, 0)  # your code here 💻 (250 XP)
level2, xp2 = (0, 0)  # your code here 💻 (0 XP)
level3, xp3 = (0, 0)  # your code here 💻 (99 XP)
level4, xp4 = (0, 0)  # your code here 💻 (500 XP)
level5, xp5 = (0, 0)  # your code here 💻 (-50 XP - invalid)

print(f"250 XP: Nivel {level1}, faltan {xp1} XP")
print(f"0 XP: Nivel {level2}, faltan {xp2} XP")
print(f"99 XP: Nivel {level3}, faltan {xp3} XP")
print(f"500 XP: Nivel {level4}, faltan {xp4} XP")
print(f"-50 XP: Nivel {level5}, faltan {xp5} XP")

# Test cases
print(level1 == 2 and xp1 == 50)
print(level2 == 0 and xp2 == 100)
print(level3 == 0 and xp3 == 1)
print(level4 == 5 and xp4 == 0)
print(level5 == 0 and xp5 == 100)
```

**💡 Tips:**
- 🔹 Nivel: `xp_points // 100` (división entera)
- 🔹 XP faltante: `100 - (xp_points % 100)`
- 🔹 Si XP % 100 == 0: faltan 0 puntos
- 🔹 Validar XP negativo primero: `if xp_points < 0:`
- 🔹 Retornar tupla: `return (level, xp_needed)`

**🚀 Motivación:** ¡Chocolate sube de nivel con matemáticas! 🐕🎮
