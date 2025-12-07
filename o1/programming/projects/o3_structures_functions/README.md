# 🐍 Python Nivel 3: Estructuras de Datos y Funciones

```
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║           🐍  PYTHON PROGRAMMING COURSE  🐍             ║
    ║                                                        ║
    ║              ∩＿＿＿∩                                   ║
    ║             /        \                                 ║
    ║            /  ●    ●  \      Level 3                   ║
    ║           |     ▼      |     Advanced                  ║
    ║           |   \___/    |                               ║
    ║            \__________/                                ║
    ║                                                        ║
    ║      Tuples • Dictionaries • Sets • Functions          ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
```

## 📖 Introducción

¡Bienvenido al Nivel 3! 🎉 Has dominado listas y control de flujo, ahora es momento de explorar estructuras de datos más avanzadas y crear código reutilizable con funciones. En este nivel aprenderás a trabajar con tuplas inmutables, diccionarios poderosos, sets únicos y funciones profesionales.

## 🎯 Descripción de la Guía

Esta guía está diseñada para estudiantes que completaron el Nivel 2 y están listos para estructuras de datos avanzadas.

### ✨ ¿Qué aprenderás?

- 📦 **o3.1 - Tuplas**: Secuencias inmutables y empaquetado de datos
- 📚 **o3.2 - Diccionarios**: Pares clave-valor y estructuras complejas
- 🎯 **o3.3 - Sets**: Elementos únicos y operaciones de conjuntos
- ⚡ **o3.4 - Funciones**: Código reutilizable, parámetros y retornos

---

## o3.1: Tuplas - Secuencias Inmutables

### 🎯 Descripción del Tema

Las tuplas son como listas pero inmutables (no se pueden modificar después de crearlas). Son perfectas para datos que no deben cambiar: coordenadas, fechas, configuraciones. Aprenderás a crear tuplas, desempaquetarlas y usarlas eficientemente.

---

### o3.1.1: 📍 Coordenadas Geográficas

**📖 Historia:** Fernanda 🧙‍♀️ almacena las coordenadas de su castillo: latitud -12.0464, longitud -77.0428 (Lima, Perú). Las coordenadas nunca deben cambiar, así que usa una tupla.

**📝 Descripción:** Tu programa debe crear una tupla con coordenadas y acceder a sus elementos.

**⚙️ Funcionalidades:**
- Crear tupla con 2 valores (latitud, longitud)
- Acceder a elementos con índices
- Desempaquetar tupla en variables
- Intentar validar inmutabilidad
- Obtener longitud de la tupla

**✅ Casos de prueba:**

| Input                  | Expected Output   |
| ---------------------- | ----------------- |
| `coords[0]`            | `-12.0464`        |
| `coords[1]`            | `-77.0428`        |
| `lat` (desempaquetado) | `-12.0464`        |
| `len(coords)`          | `2`               |
| `type(coords)`         | `<class 'tuple'>` |

**💻 Código base:**

```python
# Geographic Coordinates 📍
coords = ()  # your code here 💻
lat = 0  # your code here 💻 (unpack from coords)
lon = 0  # your code here 💻 (unpack from coords)

print(f"Coordenadas: {coords}")
print(f"Latitud: {lat}, Longitud: {lon}")

# Test cases
print(coords[0] == -12.0464)
print(coords[1] == -77.0428)
print(lat == -12.0464)
print(len(coords) == 2)
print(type(coords) == tuple)
```

**💡 Tips:**
- 🔹 Crear tupla: `coords = (-12.0464, -77.0428)`
- 🔹 Acceso: `coords[0]` para primer elemento
- 🔹 Desempaquetar: `lat, lon = coords`
- 🔹 Las tuplas son inmutables

**🚀 Motivación:** ¡Proteges datos importantes con tuplas! 📍✨

---

### o3.1.2: 📅 Fecha de Nacimiento

**📖 Historia:** Elliot ⚡ guarda su fecha de nacimiento como tupla: (15, 8, 2010) que representa día, mes, año. Necesita acceder a cada componente y formatear la fecha.

**📝 Descripción:** Tu programa trabaja con una tupla de 3 elementos representando una fecha.

**⚙️ Funcionalidades:**
- Crear tupla con día, mes, año
- Acceder a cada componente
- Desempaquetar en variables
- Formatear fecha como string
- Validar cantidad de elementos

**✅ Casos de prueba:**

| Input             | Expected Output   |
| ----------------- | ----------------- |
| `birthdate[0]`    | `15`              |
| `birthdate[1]`    | `8`               |
| `birthdate[2]`    | `2010`            |
| `formatted`       | `'15/08/2010'`    |
| `type(birthdate)` | `<class 'tuple'>` |

**💻 Código base:**

```python
# Birth Date 📅
birthdate = ()  # your code here 💻 (15, 8, 2010)
day = 0  # your code here 💻
month = 0  # your code here 💻
year = 0  # your code here 💻
formatted = ''  # your code here 💻 (format as dd/mm/yyyy)

print(f"Fecha de nacimiento: {formatted}")
print(f"Día: {day}, Mes: {month}, Año: {year}")

# Test cases
print(birthdate[0] == 15)
print(birthdate[1] == 8)
print(birthdate[2] == 2010)
print(formatted == '15/08/2010')
print(type(birthdate) == tuple)
```

**💡 Tips:**
- 🔹 Tupla: `(15, 8, 2010)`
- 🔹 Desempaquetar: `day, month, year = birthdate`
- 🔹 Formatear: `f"{day}/{month}/{year}"`
- 🔹 Usa `str()` si necesitas conversión

**🚀 Motivación:** ¡Elliot organiza su información personal! ⚡📅

---

### o3.1.3: 🎨 Colores RGB

**📖 Historia:** Fe 👨‍🍳 define colores usando tuplas RGB. El color rojo es (255, 0, 0). Necesita crear varios colores y calcular el promedio de sus componentes.

**📝 Descripción:** Tu programa trabaja con múltiples tuplas y realiza operaciones con sus valores.

**⚙️ Funcionalidades:**
- Crear 3 tuplas de colores RGB
- Acceder a componentes individuales
- Calcular suma de componentes de un color
- Comparar dos colores
- Guardar colores en una lista

**✅ Casos de prueba:**

| Input         | Expected Output   |
| ------------- | ----------------- |
| `red[0]`      | `255`             |
| `green[1]`    | `255`             |
| `red_sum`     | `255` (255+0+0)   |
| `len(colors)` | `3`               |
| `type(red)`   | `<class 'tuple'>` |

**💻 Código base:**

```python
# RGB Colors 🎨
red = ()  # your code here 💻 (255, 0, 0)
green = ()  # your code here 💻 (0, 255, 0)
blue = ()  # your code here 💻 (0, 0, 255)
red_sum = 0  # your code here 💻 (sum of red components)
colors = []  # your code here 💻 (list with all 3 colors)

print(f"Rojo: {red}")
print(f"Verde: {green}")
print(f"Azul: {blue}")
print(f"Suma componentes rojo: {red_sum}")

# Test cases
print(red[0] == 255)
print(green[1] == 255)
print(red_sum == 255)
print(len(colors) == 3)
print(type(red) == tuple)
```

**💡 Tips:**
- 🔹 RGB: `(rojo, verde, azul)` cada valor 0-255
- 🔹 Suma: `red[0] + red[1] + red[2]` o `sum(red)`
- 🔹 Lista de tuplas: `[red, green, blue]`
- 🔹 Tuplas dentro de listas son comunes

**🚀 Motivación:** ¡Fe diseña con colores inmutables! 👨‍🍳🎨

---

### o3.1.4: 📊 Estadísticas de Jugador

**📖 Historia:** Chocolate 🐕 guarda las estadísticas de un jugador: (nombre, edad, puntos, nivel). Necesita acceder a los datos y encontrar el máximo y mínimo de los valores numéricos.

**📝 Descripción:** Tu programa trabaja con una tupla mixta (string y números).

**⚙️ Funcionalidades:**
- Crear tupla con datos mixtos
- Desempaquetar todos los valores
- Obtener máximo y mínimo de valores numéricos
- Calcular promedio de puntos y nivel
- Validar tipo de datos

**✅ Casos de prueba:**

| Input          | Expected Output                  |
| -------------- | -------------------------------- |
| `player[0]`    | `'Elliot'`                       |
| `player[2]`    | `1500`                           |
| `max_value`    | `92` (max de age, points, level) |
| `average`      | `796.5` ((1500+93)/2)            |
| `type(player)` | `<class 'tuple'>`                |

**💻 Código base:**

```python
# Player Stats 📊
player = ()  # your code here 💻 ('Elliot', 25, 1500, 92)
name = ''  # your code here 💻
age = 0  # your code here 💻
points = 0  # your code here 💻
level = 0  # your code here 💻
max_value = 0  # your code here 💻 (max of numeric values)
average = 0  # your code here 💻 (average of points and level)

print(f"Jugador: {name}")
print(f"Edad: {age}, Puntos: {points}, Nivel: {level}")
print(f"Valor máximo: {max_value}")

# Test cases
print(player[0] == 'Elliot')
print(player[2] == 1500)
print(max_value == 1500)
print(average == 796.5)
print(type(player) == tuple)
```

**💡 Tips:**
- 🔹 Tupla mixta: `('Elliot', 25, 1500, 92)`
- 🔹 Desempaquetar: `name, age, points, level = player`
- 🔹 Máximo: `max(age, points, level)`
- 🔹 Promedio: `(points + level) / 2`

**🚀 Motivación:** ¡Chocolate analiza estadísticas de juego! 🐕📊

---

### o3.1.5: 🔄 Intercambio de Valores

**📖 Historia:** Amorosa 💖 necesita intercambiar dos valores: a=10, b=20. En Python puede hacerlo elegantemente con tuplas en una línea: a, b = b, a.

**📝 Descripción:** Tu programa usa tuplas para intercambiar valores y realizar operaciones múltiples.

**⚙️ Funcionalidades:**
- Crear dos variables con valores iniciales
- Intercambiar valores usando tuplas
- Verificar que se intercambiaron correctamente
- Realizar múltiples intercambios
- Retornar tupla con ambos valores

**✅ Casos de prueba:**

| Input                  | Expected Output   |
| ---------------------- | ----------------- |
| `a inicial, b inicial` | `10, 20`          |
| `a final, b final`     | `20, 10`          |
| `result`               | `(20, 10)`        |
| `a + b`                | `30`              |
| `type(result)`         | `<class 'tuple'>` |

**💻 Código base:**

```python
# Value Swap 🔄
a = 10
b = 20
initial = ()  # your code here 💻 (save initial values as tuple)

# Your code here 💻 (swap a and b)

final = ()  # your code here 💻 (save final values as tuple)
result = ()  # your code here 💻 (should be (20, 10))

print(f"Inicial: a={initial[0]}, b={initial[1]}")
print(f"Final: a={a}, b={b}")
print(f"Resultado: {result}")

# Test cases
print(initial == (10, 20))
print(final == (20, 10))
print(result == (20, 10))
print(a + b == 30)
print(type(result) == tuple)
```

**💡 Tips:**
- 🔹 Guardar: `initial = (a, b)`
- 🔹 Intercambiar: `a, b = b, a`
- 🔹 Esto es empaquetado/desempaquetado simultáneo
- 🔹 Muy pythonic y eficiente

**🚀 Motivación:** ¡Amorosa intercambia datos elegantemente! 💖🔄

---

## o3.2: Diccionarios - Estructuras Clave-Valor

### 🎯 Descripción del Tema

Los diccionarios almacenan pares clave-valor, como una base de datos en miniatura. Son perfectos para almacenar información estructurada: usuarios, configuraciones, inventarios. Aprenderás a crear, modificar, iterar y usar métodos de diccionarios.

---

### o3.2.1: 👤 Perfil de Usuario

**📖 Historia:** Doky 🐕 crea un perfil de usuario con nombre, edad, email y ciudad. Necesita almacenar esta información estructurada y acceder a cada campo fácilmente.

**📝 Descripción:** Tu programa crea un diccionario básico y accede a sus valores.

**⚙️ Funcionalidades:**
- Crear diccionario con 4 pares clave-valor
- Acceder a valores usando claves
- Modificar un valor existente
- Agregar una nueva clave-valor
- Obtener cantidad de claves

**✅ Casos de prueba:**

| Input           | Expected Output          |
| --------------- | ------------------------ |
| `user['name']`  | `'Doky'`                 |
| `user['age']`   | `5`                      |
| `user['email']` | `'doky@email.com'`       |
| `len(user)`     | `5` (después de agregar) |
| `type(user)`    | `<class 'dict'>`         |

**💻 Código base:**

```python
# User Profile 👤
user = {}  # your code here 💻 (name, age, email, city)
name = ''  # your code here 💻
age = 0  # your code here 💻

# Your code here 💻 (modify age to 6)
# Your code here 💻 (add 'country': 'Peru')

print(f"Usuario: {user['name']}")
print(f"Edad: {user['age']}")
print(f"Perfil completo: {user}")

# Test cases
print(user['name'] == 'Doky')
print(user['age'] == 6)
print(user['email'] == 'doky@email.com')
print(len(user) == 5)
print(type(user) == dict)
```

**💡 Tips:**
- 🔹 Crear: `{'name': 'Doky', 'age': 5, ...}`
- 🔹 Acceder: `user['name']`
- 🔹 Modificar: `user['age'] = 6`
- 🔹 Agregar: `user['country'] = 'Peru'`

**🚀 Motivación:** ¡Doky gestiona perfiles estructurados! 🐕👤

---

### o3.2.2: 📦 Inventario de Productos

**📖 Historia:** Mijael 🧑‍💻 gestiona un inventario de tienda: manzanas:50, peras:30, uvas:20. Necesita agregar productos, actualizar cantidades y calcular el total.

**📝 Descripción:** Tu programa trabaja con un diccionario numérico y realiza operaciones.

**⚙️ Funcionalidades:**
- Crear diccionario de productos y cantidades
- Agregar nuevo producto
- Actualizar cantidad existente
- Calcular total de productos
- Obtener lista de productos

**✅ Casos de prueba:**

| Input                   | Expected Output              |
| ----------------------- | ---------------------------- |
| `inventory['manzanas']` | `50`                         |
| `inventory['peras']`    | `35` (después de actualizar) |
| `total_items`           | `115`                        |
| `len(inventory)`        | `4` (después de agregar)     |
| `type(inventory)`       | `<class 'dict'>`             |

**💻 Código base:**

```python
# Product Inventory 📦
inventory = {}  # your code here 💻 (manzanas:50, peras:30, uvas:20)

# Your code here 💻 (add naranjas:15)
# Your code here 💻 (update peras to 35)

total_items = 0  # your code here 💻 (sum all quantities)
products = []  # your code here 💻 (list of product names)

print(f"Inventario: {inventory}")
print(f"Total items: {total_items}")
print(f"Productos: {products}")

# Test cases
print(inventory['manzanas'] == 50)
print(inventory['peras'] == 35)
print(total_items == 115)
print(len(inventory) == 4)
print(type(inventory) == dict)
```

**💡 Tips:**
- 🔹 Diccionario: `{'manzanas': 50, 'peras': 30, ...}`
- 🔹 Sumar valores: `sum(inventory.values())`
- 🔹 Obtener claves: `list(inventory.keys())`
- 🔹 `.values()` retorna los valores

**🚀 Motivación:** ¡Mijael administra su tienda! 🧑‍💻📦

---

### o3.2.3: 📚 Notas de Estudiantes

**📖 Historia:** Fernanda 🧙‍♀️ registra notas de estudiantes: Elliot:18, Fe:16, Mijael:19. Necesita calcular el promedio, encontrar la nota máxima y contar aprobados (≥14).

**📝 Descripción:** Tu programa procesa un diccionario de notas y genera estadísticas.

**⚙️ Funcionalidades:**
- Crear diccionario de estudiantes y notas
- Calcular promedio de notas
- Encontrar nota máxima y mínima
- Contar aprobados (nota ≥ 14)
- Obtener nombre del mejor estudiante

**✅ Casos de prueba:**

| Input              | Expected Output  |
| ------------------ | ---------------- |
| `grades['Elliot']` | `18`             |
| `average`          | `17.67` (aprox)  |
| `max_grade`        | `19`             |
| `approved_count`   | `3`              |
| `type(grades)`     | `<class 'dict'>` |

**💻 Código base:**

```python
# Student Grades 📚
grades = {}  # your code here 💻 (Elliot:18, Fe:16, Mijael:19)
average = 0  # your code here 💻
max_grade = 0  # your code here 💻
min_grade = 0  # your code here 💻
approved_count = 0  # your code here 💻 (count grades >= 14)
top_student = ''  # your code here 💻 (name with max grade)

print(f"Notas: {grades}")
print(f"Promedio: {average:.2f}")
print(f"Mejor nota: {max_grade} ({top_student})")

# Test cases
print(grades['Elliot'] == 18)
print(17.5 < average < 17.7)
print(max_grade == 19)
print(approved_count == 3)
print(type(grades) == dict)
```

**💡 Tips:**
- 🔹 Promedio: `sum(grades.values()) / len(grades)`
- 🔹 Máximo: `max(grades.values())`
- 🔹 Contar: usa loop `for grade in grades.values()`
- 🔹 Top student: busca con `.items()`

**🚀 Motivación:** ¡Fernanda analiza rendimiento académico! 🧙‍♀️📚

---

### o3.2.4: 🔄 Iterar Diccionario

**📖 Historia:** Elliot ⚡ tiene un diccionario de habilidades: {'fuerza': 85, 'velocidad': 92, 'inteligencia': 78}. Necesita recorrerlo e imprimir cada habilidad formateada.

**📝 Descripción:** Tu programa itera sobre claves, valores y pares clave-valor de un diccionario.

**⚙️ Funcionalidades:**
- Crear diccionario de habilidades
- Iterar solo sobre claves
- Iterar solo sobre valores
- Iterar sobre pares clave-valor
- Generar lista de strings formateados

**✅ Casos de prueba:**

| Input              | Expected Output                           |
| ------------------ | ----------------------------------------- |
| `skills['fuerza']` | `85`                                      |
| `keys_list`        | `['fuerza', 'velocidad', 'inteligencia']` |
| `values_list`      | `[85, 92, 78]`                            |
| `formatted[0]`     | `'fuerza: 85'`                            |
| `type(skills)`     | `<class 'dict'>`                          |

**💻 Código base:**

```python
# Dictionary Iteration 🔄
skills = {}  # your code here 💻 (fuerza:85, velocidad:92, inteligencia:78)
keys_list = []  # your code here 💻 (list of keys)
values_list = []  # your code here 💻 (list of values)
formatted = []  # your code here 💻 (list of 'key: value' strings)

print("Habilidades:")
for item in formatted:
    print(item)

# Test cases
print(skills['fuerza'] == 85)
print(keys_list == ['fuerza', 'velocidad', 'inteligencia'])
print(values_list == [85, 92, 78])
print(formatted[0] == 'fuerza: 85')
print(type(skills) == dict)
```

**💡 Tips:**
- 🔹 Claves: `list(skills.keys())`
- 🔹 Valores: `list(skills.values())`
- 🔹 Pares: `for key, value in skills.items():`
- 🔹 Formatear: `f"{key}: {value}"`

**🚀 Motivación:** ¡Elliot recorre sus poderes! ⚡🔄

---

### o3.2.5: 🏗️ Diccionario Anidado

**📖 Historia:** Fe 👨‍🍳 organiza su restaurante con un diccionario anidado: cada plato tiene nombre, precio e ingredientes (lista). Necesita acceder a datos profundos.

**📝 Descripción:** Tu programa trabaja con diccionarios dentro de diccionarios.

**⚙️ Funcionalidades:**
- Crear diccionario con subdiccionarios
- Acceder a valores anidados
- Modificar valores profundos
- Calcular total de precios
- Contar total de ingredientes

**✅ Casos de prueba:**

| Input                          | Expected Output               |
| ------------------------------ | ----------------------------- |
| `menu['pizza']['price']`       | `25.50`                       |
| `menu['pasta']['ingredients']` | `['pasta', 'salsa', 'queso']` |
| `total_price`                  | `50.50`                       |
| `len(menu)`                    | `2`                           |
| `type(menu)`                   | `<class 'dict'>`              |

**💻 Código base:**

```python
# Nested Dictionary 🏗️
menu = {}  # your code here 💻
# pizza: {name: 'Margarita', price: 25.50, ingredients: ['masa', 'tomate', 'queso']}
# pasta: {name: 'Carbonara', price: 25.00, ingredients: ['pasta', 'salsa', 'queso']}

total_price = 0  # your code here 💻
total_ingredients = 0  # your code here 💻 (count all ingredients from both dishes)
pizza_name = ''  # your code here 💻

print(f"Menú: {list(menu.keys())}")
print(f"Pizza: {pizza_name} - ${menu['pizza']['price']}")
print(f"Total precio: ${total_price}")

# Test cases
print(menu['pizza']['price'] == 25.50)
print(menu['pasta']['ingredients'] == ['pasta', 'salsa', 'queso'])
print(total_price == 50.50)
print(len(menu) == 2)
print(type(menu) == dict)
```

**💡 Tips:**
- 🔹 Anidado: `{'pizza': {'name': '...', 'price': 25.5, ...}}`
- 🔹 Acceso profundo: `menu['pizza']['price']`
- 🔹 Suma precios: recorre el menú
- 🔹 Cuenta ingredientes: `len()` de cada lista

**🚀 Motivación:** ¡Fe estructura su menú profesionalmente! 👨‍🍳🏗️

---

## o3.3: Sets - Conjuntos Únicos

### 🎯 Descripción del Tema

Los sets son colecciones de elementos únicos sin orden específico. Son perfectos para eliminar duplicados, verificar pertenencia rápidamente y realizar operaciones matemáticas de conjuntos: unión, intersección, diferencia.

---

### o3.3.1: 🎯 Elementos Únicos

**📖 Historia:** Chocolate 🐕 tiene una lista con duplicados: [1, 2, 2, 3, 4, 3, 5]. Necesita obtener solo los elementos únicos usando un set.

**📝 Descripción:** Tu programa convierte una lista con duplicados en un set sin duplicados.

**⚙️ Funcionalidades:**
- Crear lista con elementos duplicados
- Convertir lista a set
- Verificar que no hay duplicados
- Convertir set de vuelta a lista ordenada
- Contar elementos únicos

**✅ Casos de prueba:**

| Input              | Expected Output   |
| ------------------ | ----------------- |
| `unique_set`       | `{1, 2, 3, 4, 5}` |
| `len(unique_set)`  | `5`               |
| `3 in unique_set`  | `True`            |
| `sorted_list`      | `[1, 2, 3, 4, 5]` |
| `type(unique_set)` | `<class 'set'>`   |

**💻 Código base:**

```python
# Unique Elements 🎯
numbers = [1, 2, 2, 3, 4, 3, 5]
unique_set = set()  # your code here 💻
count = 0  # your code here 💻
sorted_list = []  # your code here 💻 (convert set back to sorted list)

print(f"Lista original: {numbers}")
print(f"Set único: {unique_set}")
print(f"Lista ordenada: {sorted_list}")

# Test cases
print(unique_set == {1, 2, 3, 4, 5})
print(len(unique_set) == 5)
print(3 in unique_set)
print(sorted_list == [1, 2, 3, 4, 5])
print(type(unique_set) == set)
```

**💡 Tips:**
- 🔹 Convertir: `set(numbers)`
- 🔹 Sets eliminan duplicados automáticamente
- 🔹 A lista ordenada: `sorted(unique_set)`
- 🔹 Contar: `len(unique_set)`

**🚀 Motivación:** ¡Chocolate limpia datos con sets! 🐕🎯

---

### o3.3.2: ➕ Unión de Conjuntos

**📖 Historia:** Amorosa 💖 tiene dos grupos de amigos: {'Ana', 'Luis', 'Pedro'} y {'María', 'Luis', 'Carlos'}. Necesita unir ambos grupos sin duplicados.

**📝 Descripción:** Tu programa usa la operación de unión de sets.

**⚙️ Funcionalidades:**
- Crear dos sets de amigos
- Realizar unión con operador `|` o `.union()`
- Contar total de amigos únicos
- Verificar si alguien está en la unión
- Convertir a lista ordenada

**✅ Casos de prueba:**

| Input                   | Expected Output                               |
| ----------------------- | --------------------------------------------- |
| `all_friends`           | `{'Ana', 'Luis', 'Pedro', 'María', 'Carlos'}` |
| `len(all_friends)`      | `5`                                           |
| `'Luis' in all_friends` | `True`                                        |
| `sorted_friends`        | `['Ana', 'Carlos', 'Luis', 'María', 'Pedro']` |
| `type(all_friends)`     | `<class 'set'>`                               |

**💻 Código base:**

```python
# Set Union ➕
group1 = set()  # your code here 💻 ('Ana', 'Luis', 'Pedro')
group2 = set()  # your code here 💻 ('María', 'Luis', 'Carlos')
all_friends = set()  # your code here 💻 (union of both)
count = 0  # your code here 💻
sorted_friends = []  # your code here 💻

print(f"Grupo 1: {group1}")
print(f"Grupo 2: {group2}")
print(f"Todos los amigos: {all_friends}")
print(f"Total: {count}")

# Test cases
print(len(all_friends) == 5)
print('Luis' in all_friends)
print('Ana' in all_friends)
print(sorted_friends == ['Ana', 'Carlos', 'Luis', 'María', 'Pedro'])
print(type(all_friends) == set)
```

**💡 Tips:**
- 🔹 Crear set: `{'Ana', 'Luis', 'Pedro'}`
- 🔹 Unión: `group1 | group2` o `group1.union(group2)`
- 🔹 La unión no tiene duplicados
- 🔹 Ordenar: `sorted(all_friends)`

**🚀 Motivación:** ¡Amorosa une a todos sus amigos! 💖➕

---

### o3.3.3: 🔍 Intersección de Conjuntos

**📖 Historia:** Doky 🐕 compara dos sets de juguetes: {'pelota', 'hueso', 'cuerda'} y {'pelota', 'disco', 'hueso'}. Necesita encontrar cuáles tiene en común.

**📝 Descripción:** Tu programa usa la operación de intersección de sets.

**⚙️ Funcionalidades:**
- Crear dos sets de juguetes
- Realizar intersección con `&` o `.intersection()`
- Contar elementos en común
- Verificar si hay intersección
- Guardar resultado

**✅ Casos de prueba:**

| Input                     | Expected Output       |
| ------------------------- | --------------------- |
| `common_toys`             | `{'pelota', 'hueso'}` |
| `len(common_toys)`        | `2`                   |
| `'pelota' in common_toys` | `True`                |
| `'disco' in common_toys`  | `False`               |
| `type(common_toys)`       | `<class 'set'>`       |

**💻 Código base:**

```python
# Set Intersection 🔍
toys1 = set()  # your code here 💻 ('pelota', 'hueso', 'cuerda')
toys2 = set()  # your code here 💻 ('pelota', 'disco', 'hueso')
common_toys = set()  # your code here 💻 (intersection)
count = 0  # your code here 💻
has_common = False  # your code here 💻 (True if intersection not empty)

print(f"Juguetes 1: {toys1}")
print(f"Juguetes 2: {toys2}")
print(f"En común: {common_toys}")

# Test cases
print(common_toys == {'pelota', 'hueso'})
print(len(common_toys) == 2)
print('pelota' in common_toys)
print('disco' not in common_toys)
print(type(common_toys) == set)
```

**💡 Tips:**
- 🔹 Intersección: `toys1 & toys2` o `toys1.intersection(toys2)`
- 🔹 Retorna elementos que están en AMBOS sets
- 🔹 Verificar si vacío: `len(common_toys) > 0`
- 🔹 Los sets vacíos son falsy en Python

**🚀 Motivación:** ¡Doky encuentra juguetes favoritos! 🐕🔍

---

### o3.3.4: ➖ Diferencia de Conjuntos

**📖 Historia:** Mijael 🧑‍💻 tiene habilidades actuales: {'Python', 'JavaScript', 'HTML'} y habilidades deseadas: {'Python', 'React', 'Node'}. Necesita saber qué le falta aprender.

**📝 Descripción:** Tu programa usa la operación de diferencia de sets.

**⚙️ Funcionalidades:**
- Crear dos sets de habilidades
- Calcular diferencia (deseadas - actuales)
- Calcular diferencia inversa (actuales - deseadas)
- Contar habilidades faltantes
- Listar lo que debe aprender

**✅ Casos de prueba:**

| Input                  | Expected Output          |
| ---------------------- | ------------------------ |
| `to_learn`             | `{'React', 'Node'}`      |
| `len(to_learn)`        | `2`                      |
| `extra_skills`         | `{'JavaScript', 'HTML'}` |
| `'Python' in to_learn` | `False`                  |
| `type(to_learn)`       | `<class 'set'>`          |

**💻 Código base:**

```python
# Set Difference ➖
current = set()  # your code here 💻 ('Python', 'JavaScript', 'HTML')
desired = set()  # your code here 💻 ('Python', 'React', 'Node')
to_learn = set()  # your code here 💻 (desired - current)
extra_skills = set()  # your code here 💻 (current - desired)
total_to_learn = 0  # your code here 💻

print(f"Actuales: {current}")
print(f"Deseadas: {desired}")
print(f"Debe aprender: {to_learn}")
print(f"Habilidades extra: {extra_skills}")

# Test cases
print(to_learn == {'React', 'Node'})
print(len(to_learn) == 2)
print(extra_skills == {'JavaScript', 'HTML'})
print('Python' not in to_learn)
print(type(to_learn) == set)
```

**💡 Tips:**
- 🔹 Diferencia: `desired - current` o `desired.difference(current)`
- 🔹 Retorna elementos en el primero pero NO en el segundo
- 🔹 La diferencia NO es simétrica: A-B ≠ B-A
- 🔹 Útil para encontrar faltantes

**🚀 Motivación:** ¡Mijael planea su aprendizaje! 🧑‍💻➖

---

### o3.3.5: 🔄 Operaciones Múltiples

**📖 Historia:** Fe 👨‍🍳 tiene 3 sets de ingredientes de diferentes recetas. Necesita: unión de todos, intersección (ingredientes comunes) y diferencia simétrica.

**📝 Descripción:** Tu programa combina múltiples operaciones de sets.

**⚙️ Funcionalidades:**
- Crear 3 sets de ingredientes
- Calcular unión de los 3
- Calcular intersección de todos
- Calcular diferencia simétrica
- Contar resultados

**✅ Casos de prueba:**

| Input                   | Expected Output                                             |
| ----------------------- | ----------------------------------------------------------- |
| `all_ingredients`       | `{'sal', 'pimienta', 'aceite', 'ajo', 'cebolla', 'tomate'}` |
| `len(all_ingredients)`  | `6`                                                         |
| `common_to_all`         | `{'sal'}`                                                   |
| `len(common_to_all)`    | `1`                                                         |
| `type(all_ingredients)` | `<class 'set'>`                                             |

**💻 Código base:**

```python
# Multiple Set Operations 🔄
recipe1 = set()  # your code here 💻 ('sal', 'pimienta', 'aceite')
recipe2 = set()  # your code here 💻 ('sal', 'ajo', 'cebolla')
recipe3 = set()  # your code here 💻 ('sal', 'tomate', 'aceite')
all_ingredients = set()  # your code here 💻 (union of all 3)
common_to_all = set()  # your code here 💻 (intersection of all 3)
unique_to_recipe1 = set()  # your code here 💻 (only in recipe1)

print(f"Todos los ingredientes: {all_ingredients}")
print(f"Común a todas: {common_to_all}")
print(f"Únicos de receta 1: {unique_to_recipe1}")

# Test cases
print(len(all_ingredients) == 6)
print(common_to_all == {'sal'})
print(len(common_to_all) == 1)
print('sal' in all_ingredients)
print(type(all_ingredients) == set)
```

**💡 Tips:**
- 🔹 Unión múltiple: `recipe1 | recipe2 | recipe3`
- 🔹 Intersección múltiple: `recipe1 & recipe2 & recipe3`
- 🔹 Único de 1: `recipe1 - (recipe2 | recipe3)`
- 🔹 Encadena operaciones

**🚀 Motivación:** ¡Fe optimiza sus recetas! 👨‍🍳🔄

---

## o3.4: Funciones - Código Reutilizable

### 🎯 Descripción del Tema

Las funciones son bloques de código reutilizable con nombre. Son fundamentales para organizar código, evitar repetición y crear programas modulares. Aprenderás a definir funciones, pasar parámetros, retornar valores y usar funciones en programas reales.

---

### o3.4.1: 👋 Función Saludar

**📖 Historia:** Elliot ⚡ crea su primera función que saluda a una persona por su nombre. La función debe recibir un nombre y retornar un saludo personalizado.

**📝 Descripción:** Tu programa define una función básica con un parámetro y retorno.

**⚙️ Funcionalidades:**
- Definir función `greet(name)`
- Recibir parámetro name
- Retornar string con saludo
- Llamar función con diferentes nombres
- Guardar resultados

**✅ Casos de prueba:**

| Input               | Expected Output     |
| ------------------- | ------------------- |
| `greet('Elliot')`   | `'Hola, Elliot!'`   |
| `greet('Fernanda')` | `'Hola, Fernanda!'` |
| `greet('Fe')`       | `'Hola, Fe!'`       |
| `result1`           | `'Hola, Elliot!'`   |
| `type(result1)`     | `<class 'str'>`     |

**💻 Código base:**

```python
# Greeting Function 👋

# Your code here 💻 (define greet function)

result1 = ''  # your code here 💻 (call greet with 'Elliot')
result2 = ''  # your code here 💻 (call greet with 'Fernanda')
result3 = ''  # your code here 💻 (call greet with 'Fe')

print(result1)
print(result2)
print(result3)

# Test cases
print(result1 == 'Hola, Elliot!')
print(result2 == 'Hola, Fernanda!')
print(result3 == 'Hola, Fe!')
print(type(result1) == str)
```

**💡 Tips:**
- 🔹 Definir: `def greet(name):`
- 🔹 Retornar: `return f"Hola, {name}!"`
- 🔹 Llamar: `greet('Elliot')`
- 🔹 Indentación es crucial

**🚀 Motivación:** ¡Elliot crea su primera función! ⚡👋

---

### o3.4.2: ➕ Función Calculadora

**📖 Historia:** Fernanda 🧙‍♀️ necesita una función `calculate(a, b, operation)` que recibe dos números y una operación ('suma', 'resta', 'multiplicación', 'división') y retorna el resultado.

**📝 Descripción:** Tu programa define una función con múltiples parámetros y lógica condicional.

**⚙️ Funcionalidades:**
- Definir función con 3 parámetros
- Implementar 4 operaciones
- Usar condicionales dentro de función
- Retornar resultado correcto
- Manejar división por cero

**✅ Casos de prueba:**

| Input                                | Expected Output |
| ------------------------------------ | --------------- |
| `calculate(10, 5, 'suma')`           | `15`            |
| `calculate(10, 5, 'resta')`          | `5`             |
| `calculate(10, 5, 'multiplicación')` | `50`            |
| `calculate(10, 5, 'división')`       | `2.0`           |
| `type(result1)`                      | `<class 'int'>` |

**💻 Código base:**

```python
# Calculator Function ➕

# Your code here 💻 (define calculate function)

result1 = 0  # your code here 💻 (10 + 5)
result2 = 0  # your code here 💻 (10 - 5)
result3 = 0  # your code here 💻 (10 * 5)
result4 = 0  # your code here 💻 (10 / 5)

print(f"10 + 5 = {result1}")
print(f"10 - 5 = {result2}")
print(f"10 * 5 = {result3}")
print(f"10 / 5 = {result4}")

# Test cases
print(result1 == 15)
print(result2 == 5)
print(result3 == 50)
print(result4 == 2.0)
print(type(result1) == int)
```

**💡 Tips:**
- 🔹 Definir: `def calculate(a, b, operation):`
- 🔹 Usa `if operation == 'suma':`
- 🔹 Retorna resultado según operación
- 🔹 División retorna float

**🚀 Motivación:** ¡Fernanda automatiza cálculos! 🧙‍♀️➕

---

### o3.4.3: 📊 Función de Estadísticas

**📖 Historia:** Chocolate 🐕 necesita una función `get_stats(numbers)` que recibe una lista de números y retorna una tupla con (mínimo, máximo, promedio, suma).

**📝 Descripción:** Tu programa define una función que retorna múltiples valores.

**⚙️ Funcionalidades:**
- Definir función que recibe lista
- Calcular mínimo, máximo, promedio, suma
- Retornar tupla con 4 valores
- Desempaquetar resultado
- Validar todos los cálculos

**✅ Casos de prueba:**

| Input                    | Expected Output   |
| ------------------------ | ----------------- |
| `get_stats([1,2,3,4,5])` | `(1, 5, 3.0, 15)` |
| `min_val`                | `1`               |
| `max_val`                | `5`               |
| `avg_val`                | `3.0`             |
| `type(stats)`            | `<class 'tuple'>` |

**💻 Código base:**

```python
# Statistics Function 📊

# Your code here 💻 (define get_stats function)

numbers = [1, 2, 3, 4, 5]
stats = ()  # your code here 💻 (call get_stats)
min_val = 0  # your code here 💻 (unpack from stats)
max_val = 0  # your code here 💻
avg_val = 0  # your code here 💻
sum_val = 0  # your code here 💻

print(f"Números: {numbers}")
print(f"Mínimo: {min_val}")
print(f"Máximo: {max_val}")
print(f"Promedio: {avg_val}")
print(f"Suma: {sum_val}")

# Test cases
print(stats == (1, 5, 3.0, 15))
print(min_val == 1)
print(max_val == 5)
print(avg_val == 3.0)
print(type(stats) == tuple)
```

**💡 Tips:**
- 🔹 Definir: `def get_stats(numbers):`
- 🔹 Calcular: `min()`, `max()`, `sum()`, `sum()/len()`
- 🔹 Retornar tupla: `return (min_val, max_val, avg, total)`
- 🔹 Desempaquetar: `min_val, max_val, avg_val, sum_val = get_stats(numbers)`

**🚀 Motivación:** ¡Chocolate procesa datos estadísticos! 🐕📊

---

### o3.4.4: 🔄 Función con Valor por Defecto

**📖 Historia:** Amorosa 💖 crea una función `create_profile(name, age, city='Lima')` donde city es opcional y por defecto es 'Lima'. Retorna un diccionario.

**📝 Descripción:** Tu programa define una función con parámetros por defecto.

**⚙️ Funcionalidades:**
- Definir función con parámetro por defecto
- Retornar diccionario
- Llamar con todos los parámetros
- Llamar sin el parámetro opcional
- Validar ambos casos

**✅ Casos de prueba:**

| Input                                 | Expected Output                             |
| ------------------------------------- | ------------------------------------------- |
| `create_profile('Ana', 25)`           | `{'name':'Ana', 'age':25, 'city':'Lima'}`   |
| `create_profile('Luis', 30, 'Cusco')` | `{'name':'Luis', 'age':30, 'city':'Cusco'}` |
| `profile1['city']`                    | `'Lima'`                                    |
| `profile2['city']`                    | `'Cusco'`                                   |
| `type(profile1)`                      | `<class 'dict'>`                            |

**💻 Código base:**

```python
# Profile Function with Default 🔄

# Your code here 💻 (define create_profile function)

profile1 = {}  # your code here 💻 (call with 'Ana', 25)
profile2 = {}  # your code here 💻 (call with 'Luis', 30, 'Cusco')

print(f"Perfil 1: {profile1}")
print(f"Perfil 2: {profile2}")

# Test cases
print(profile1 == {'name': 'Ana', 'age': 25, 'city': 'Lima'})
print(profile2 == {'name': 'Luis', 'age': 30, 'city': 'Cusco'})
print(profile1['city'] == 'Lima')
print(profile2['city'] == 'Cusco')
print(type(profile1) == dict)
```

**💡 Tips:**
- 🔹 Definir: `def create_profile(name, age, city='Lima'):`
- 🔹 Retornar: `return {'name': name, 'age': age, 'city': city}`
- 🔹 Parámetro por defecto al final
- 🔹 Se usa si no se proporciona

**🚀 Motivación:** ¡Amorosa crea perfiles flexibles! 💖🔄

---

### o3.4.5: 🎯 Función Compleja

**📖 Historia:** Doky 🐕 necesita una función `process_list(items, operation='count')` que recibe una lista y una operación ('count', 'sum', 'average', 'unique') y retorna el resultado correspondiente.

**📝 Descripción:** Tu programa define una función compleja que combina todo lo aprendido.

**⚙️ Funcionalidades:**
- Definir función con parámetro por defecto
- Implementar 4 operaciones diferentes
- Manejar diferentes tipos de retorno
- Usar lógica condicional compleja
- Validar todas las operaciones

**✅ Casos de prueba:**

| Input                                  | Expected Output |
| -------------------------------------- | --------------- |
| `process_list([1,2,3,4,5], 'count')`   | `5`             |
| `process_list([1,2,3,4,5], 'sum')`     | `15`            |
| `process_list([1,2,3,4,5], 'average')` | `3.0`           |
| `process_list([1,2,2,3], 'unique')`    | `[1,2,3]`       |
| `type(result1)`                        | `<class 'int'>` |

**💻 Código base:**

```python
# Complex List Processor 🎯

# Your code here 💻 (define process_list function)

numbers = [1, 2, 3, 4, 5]
result1 = 0  # your code here 💻 (count)
result2 = 0  # your code here 💻 (sum)
result3 = 0  # your code here 💻 (average)
result4 = []  # your code here 💻 (unique from [1,2,2,3])

print(f"Count: {result1}")
print(f"Sum: {result2}")
print(f"Average: {result3}")
print(f"Unique: {result4}")

# Test cases
print(result1 == 5)
print(result2 == 15)
print(result3 == 3.0)
print(result4 == [1, 2, 3])
print(type(result1) == int)
```

**💡 Tips:**
- 🔹 Definir: `def process_list(items, operation='count'):`
- 🔹 Usa múltiples `if-elif`
- 🔹 Unique: convierte a set y luego a lista
- 🔹 Retorna tipos diferentes según operación

**🚀 Motivación:** ¡Doky crea funciones profesionales! 🐕🎯

---

## 🎉 ¡Felicidades! Has completado el Nivel 3

### 📊 Resumen de Logros

**✅ Has dominado:**
- 📦 **Tuplas**: Secuencias inmutables, desempaquetado, intercambio de valores
- 📚 **Diccionarios**: Pares clave-valor, iteración, diccionarios anidados
- 🎯 **Sets**: Elementos únicos, unión, intersección, diferencia
- ⚡ **Funciones**: Definición, parámetros, retornos, valores por defecto

**⏰ Tiempo completado:** 8 horas de práctica intensiva

**🎓 Habilidades adquiridas:**
- Organización de datos con estructuras adecuadas
- Operaciones avanzadas con conjuntos
- Código modular y reutilizable con funciones
- Manejo de datos complejos y anidados

**🔜 Próximo nivel:** Nivel 4 - Módulos, Archivos y Proyectos

---

💪 **¡Excelente trabajo!** Fernanda, Elliot, Fe, Mijael, Chocolate, Doky y Amorosa están orgullosos de ti. ¡Eres un verdadero programador avanzado! 🏆✨🚀
