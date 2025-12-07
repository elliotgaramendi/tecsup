# 🐍 Examen Python Nivel 2 - Fundamentos Intermedios 🐍

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
    ║           🐍 PYTHON FUNDAMENTALS EXAM 🐍                    ║
    ║                                                            ║
    ║         ✨ Demuestra todo lo que has aprendido ✨           ║
    ║                                                            ║
    ║      🚀 ¡TÚ PUEDES LOGRARLO, PROGRAMADOR! 🚀                ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
```

---

## 📋 Instrucciones Generales

¡Bienvenido al examen de Python Nivel 2, futuro desarrollador! 🐍✨ Este examen valida que has comprendido los fundamentos intermedios de programación. Cada reto es una oportunidad para demostrar tus nuevas habilidades.

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

## 🎯 Tema 1: Condicionales II - Lógica Avanzada

### o1.1: 🎟️ Control de Entrada a Concierto

**📖 Historia:** Fernanda 🧙‍♀️ gestiona la entrada a un concierto. Las reglas son: edad entre 16-60 años Y tener boleto válido. Mijael tiene 22 años y boleto válido. ¿Puede entrar?

**📝 Descripción:** Tu programa debe validar edad en rango Y posesión de boleto usando operador `and`.

**⚙️ Funcionalidades:**
- Crear variables de edad y boleto
- Validar edad entre 16 y 60 años
- Verificar boleto válido (booleano)
- Combinar condiciones con `and`
- Asignar resultado a variable `can_enter`

**✅ Casos de prueba:**

| Input                      | Expected Output   |
| -------------------------- | ----------------- |
| `age=22, has_ticket=True`  | `can_enter=True`  |
| `age=22, has_ticket=False` | `can_enter=False` |
| `age=15, has_ticket=True`  | `can_enter=False` |
| `age=65, has_ticket=True`  | `can_enter=False` |
| `type(can_enter)`          | `<class 'bool'>`  |

**💻 Código base:**

```python
# Concert Entry Control 🎟️
age = 22
has_ticket = True
can_enter = None  # your code here 💻

print(f"Edad: {age}, Boleto: {has_ticket}")
print(f"Entrada: {'Permitida ✅' if can_enter else 'Denegada ❌'}")

# Test cases
print(can_enter == True)
print(type(can_enter) == bool)
```

**💡 Tips:**
- 🔹 Valida rango: `16 <= age <= 60`
- 🔹 Usa `and` para combinar: `(condicion1) and (condicion2)`
- 🔹 Ambas deben ser True para entrar

**🚀 Motivación:** ¡Validas acceso con lógica compleja! 🎟️✨

---

### o1.2: 💎 Clasificador de Miembros VIP

**📖 Historia:** Elliot ⚡ clasifica miembros de un club. Un miembro es VIP si gasta más de $500 O tiene más de 5 años de antigüedad. Fe gastó $400 pero tiene 7 años. ¿Es VIP?

**📝 Descripción:** Tu programa usa operador `or` para clasificar miembros VIP.

**⚙️ Funcionalidades:**
- Crear variables de gasto y años
- Validar gasto mayor a $500
- Validar años mayor a 5
- Usar `or` para clasificar
- Asignar resultado a `is_vip`

**✅ Casos de prueba:**

| Input                | Expected Output  |
| -------------------- | ---------------- |
| `spent=400, years=7` | `is_vip=True`    |
| `spent=600, years=2` | `is_vip=True`    |
| `spent=300, years=3` | `is_vip=False`   |
| `spent=500, years=5` | `is_vip=False`   |
| `type(is_vip)`       | `<class 'bool'>` |

**💻 Código base:**

```python
# VIP Member Classifier 💎
spent = 400
years = 7
is_vip = None  # your code here 💻

print(f"Gasto: ${spent}, Años: {years}")
print(f"VIP: {'Sí 💎' if is_vip else 'No'}")

# Test cases
print(is_vip == True)
print(type(is_vip) == bool)
```

**💡 Tips:**
- 🔹 Usa `or`: `(spent > 500) or (years > 5)`
- 🔹 Con `or` solo UNA necesita ser True
- 🔹 Note que 500 y 5 NO califican (mayor, no igual)

**🚀 Motivación:** ¡Fe es VIP por su lealtad! 💎✨

---

### o1.3: 🌡️ Monitor de Clima Extremo

**📖 Historia:** Chocolate 🐕 monitorea el clima. Hay alerta si temperatura >35°C O lluvia >50mm O viento >60km/h. Hoy: 32°C, 55mm lluvia, 40km/h viento. ¿Hay alerta?

**📝 Descripción:** Tu programa usa múltiples `or` para detectar clima extremo.

**⚙️ Funcionalidades:**
- Crear variables de temperatura, lluvia, viento
- Validar cada condición de peligro
- Usar `or` múltiple
- Contar cuántas alertas hay
- Asignar resultado a `has_alert`

**✅ Casos de prueba:**

| Input                       | Expected Output   |
| --------------------------- | ----------------- |
| `temp=32, rain=55, wind=40` | `has_alert=True`  |
| `temp=36, rain=30, wind=50` | `has_alert=True`  |
| `temp=25, rain=40, wind=50` | `has_alert=False` |
| `temp=38, rain=60, wind=70` | `has_alert=True`  |
| `type(has_alert)`           | `<class 'bool'>`  |

**💻 Código base:**

```python
# Extreme Weather Monitor 🌡️
temp = 32
rain = 55
wind = 40
has_alert = None  # your code here 💻
alert_count = 0  # your code here 💻 (count how many conditions are true)

print(f"Temp: {temp}°C, Lluvia: {rain}mm, Viento: {wind}km/h")
print(f"Alerta: {'SÍ 🌡️' if has_alert else 'NO ✅'}")
print(f"Alertas activas: {alert_count}")

# Test cases
print(has_alert == True)
print(alert_count == 1)
print(type(has_alert) == bool)
```

**💡 Tips:**
- 🔹 Combina: `(temp > 35) or (rain > 50) or (wind > 60)`
- 🔹 Cuenta convirtiendo booleanos: `int(temp > 35) + ...`
- 🔹 Con `or`, cualquiera True da True

**🚀 Motivación:** ¡Chocolate detecta clima peligroso! 🐕🌡️

---

## 🔄 Tema 2: Bucles II - Control de Flujo

### o2.1: 🔎 Buscador de Palabra

**📖 Historia:** Amorosa 💖 busca la palabra 'amor' en una lista de 15 palabras. Cuando la encuentra debe detenerse y reportar la posición. La palabra está en posición 8.

**📝 Descripción:** Tu programa recorre una lista hasta encontrar la palabra, usando `break` para detenerse.

**⚙️ Funcionalidades:**
- Crear lista de 15 palabras
- Buscar palabra específica
- Usar `break` al encontrarla
- Contar iteraciones
- Guardar posición encontrada

**✅ Casos de prueba:**

| Input                  | Expected Output            |
| ---------------------- | -------------------------- |
| `target='amor'`        | `found=True, position=7`   |
| `iterations`           | `8`                        |
| `target='paz'` (pos 3) | `found=True, iterations=4` |
| `target='inexistente'` | `found=False`              |
| `type(found)`          | `<class 'bool'>`           |

**💻 Código base:**

```python
# Word Finder 🔎
words = ['sol', 'luna', 'estrella', 'paz', 'cielo', 'mar', 'nube', 'amor',
         'flor', 'rio', 'monte', 'valle', 'isla', 'lago', 'bosque']
target = 'amor'
found = False  # your code here 💻
position = -1  # your code here 💻
iterations = 0  # your code here 💻

print(f"Buscando: '{target}'")
print(f"Encontrado: {found} en posición {position}")
print(f"Iteraciones: {iterations}")

# Test cases
print(found == True)
print(position == 7)
print(iterations == 8)
print(type(found) == bool)
```

**💡 Tips:**
- 🔹 Usa `for i, word in enumerate(words):`
- 🔹 Incrementa `iterations` cada vuelta
- 🔹 `if word == target: break`
- 🔹 Guarda `position = i` antes del break

**🚀 Motivación:** ¡Amorosa encuentra palabras eficientemente! 💖🔎

---

### o2.2: 🎯 Contador Selectivo

**📖 Historia:** Doky 🐕 cuenta números del 1 al 25, pero debe SALTAR los múltiplos de 7 (7, 14, 21). Los múltiplos de 7 no se cuentan.

**📝 Descripción:** Tu programa usa `continue` para saltar números específicos sin procesarlos.

**⚙️ Funcionalidades:**
- Recorrer del 1 al 25
- Identificar múltiplos de 7
- Usar `continue` para saltarlos
- Contar números procesados
- Crear lista con números contados

**✅ Casos de prueba:**

| Input           | Expected Output |
| --------------- | --------------- |
| `range(1, 26)`  | `count=22`      |
| `7 in numbers`  | `False`         |
| `14 in numbers` | `False`         |
| `21 in numbers` | `False`         |
| `type(count)`   | `<class 'int'>` |

**💻 Código base:**

```python
# Selective Counter 🎯
count = 0  # your code here 💻
numbers = []  # your code here 💻

# Your loop here 💻
# for i in range(1, 26):

print(f"Números contados: {count}")
print(f"Múltiplos de 7 omitidos: {25 - count}")

# Test cases
print(count == 22)
print(7 not in numbers)
print(14 not in numbers)
print(21 not in numbers)
print(type(count) == int)
```

**💡 Tips:**
- 🔹 `if i % 7 == 0: continue`
- 🔹 Después del continue, cuenta y agrega
- 🔹 `continue` salta sin salir del bucle
- 🔹 25 total - 3 múltiplos de 7 = 22

**🚀 Motivación:** ¡Doky filtra números como experto! 🐕🎯

---

### o2.3: 🔺 Cuadrado de Números

**📖 Historia:** Mijael 🧑‍💻 dibuja un cuadrado de 4x4 con números. Cada posición muestra fila*columna. Necesita bucles anidados para crear la matriz.

**📝 Descripción:** Tu programa usa bucles anidados para generar un patrón bidimensional.

**⚙️ Funcionalidades:**
- Bucle externo para 4 filas
- Bucle interno para 4 columnas
- Calcular fila * columna en cada posición
- Contar total de números generados
- Sumar todos los productos

**✅ Casos de prueba:**

| Input           | Expected Output |
| --------------- | --------------- |
| `size=4`        | `total_nums=16` |
| `sum_all`       | `100`           |
| `first_row_sum` | `10` (1+2+3+4)  |
| `last_value`    | `16` (4*4)      |
| `type(sum_all)` | `<class 'int'>` |

**💻 Código base:**

```python
# Number Square 🔺
size = 4
total_nums = 0  # your code here 💻
sum_all = 0  # your code here 💻
first_row_sum = 0  # your code here 💻
last_value = 0  # your code here 💻

# Your nested loop here 💻
# for row in range(1, size + 1):
#     for col in range(1, size + 1):

print(f"Total números: {total_nums}")
print(f"Suma total: {sum_all}")
print(f"Primera fila suma: {first_row_sum}")

# Test cases
print(total_nums == 16)
print(sum_all == 100)
print(first_row_sum == 10)
print(last_value == 16)
print(type(sum_all) == int)
```

**💡 Tips:**
- 🔹 Externo: `for row in range(1, 5):`
- 🔹 Interno: `for col in range(1, 5):`
- 🔹 Calcula: `value = row * col`
- 🔹 Suma primera fila con `if row == 1:`

**🚀 Motivación:** ¡Mijael crea matrices matemáticas! 🧑‍💻🔺

---

## ⚡ Tema 3: Bucles III - Iteración Avanzada

### o3.1: 📋 Inventario con Índices

**📖 Historia:** Fe 👨‍🍳 tiene 6 productos: ['pan', 'leche', 'huevos', 'queso', 'mantequilla', 'yogur']. Necesita mostrar cada uno con su número de posición usando `enumerate()`.

**📝 Descripción:** Tu programa usa `enumerate()` para obtener índice y valor simultáneamente.

**⚙️ Funcionalidades:**
- Crear lista de 6 productos
- Usar `enumerate()` en bucle
- Formatear como "posición: producto"
- Guardar en lista de salida
- Validar todas las posiciones

**✅ Casos de prueba:**

| Input          | Expected Output  |
| -------------- | ---------------- |
| `products[0]`  | `'pan'`          |
| `output[0]`    | `'0: pan'`       |
| `output[3]`    | `'3: queso'`     |
| `len(output)`  | `6`              |
| `type(output)` | `<class 'list'>` |

**💻 Código base:**

```python
# Inventory with Indices 📋
products = ['pan', 'leche', 'huevos', 'queso', 'mantequilla', 'yogur']
output = []  # your code here 💻

# Your loop here 💻
# for index, product in enumerate(products):

print("Inventario:")
for line in output:
    print(line)

# Test cases
print(output[0] == '0: pan')
print(output[3] == '3: queso')
print(len(output) == 6)
print(type(output) == list)
```

**💡 Tips:**
- 🔹 `for i, item in enumerate(lista):`
- 🔹 `i` es índice (inicia en 0)
- 🔹 Formatea: `f"{i}: {item}"`
- 🔹 Usa `.append()` para guardar

**🚀 Motivación:** ¡Fe organiza su inventario! 👨‍🍳📋

---

### o3.2: 🔢 Contador de 3 en 3

**📖 Historia:** Elliot ⚡ cuenta del 0 al 24 pero solo los múltiplos de 3 (0, 3, 6, 9...). Usa `range()` con step de 3.

**📝 Descripción:** Tu programa usa `range()` con step para generar secuencias específicas.

**⚙️ Funcionalidades:**
- Usar `range(start, stop, step)`
- Generar múltiplos de 3 del 0 al 24
- Sumar los números
- Contar cuántos hay
- Crear lista con valores

**✅ Casos de prueba:**

| Input             | Expected Output            |
| ----------------- | -------------------------- |
| `range(0, 25, 3)` | `multiples=[0,3,6,...,24]` |
| `total`           | `108`                      |
| `count`           | `9`                        |
| `multiples[4]`    | `12`                       |
| `type(multiples)` | `<class 'list'>`           |

**💻 Código base:**

```python
# Counter by 3 🔢
multiples = []  # your code here 💻
total = 0  # your code here 💻
count = 0  # your code here 💻

# Your loop here 💻
# for i in range(0, 25, 3):

print(f"Múltiplos de 3: {multiples}")
print(f"Suma: {total}")
print(f"Cantidad: {count}")

# Test cases
print(len(multiples) == 9)
print(total == 108)
print(count == 9)
print(multiples[4] == 12)
print(type(multiples) == list)
```

**💡 Tips:**
- 🔹 `range(0, 25, 3)` genera: 0, 3, 6, 9, 12, 15, 18, 21, 24
- 🔹 Tercer parámetro es el paso
- 🔹 Acumula suma con `+=`
- 🔹 Cuenta con `count += 1` o usa `len()`

**🚀 Motivación:** ¡Elliot domina rangos personalizados! ⚡🔢

---

### o3.3: 🔍 Búsqueda con For-Else

**📖 Historia:** Fernanda 🧙‍♀️ busca 'magia' en una lista de 5 habilidades: ['fuerza', 'velocidad', 'inteligencia', 'agilidad', 'resistencia']. Si NO lo encuentra, el `else` del `for` se ejecuta.

**📝 Descripción:** Tu programa usa el `else` especial de Python en bucles `for`.

**⚙️ Funcionalidades:**
- Crear lista de habilidades sin 'magia'
- Buscar 'magia' en la lista
- Usar `break` si encuentra
- Usar `else` si no encuentra
- Reportar resultado

**✅ Casos de prueba:**

| Input                                 | Expected Output  |
| ------------------------------------- | ---------------- |
| `search='magia'`                      | `found=False`    |
| `else_executed`                       | `True`           |
| `search='fuerza'`                     | `found=True`     |
| `abilities=['magia'], search='magia'` | `found=True`     |
| `type(found)`                         | `<class 'bool'>` |

**💻 Código base:**

```python
# For-Else Search 🔍
abilities = ['fuerza', 'velocidad', 'inteligencia', 'agilidad', 'resistencia']
search = 'magia'
found = False  # your code here 💻
else_executed = False  # your code here 💻

# Your loop here 💻

print(f"Buscando: {search}")
print(f"Encontrado: {found}")
print(f"Else ejecutado: {else_executed}")

# Test cases
print(found == False)
print(else_executed == True)
print(type(found) == bool)
```

**💡 Tips:**
- 🔹 Estructura: `for ... else:`
- 🔹 `else` se ejecuta si NO hay `break`
- 🔹 Perfecto para "no encontrado"
- 🔹 Característica única de Python

**🚀 Motivación:** ¡Fernanda usa for-else! 🧙‍♀️🔍

---

## 📊 Tema 4: Listas - Colecciones Dinámicas

### o4.1: ➕ Constructor de Tareas

**📖 Historia:** Chocolate 🐕 crea una lista de tareas vacía y agrega 4 tareas: 'estudiar', 'cocinar', 'ejercicio', 'leer'. Usa `.append()` para cada una.

**📝 Descripción:** Tu programa construye una lista dinámicamente con `.append()`.

**⚙️ Funcionalidades:**
- Iniciar lista vacía
- Agregar 4 tareas con `.append()`
- Obtener primera y última tarea
- Contar total
- Verificar tipo

**✅ Casos de prueba:**

| Input                | Expected Output  |
| -------------------- | ---------------- |
| `tasks[0]`           | `'estudiar'`     |
| `tasks[-1]`          | `'leer'`         |
| `len(tasks)`         | `4`              |
| `'cocinar' in tasks` | `True`           |
| `type(tasks)`        | `<class 'list'>` |

**💻 Código base:**

```python
# Task Builder ➕
tasks = []  # your code here 💻
first = ''  # your code here 💻
last = ''  # your code here 💻
total = 0  # your code here 💻

print(f"Tareas: {tasks}")
print(f"Primera: {first}")
print(f"Última: {last}")
print(f"Total: {total}")

# Test cases
print(first == 'estudiar')
print(last == 'leer')
print(total == 4)
print('cocinar' in tasks)
print(type(tasks) == list)
```

**💡 Tips:**
- 🔹 `.append(elemento)` agrega al final
- 🔹 `tasks[0]` primera tarea
- 🔹 `tasks[-1]` última tarea
- 🔹 `len(tasks)` cuenta elementos

**🚀 Motivación:** ¡Chocolate organiza su día! 🐕➕

---

### o4.2: ✂️ Extractor de Secciones

**📖 Historia:** Amorosa 💖 tiene una lista de 8 números: [10, 20, 30, 40, 50, 60, 70, 80]. Necesita extraer: primeros 3, últimos 2, y del medio (índices 2 al 5).

**📝 Descripción:** Tu programa usa slicing para extraer partes de listas.

**⚙️ Funcionalidades:**
- Crear lista de 8 números
- Extraer primeros 3
- Extraer últimos 2
- Extraer del medio (índice 2 al 5)
- Validar longitudes

**✅ Casos de prueba:**

| Input           | Expected Output    |
| --------------- | ------------------ |
| `first_3`       | `[10, 20, 30]`     |
| `last_2`        | `[70, 80]`         |
| `middle`        | `[30, 40, 50, 60]` |
| `len(middle)`   | `4`                |
| `type(first_3)` | `<class 'list'>`   |

**💻 Código base:**

```python
# Section Extractor ✂️
numbers = []  # your code here 💻
first_3 = []  # your code here 💻
last_2 = []  # your code here 💻
middle = []  # your code here 💻

print(f"Primeros 3: {first_3}")
print(f"Últimos 2: {last_2}")
print(f"Medio (2-5): {middle}")

# Test cases
print(first_3 == [10, 20, 30])
print(last_2 == [70, 80])
print(middle == [30, 40, 50, 60])
print(len(middle) == 4)
print(type(first_3) == list)
```

**💡 Tips:**
- 🔹 `numbers = [10, 20, 30, 40, 50, 60, 70, 80]`
- 🔹 `lista[0:3]` primeros 3
- 🔹 `lista[-2:]` últimos 2
- 🔹 `lista[2:6]` índices 2,3,4,5

**🚀 Motivación:** ¡Amorosa corta listas con precisión! 💖✂️

---

### o4.3: 🧹 Limpiador de Repetidos

**📖 Historia:** Doky 🐕 tiene una lista con duplicados: [5, 10, 5, 20, 10, 30, 5]. Necesita crear una lista nueva con solo valores únicos, manteniendo el orden original.

**📝 Descripción:** Tu programa elimina duplicados usando un bucle y verificación.

**⚙️ Funcionalidades:**
- Crear lista con duplicados
- Recorrer y verificar con `not in`
- Crear lista única
- Mantener orden original
- Contar elementos únicos

**✅ Casos de prueba:**

| Input          | Expected Output       |
| -------------- | --------------------- |
| `original`     | `[5,10,5,20,10,30,5]` |
| `unique`       | `[5, 10, 20, 30]`     |
| `len(unique)`  | `4`                   |
| `unique[0]`    | `5`                   |
| `type(unique)` | `<class 'list'>`      |

**💻 Código base:**

```python
# Duplicate Cleaner 🧹
original = []  # your code here 💻
unique = []  # your code here 💻

# Your loop here 💻

print(f"Original: {original}")
print(f"Sin duplicados: {unique}")
print(f"Únicos: {len(unique)}")

# Test cases
print(len(original) == 7)
print(unique == [5, 10, 20, 30])
print(len(unique) == 4)
print(unique[0] == 5)
print(type(unique) == list)
```

**💡 Tips:**
- 🔹 `original = [5, 10, 5, 20, 10, 30, 5]`
- 🔹 `if item not in unique:` verifica
- 🔹 `.append()` solo si no existe
- 🔹 Mantiene orden de primera aparición

**🚀 Motivación:** ¡Doky limpia datos como pro! 🐕🧹

---

## 🏆 ¡FELICIDADES PROGRAMADOR! 🎊

```
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║          🌟 ¡COMPLETASTE EL EXAMEN NIVEL 2! 🌟           ║
    ║                                                          ║
    ║              ∩＿＿＿∩                                     ║
    ║             /  ^   ^  \                                  ║
    ║            /  ●   ●   \                                  ║
    ║           |     ▼      |                                 ║
    ║           |   \___/    |    ¡EXCELENTE!                  ║
    ║            \__________/                                  ║
    ║                                                          ║
    ║    ✨ Has demostrado dominio de los fundamentos          ║
    ║       intermedios de Python. ¡Sigue adelante! ✨         ║
    ║                                                          ║
    ║         La programación es tu superpoder 🚀              ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
```

---

## 📚 Resumen del Examen

### ✅ Conceptos Evaluados

**🎯 Tema 1: Condicionales II**
- ✅ Operador `and` para condiciones múltiples
- ✅ Operador `or` para alternativas
- ✅ Combinación de condiciones complejas
- ✅ Conteo de condiciones verdaderas

**🔄 Tema 2: Bucles II**
- ✅ Uso de `break` para detener búsquedas
- ✅ Uso de `continue` para saltar iteraciones
- ✅ Bucles anidados para estructuras 2D
- ✅ Conteo y acumulación en bucles

**⚡ Tema 3: Bucles III**
- ✅ `enumerate()` para índice + valor
- ✅ `range()` con step personalizado
- ✅ Bucle `for-else` para búsquedas
- ✅ Iteración avanzada y eficiente

**📊 Tema 4: Listas**
- ✅ Construcción dinámica con `.append()`
- ✅ Slicing para extraer secciones
- ✅ Eliminación de duplicados
- ✅ Manipulación y validación de listas

---

## 🎓 Próximos Pasos

### 📖 Si aprobaste el examen:
- 🎉 ¡Felicidades! Dominas los fundamentos intermedios
- 🚀 Estás listo para **Nivel 3: Tuplas, Diccionarios y Sets**
- 💪 Sigue practicando estos conceptos
- 🔄 Revisa los retos que te costaron más

### 📝 Si necesitas reforzar:
- 🔍 Identifica los temas donde tuviste dificultad
- 📚 Repasa la guía de Nivel 2
- 💻 Practica los ejercicios de los temas débiles
- 🎯 Vuelve a intentar el examen cuando te sientas listo

---

## ✨ Mensaje de Motivación

> **"Cada línea de código que escribes te acerca más a convertirte en el programador que quieres ser."**
>
> 🐍 Has demostrado tu comprensión de Python intermedio
>
> 💪 Condicionales complejas, bucles avanzados y listas ya no tienen secretos para ti
>
> 🌟 Cada reto resuelto es un paso más en tu camino
>
> 🚀 El mundo del código te espera. ¡Continúa conquistándolo!

---

## 🎯 Consejos Finales

### Para mejorar continuamente:
1. **Practica diariamente** 📅 - Aunque sea 15 minutos al día
2. **Crea tus propios retos** 🎨 - Modifica los ejercicios con tus ideas
3. **Comparte tu código** 🤝 - Aprende de otros programadores
4. **Lee código de otros** 👀 - Hay múltiples formas de resolver problemas
5. **No te rindas** 💪 - La programación requiere persistencia

### Recursos recomendados:
- 🔄 Repasa la guía de Nivel 2 cuando necesites
- 📊 Practica con el archivo de soluciones
- 💡 Experimenta modificando los ejercicios
- 🎮 Crea pequeños proyectos personales
- 🌐 Explora documentación de Python oficial

---

## 🐍 ¡BIENVENIDO AL SIGUIENTE NIVEL! 🐍

**Has superado un hito importante en tu camino como programador Python.**

✨ Condicionales avanzadas ✅  
✨ Control de flujo experto ✅  
✨ Iteración sofisticada ✅  
✨ Manipulación de listas ✅  

**¡GRACIAS POR TU DEDICACIÓN Y ESFUERZO!** 💚🇵🇪

### 🎊 Tus amigos te felicitan:
- Fernanda 🧙‍♀️: "¡Usas la lógica como un mago!"
- Elliot ⚡: "¡Tus bucles son veloces como rayos!"
- Fe 👨‍🍳: "¡Cocinas código delicioso!"
- Mijael 🧑‍💻: "¡Eres un arquitecto del código!"
- Chocolate 🐕: "¡Guau! ¡Eres increíble!"
- Doky 🐕: "¡Woof! ¡Lo lograste!"
- Amorosa 💖: "¡Te queremos, programador!"

---

## 📊 Puntuación

**Total de retos:** 12  
**Para aprobar:** 9/12 correctos (75%)  
**Excelente:** 11/12 correctos (90%+)  

### 🏆 Nivel de Dominio

- **12/12** 🌟🌟🌟 - ¡MAESTRO! Dominio total
- **11/12** 🌟🌟 - ¡EXPERTO! Excelente nivel
- **10/12** 🌟 - ¡AVANZADO! Muy buen trabajo
- **9/12** ✅ - ¡APROBADO! Buen entendimiento
- **< 9/12** 📚 - Necesitas repasar

---

## 🎯 Autoevaluación

Marca lo que lograste dominar:

- [ ] Uso correcto de `and` y `or`
- [ ] Implementación de `break` en búsquedas
- [ ] Aplicación de `continue` para filtrar
- [ ] Creación de bucles anidados
- [ ] Uso de `enumerate()` con índices
- [ ] Implementación de `range()` con step
- [ ] Comprensión de `for-else`
- [ ] Construcción dinámica de listas
- [ ] Uso correcto de slicing
- [ ] Eliminación de duplicados
- [ ] Validación con todos los test cases
- [ ] Código limpio y funcional

---

*Con amor desde la comunidad de programadores Python* 🐍✨

**¡Nos vemos en el Nivel 3!** 🚀💪
    ║
