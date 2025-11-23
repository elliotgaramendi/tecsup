# 🐍 Python Nivel 2: Strings, Condicionales y Bucles Avanzados

```
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║           🐍  PYTHON PROGRAMMING COURSE  🐍             ║
    ║                                                        ║
    ║              ∩＿＿＿∩                                   ║
    ║             /        \                                 ║
    ║            /  ●    ●  \      Level 2                   ║
    ║           |     ▼      |     Intermediate              ║
    ║           |   \___/    |                               ║
    ║            \__________/                                ║
    ║                                                        ║
    ║        Strings • Conditionals • Loops • Lists          ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
```

## 📖 Introducción

¡Bienvenido al Nivel 2! 🎉 Ya dominas los fundamentos de Python, ahora es momento de profundizar en conceptos más poderosos. En este nivel aprenderás a manipular texto como un profesional, crear lógica compleja con condicionales avanzadas y dominar los bucles para automatizar cualquier tarea repetitiva.

## 🎯 Descripción de la Guía

Esta guía está diseñada para estudiantes que ya completaron el Nivel 1 y están listos para desafíos más complejos.

### ✨ ¿Qué aprenderás?

- 📝 **o2.1 - Condicionales II**: Lógica compleja con operadores `and`, `or`, `not`
- 🔄 **o2.2 - Bucles II**: Control de flujo con `break`, `continue`, bucles anidados
- ⚡ **o2.3 - Bucles III**: `enumerate()`, `range()` con pasos, `for-else`
- 📊 **o2.4 - Listas**: Colecciones dinámicas, métodos, slicing

**Tiempo estimado por tema: 2 horas**  
**Tiempo total del nivel: 8 horas**

---

## o2.1: Condicionales II - Lógica Avanzada

### 🎯 Descripción del Tema

Dominarás operadores lógicos (`and`, `or`, `not`) para crear condiciones complejas que evalúan múltiples criterios simultáneamente. Aprenderás a combinar condiciones, validar rangos y crear sistemas de decisión sofisticados.

---

### o2.1.1: 🎫 Sistema de Acceso

**📖 Historia:** Fernanda 🧙‍♀️ gestiona la entrada a un evento exclusivo. Solo pueden entrar personas de 18-65 años Y que tengan invitación. Mijael tiene 25 años y no tiene invitación. ¿Puede entrar?

**📝 Descripción:** Tu programa debe validar dos condiciones simultáneamente: edad en rango válido Y poseer invitación.

**⚙️ Funcionalidades:**
- Validar edad entre 18 y 65 años
- Verificar si tiene invitación (booleano)
- Combinar ambas condiciones con `and`
- Determinar acceso permitido o denegado
- Mostrar mensaje específico de rechazo

**✅ Casos de prueba:**

| Input                          | Expected Output  |
| ------------------------------ | ---------------- |
| `age=25, has_invitation=True`  | `access=True`    |
| `age=25, has_invitation=False` | `access=False`   |
| `age=17, has_invitation=True`  | `access=False`   |
| `age=70, has_invitation=True`  | `access=False`   |
| `type(access)`                 | `<class 'bool'>` |

**💻 Código base:**

```python
# Access System 🎫
age = 25
has_invitation = False
access = None  # your code here 💻

print(f"Edad: {age}, Invitación: {has_invitation}")
print(f"Acceso: {'Permitido ✅' if access else 'Denegado ❌'}")

# Test cases
print(access == False)  # age=25, has_invitation=False
print(type(access) == bool)
```

**💡 Tips:**
- 🔹 Usa `and` para que AMBAS condiciones sean True
- 🔹 Rango: `18 <= age <= 65`
- 🔹 Combina: `(condicion1) and (condicion2)`
- 🔹 `and` retorna False si alguna es False

**🚀 Motivación:** ¡Creas sistemas de seguridad inteligentes! 🎫🔒

---

### o2.1.2: 🎮 Validador de Usuario Premium

**📖 Historia:** Elliot ⚡ diseña un sistema para identificar usuarios premium. Un usuario es premium si tiene nivel ≥50 O ha pagado membresía. Fe tiene nivel 35 pero pagó membresía. ¿Es premium?

**📝 Descripción:** Tu programa debe usar el operador `or` para validar que AL MENOS UNA de dos condiciones se cumpla.

**⚙️ Funcionalidades:**
- Validar nivel del usuario (≥50)
- Verificar si pagó membresía (booleano)
- Usar operador `or` para determinar premium
- Asignar beneficios según resultado
- Calcular descuento (20% premium, 0% regular)

**✅ Casos de prueba:**

| Input                  | Expected Output    |
| ---------------------- | ------------------ |
| `level=35, paid=True`  | `is_premium=True`  |
| `level=60, paid=False` | `is_premium=True`  |
| `level=30, paid=False` | `is_premium=False` |
| `level=50, paid=True`  | `is_premium=True`  |
| `type(is_premium)`     | `<class 'bool'>`   |

**💻 Código base:**

```python
# Premium Validator 🎮
level = 35
paid = True
is_premium = None  # your code here 💻
discount = 0  # your code here 💻 (20 if premium, else 0)

print(f"Nivel: {level}, Membresía: {paid}")
print(f"Premium: {is_premium} | Descuento: {discount}%")

# Test cases
print(is_premium == True)  # level=35, paid=True
print(discount == 20)
print(type(is_premium) == bool)
```

**💡 Tips:**
- 🔹 Usa `or` para que AL MENOS UNA sea True
- 🔹 `(level >= 50) or (paid == True)`
- 🔹 `or` retorna True si alguna es True
- 🔹 Usa operador ternario para descuento

**🚀 Motivación:** ¡Fe obtiene beneficios premium! 🎮✨

---

### o2.1.3: 🚦 Semáforo Inteligente

**📖 Historia:** Chocolate 🐕 cruza la calle. El semáforo tiene 3 estados: 'verde', 'amarillo', 'rojo'. Puede cruzar SOLO si está en verde Y no hay carros pasando. El semáforo está en verde pero pasan 3 carros. ¿Puede cruzar?

**📝 Descripción:** Tu programa debe combinar condición de igualdad con condición numérica usando `and`.

**⚙️ Funcionalidades:**
- Verificar color del semáforo
- Contar carros pasando
- Permitir cruce solo con verde Y 0 carros
- Usar operador `and` para decisión
- Mostrar razón de espera si no puede cruzar

**✅ Casos de prueba:**

| Input                      | Expected Output   |
| -------------------------- | ----------------- |
| `light='verde', cars=0`    | `can_cross=True`  |
| `light='verde', cars=3`    | `can_cross=False` |
| `light='rojo', cars=0`     | `can_cross=False` |
| `light='amarillo', cars=0` | `can_cross=False` |
| `type(can_cross)`          | `<class 'bool'>`  |

**💻 Código base:**

```python
# Smart Traffic Light 🚦
light = 'verde'
cars = 3
can_cross = None  # your code here 💻

print(f"Semáforo: {light} | Carros: {cars}")
print(f"¿Puede cruzar?: {'Sí ✅' if can_cross else 'No ❌'}")

# Test cases
print(can_cross == False)  # light='verde', cars=3
print(type(can_cross) == bool)
```

**💡 Tips:**
- 🔹 Combina: `(light == 'verde') and (cars == 0)`
- 🔹 Usa `==` para comparar strings
- 🔹 Ambas condiciones deben ser True
- 🔹 Puedes usar paréntesis para claridad

**🚀 Motivación:** ¡Chocolate cruza seguro! 🐕🚦

---

### o2.1.4: ⚠️ Detector de Peligro

**📖 Historia:** Amorosa 💖 monitorea una cueva. Hay peligro si la temperatura es >40°C O la humedad es <20% O hay gas tóxico. La cueva tiene 35°C, 15% humedad, sin gas. ¿Hay peligro?

**📝 Descripción:** Tu programa debe usar múltiples condiciones `or` para detectar cualquier señal de peligro.

**⚙️ Funcionalidades:**
- Validar temperatura (peligro si >40)
- Validar humedad (peligro si <20)
- Verificar presencia de gas (booleano)
- Usar `or` múltiple para detectar peligro
- Contar cuántas señales de peligro hay

**✅ Casos de prueba:**

| Input                             | Expected Output  |
| --------------------------------- | ---------------- |
| `temp=35, humidity=15, gas=False` | `danger=True`    |
| `temp=45, humidity=25, gas=False` | `danger=True`    |
| `temp=30, humidity=30, gas=False` | `danger=False`   |
| `temp=35, humidity=15, gas=True`  | `danger=True`    |
| `type(danger)`                    | `<class 'bool'>` |

**💻 Código base:**

```python
# Danger Detector ⚠️
temp = 35
humidity = 15
gas = False
danger = None  # your code here 💻
danger_count = 0  # your code here 💻

print(f"Temp: {temp}°C | Humedad: {humidity}% | Gas: {gas}")
print(f"Peligro: {'SÍ ⚠️' if danger else 'NO ✅'}")
print(f"Señales de peligro: {danger_count}")

# Test cases
print(danger == True)  # temp=35, humidity=15, gas=False
print(danger_count == 1)
print(type(danger) == bool)
```

**💡 Tips:**
- 🔹 Usa: `(temp > 40) or (humidity < 20) or gas`
- 🔹 Con `or`, si CUALQUIERA es True, resultado es True
- 🔹 Cuenta señales sumando condiciones como números
- 🔹 `True` se cuenta como 1, `False` como 0

**🚀 Motivación:** ¡Amorosa detecta peligros a tiempo! 💖⚠️

---

### o2.1.5: 🔐 Sistema de Seguridad Completo

**📖 Historia:** Mijael 🧑‍💻 crea el sistema de seguridad definitivo. Para acceso total necesita: (edad 18-60 Y código correcto) O ser administrador. Doky tiene 25 años, código correcto pero no es admin. ¿Acceso total?

**📝 Descripción:** Tu programa debe combinar `and` y `or` en una expresión compleja con paréntesis.

**⚙️ Funcionalidades:**
- Validar edad en rango (18-60)
- Verificar código de acceso
- Verificar si es administrador
- Combinar: `((edad válida) and código) or admin`
- Determinar nivel de acceso (total/parcial/ninguno)

**✅ Casos de prueba:**

| Input                              | Expected Output     |
| ---------------------------------- | ------------------- |
| `age=25, code='1234', admin=False` | `full_access=True`  |
| `age=70, code='1234', admin=False` | `full_access=False` |
| `age=25, code='0000', admin=False` | `full_access=False` |
| `age=70, code='0000', admin=True`  | `full_access=True`  |
| `type(full_access)`                | `<class 'bool'>`    |

**💻 Código base:**

```python
# Complete Security System 🔐
age = 25
code = '1234'
admin = False
valid_code = '1234'
full_access = None  # your code here 💻

print(f"Edad: {age} | Código: {code} | Admin: {admin}")
print(f"Acceso: {'TOTAL ✅' if full_access else 'DENEGADO ❌'}")

# Test cases
print(full_access == True)  # age=25, code='1234', admin=False
print(type(full_access) == bool)
```

**💡 Tips:**
- 🔹 Usa paréntesis: `((cond1 and cond2) or cond3)`
- 🔹 Los paréntesis controlan el orden
- 🔹 Primero se evalúa lo de adentro
- 🔹 `and` tiene mayor precedencia que `or`

**🚀 Motivación:** ¡Doky entra al sistema seguro! 🔐🐕

---

## o2.2: Bucles II - Control de Flujo

### 🎯 Descripción del Tema

Aprenderás a controlar bucles con precisión usando `break` para salir anticipadamente, `continue` para saltar iteraciones, y bucles anidados para estructuras bidimensionales.

---

### o2.2.1: 🔍 Búsqueda con Break

**📖 Historia:** Fe 👨‍🍳 busca el ingrediente 'sal' en su despensa de 20 elementos. Cuando lo encuentra, debe detenerse inmediatamente y reportar en qué posición estaba. La sal está en la posición 7.

**📝 Descripción:** Tu programa debe recorrer una lista hasta encontrar un elemento específico, usando `break` para detener la búsqueda.

**⚙️ Funcionalidades:**
- Crear lista de 20 ingredientes
- Buscar elemento específico
- Usar `break` cuando lo encuentre
- Contar iteraciones hasta encontrarlo
- Reportar posición del elemento

**✅ Casos de prueba:**

| Input                           | Expected Output              |
| ------------------------------- | ---------------------------- |
| `target='sal', position=7`      | `found=True, iterations=7`   |
| `target='pimienta', position=3` | `found=True, iterations=3`   |
| `target='azucar', position=15`  | `found=True, iterations=15`  |
| `target='inexistente'`          | `found=False, iterations=20` |
| `type(found)`                   | `<class 'bool'>`             |

**💻 Código base:**

```python
# Ingredient Finder 🔍
pantry = ['harina', 'aceite', 'pimienta', 'arroz', 'pasta', 'tomate', 'sal', 
          'vinagre', 'azucar', 'cafe', 'te', 'leche', 'huevos', 'queso', 
          'mantequilla', 'pan', 'agua', 'jugo', 'yogur', 'cereal']
target = 'sal'
found = False  # your code here 💻
iterations = 0  # your code here 💻
position = -1  # your code here 💻

# Test cases
print(found == True)
print(iterations == 7)
print(position == 6)  # index 6 = position 7
print(type(found) == bool)
```

**💡 Tips:**
- 🔹 Usa `for i, item in enumerate(pantry):`
- 🔹 `if item == target: break`
- 🔹 Incrementa `iterations` en cada vuelta
- 🔹 `break` sale del bucle inmediatamente

**🚀 Motivación:** ¡Fe encuentra ingredientes rápido! 👨‍🍳🔍

---

### o2.2.2: ⏭️ Filtrar con Continue

**📖 Historia:** Fernanda 🧙‍♀️ cuenta números pares del 1 al 20, pero debe SALTAR los múltiplos de 10 (10, 20). Los múltiplos de 10 no se cuentan aunque sean pares.

**📝 Descripción:** Tu programa debe usar `continue` para saltar iteraciones específicas sin procesarlas.

**⚙️ Funcionalidades:**
- Recorrer números del 1 al 20
- Identificar múltiplos de 10
- Usar `continue` para saltarlos
- Contar solo números pares no múltiplos de 10
- Crear lista con números contados

**✅ Casos de prueba:**

| Input              | Expected Output         |
| ------------------ | ----------------------- |
| `range(1, 21)`     | `even_count=8`          |
| `evens_list`       | `[2,4,6,8,12,14,16,18]` |
| `len(evens_list)`  | `8`                     |
| `10 in evens_list` | `False`                 |
| `type(even_count)` | `<class 'int'>`         |

**💻 Código base:**

```python
# Even Filter ⏭️
even_count = 0  # your code here 💻
evens_list = []  # your code here 💻

# Your loop here 💻
# for i in range(1, 21):
#     if multiple of 10: continue
#     if even: count and add

print(f"Pares (sin múltiplos de 10): {even_count}")
print(f"Lista: {evens_list}")

# Test cases
print(even_count == 8)
print(evens_list == [2,4,6,8,12,14,16,18])
print(10 not in evens_list)
print(type(even_count) == int)
```

**💡 Tips:**
- 🔹 `if i % 10 == 0: continue`
- 🔹 `continue` salta a la siguiente iteración
- 🔹 Código después de `continue` no se ejecuta
- 🔹 Útil para filtrar sin anidar mucho

**🚀 Motivación:** ¡Fernanda filtra con elegancia! 🧙‍♀️⏭️

---

### o2.2.3: 🎨 Patrón de Asteriscos

**📖 Historia:** Elliot ⚡ dibuja un triángulo de asteriscos de altura 5. Cada fila tiene tantos asteriscos como su número de fila. Necesita bucles anidados.

**📝 Descripción:** Tu programa debe usar un bucle externo para filas y uno interno para columnas, creando un patrón bidimensional.

**⚙️ Funcionalidades:**
- Bucle externo para 5 filas
- Bucle interno para asteriscos por fila
- Cada fila i tiene i asteriscos
- Acumular patrón en string
- Contar total de asteriscos dibujados

**✅ Casos de prueba:**

| Input                | Expected Output                     |
| -------------------- | ----------------------------------- |
| `height=5`           | `pattern='*\n**\n***\n****\n*****'` |
| `total_stars=15`     | `15` (1+2+3+4+5)                    |
| `lines=5`            | `5`                                 |
| `pattern.count('*')` | `15`                                |
| `type(pattern)`      | `<class 'str'>`                     |

**💻 Código base:**

```python
# Star Pattern 🎨
height = 5
pattern = ''  # your code here 💻
total_stars = 0  # your code here 💻

# Your nested loop here 💻
# for row in range(1, height + 1):
#     for col in range(row):
#         add star

print(pattern)
print(f"Total de estrellas: {total_stars}")

# Test cases
print(pattern.count('\n') == 4)  # 4 saltos de línea para 5 filas
print(total_stars == 15)
print(pattern.count('*') == 15)
print(type(pattern) == str)
```

**💡 Tips:**
- 🔹 Externo: `for i in range(1, height + 1):`
- 🔹 Interno: `for j in range(i):`
- 🔹 Acumula: `pattern += '*' * i + '\n'`
- 🔹 Cuenta: `total_stars += i`

**🚀 Motivación:** ¡Elliot crea arte con código! ⚡🎨

---

### o2.2.4: 📊 Tabla de Multiplicar

**📖 Historia:** Mijael 🧑‍💻 genera las tablas del 1 al 5, cada una del 1 al 10. Necesita mostrar 50 operaciones (5 tablas × 10 operaciones).

**📝 Descripción:** Tu programa usa bucles anidados para generar múltiples tablas de multiplicar completas.

**⚙️ Funcionalidades:**
- Bucle externo para números del 1 al 5
- Bucle interno para multiplicadores del 1 al 10
- Calcular cada producto
- Acumular suma de productos por tabla
- Contar total de operaciones

**✅ Casos de prueba:**

| Input                    | Expected Output       |
| ------------------------ | --------------------- |
| `tables=1 to 5`          | `total_operations=50` |
| `table_3_sum`            | `165` (3+6+9...+30)   |
| `table_1_sum`            | `55` (1+2+3...+10)    |
| `table_5_sum`            | `275` (5+10+15...+50) |
| `type(total_operations)` | `<class 'int'>`       |

**💻 Código base:**

```python
# Multiplication Tables 📊
total_operations = 0  # your code here 💻
table_1_sum = 0  # your code here 💻
table_3_sum = 0  # your code here 💻
table_5_sum = 0  # your code here 💻

# Your nested loop here 💻
# for num in range(1, 6):
#     for mult in range(1, 11):
#         calculate and accumulate

print(f"Total de operaciones: {total_operations}")
print(f"Suma tabla 3: {table_3_sum}")

# Test cases
print(total_operations == 50)
print(table_3_sum == 165)
print(table_5_sum == 275)
print(type(total_operations) == int)
```

**💡 Tips:**
- 🔹 Externo: `for num in range(1, 6):`
- 🔹 Interno: `for mult in range(1, 11):`
- 🔹 Producto: `num * mult`
- 🔹 Suma condicional: `if num == 3: sum += product`

**🚀 Motivación:** ¡Mijael automatiza las matemáticas! 🧑‍💻📊

---

### o2.2.5: 🎲 Suma hasta Límite

**📖 Historia:** Chocolate 🐕 suma números del 1 al 100, pero se detiene cuando la suma supera 500. ¿En qué número se detiene y cuál es la suma final?

**📝 Descripción:** Tu programa debe usar `break` para detener un bucle cuando se alcanza una condición específica.

**⚙️ Funcionalidades:**
- Iniciar suma en 0
- Recorrer números del 1 al 100
- Acumular suma
- Usar `break` cuando suma > 500
- Reportar último número sumado y suma final

**✅ Casos de prueba:**

| Input             | Expected Output                |
| ----------------- | ------------------------------ |
| `limit=500`       | `last_num=31, total_sum=496`   |
| `limit=1000`      | `last_num=44, total_sum=990`   |
| `limit=100`       | `last_num=13, total_sum=91`    |
| `limit=5000`      | `last_num=100, total_sum=5050` |
| `type(total_sum)` | `<class 'int'>`                |

**💻 Código base:**

```python
# Sum Until Limit 🎲
limit = 500
total_sum = 0  # your code here 💻
last_num = 0  # your code here 💻

# Your loop here 💻
# for i in range(1, 101):
#     if sum + i > limit: break

print(f"Límite: {limit}")
print(f"Suma final: {total_sum}")
print(f"Último número: {last_num}")

# Test cases
print(last_num == 31)
print(total_sum == 496)
print(type(total_sum) == int)
```

**💡 Tips:**
- 🔹 Verifica ANTES de sumar: `if total_sum + i > limit:`
- 🔹 Guarda `last_num` antes de break
- 🔹 `break` detiene inmediatamente
- 🔹 La suma final está en `total_sum`

**🚀 Motivación:** ¡Chocolate controla límites perfectamente! 🐕🎲

---

## o2.3: Bucles III - Iteración Avanzada

### 🎯 Descripción del Tema

Técnicas avanzadas: `enumerate()` para índice+valor, `range()` con pasos, bucles `for-else`, y patrones de acumulación complejos.

---

### o2.3.1: 📇 Lista con Índices

**📖 Historia:** Amorosa 💖 tiene una lista de 5 frutas: ['manzana', 'pera', 'uva', 'fresa', 'kiwi']. Necesita mostrar cada fruta con su posición usando `enumerate()`.

**📝 Descripción:** Tu programa usa `enumerate()` para obtener índice y valor simultáneamente durante la iteración.

**⚙️ Funcionalidades:**
- Crear lista de 5 frutas
- Usar `enumerate()` en el bucle
- Obtener índice y elemento
- Formatear salida "posición: elemento"
- Validar que recorre todas

**✅ Casos de prueba:**

| Input                    | Expected Output  |
| ------------------------ | ---------------- |
| `fruits[0]`              | `'manzana'`      |
| `enumerate_output[0]`    | `'0: manzana'`   |
| `enumerate_output[2]`    | `'2: uva'`       |
| `len(enumerate_output)`  | `5`              |
| `type(enumerate_output)` | `<class 'list'>` |

**💻 Código base:**

```python
# Fruit Enumerator 📇
fruits = ['manzana', 'pera', 'uva', 'fresa', 'kiwi']
enumerate_output = []  # your code here 💻

# Your loop here 💻
# for index, fruit in enumerate(fruits):

print("Frutas con índice:")
for line in enumerate_output:
    print(line)

# Test cases
print(enumerate_output[0] == '0: manzana')
print(enumerate_output[2] == '2: uva')
print(len(enumerate_output) == 5)
print(type(enumerate_output) == list)
```

**💡 Tips:**
- 🔹 `for i, item in enumerate(lista):`
- 🔹 `i` es el índice (empieza en 0)
- 🔹 `item` es el valor
- 🔹 Formatea: `f"{i}: {item}"`

**🚀 Motivación:** ¡Amorosa enumera con estilo! 💖📇

---

### o2.3.2: ⏩ Saltos Personalizados

**📖 Historia:** Doky 🐕 cuenta del 0 al 30 pero solo los múltiplos de 5 (0, 5, 10, 15, 20, 25, 30). Usa `range()` con step personalizado.

**📝 Descripción:** Tu programa usa el tercer parámetro de `range()` para controlar el paso de iteración.

**⚙️ Funcionalidades:**
- Usar `range(start, stop, step)`
- Generar múltiplos de 5 del 0 al 30
- Sumar los números generados
- Contar cuántos números se generaron
- Crear lista con los números

**✅ Casos de prueba:**

| Input             | Expected Output                  |
| ----------------- | -------------------------------- |
| `range(0, 31, 5)` | `multiples=[0,5,10,15,20,25,30]` |
| `total_sum`       | `105`                            |
| `count`           | `7`                              |
| `multiples[3]`    | `15`                             |
| `type(multiples)` | `<class 'list'>`                 |

**💻 Código base:**

```python
# Custom Step Counter ⏩
multiples = []  # your code here 💻
total_sum = 0  # your code here 💻
count = 0  # your code here 💻

# Your loop here 💻
# for i in range(0, 31, 5):

print(f"Múltiplos de 5: {multiples}")
print(f"Suma total: {total_sum}")
print(f"Cantidad: {count}")

# Test cases
print(multiples == [0, 5, 10, 15, 20, 25, 30])
print(total_sum == 105)
print(count == 7)
print(type(multiples) == list)
```

**💡 Tips:**
- 🔹 `range(0, 31, 5)` genera: 0, 5, 10, 15, 20, 25, 30
- 🔹 Tercer parámetro es el "paso" o "step"
- 🔹 Acumula suma y cuenta en el bucle
- 🔹 `append()` para agregar a la lista

**🚀 Motivación:** ¡Doky cuenta con saltos! 🐕⏩

---

### o2.3.3: 🔄 Separar Pares e Impares

**📖 Historia:** Fe 👨‍🍳 tiene una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. En UN SOLO bucle debe separarlos: pares en una lista, impares en otra, y sumar cada grupo.

**📝 Descripción:** Tu programa debe clasificar números en una sola pasada, usando acumuladores múltiples.

**⚙️ Funcionalidades:**
- Recorrer lista de 10 números
- Identificar pares e impares con `%`
- Acumular pares en lista y suma
- Acumular impares en lista y suma
- Todo en un solo bucle

**✅ Casos de prueba:**

| Input             | Expected Output  |
| ----------------- | ---------------- |
| `even_list`       | `[2,4,6,8,10]`   |
| `odd_list`        | `[1,3,5,7,9]`    |
| `even_sum`        | `30`             |
| `odd_sum`         | `25`             |
| `type(even_list)` | `<class 'list'>` |

**💻 Código base:**

```python
# Even/Odd Separator 🔄
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []  # your code here 💻
odd_list = []  # your code here 💻
even_sum = 0  # your code here 💻
odd_sum = 0  # your code here 💻

# Your loop here 💻
# for num in numbers:

print(f"Pares: {even_list} | Suma: {even_sum}")
print(f"Impares: {odd_list} | Suma: {odd_sum}")

# Test cases
print(even_list == [2, 4, 6, 8, 10])
print(odd_list == [1, 3, 5, 7, 9])
print(even_sum == 30)
print(odd_sum == 25)
print(type(even_list) == list)
```

**💡 Tips:**
- 🔹 `if num % 2 == 0:` identifica pares
- 🔹 `else:` para impares
- 🔹 Usa `.append()` y `+=` en cada caso
- 🔹 Eficiente: un solo bucle para todo

**🚀 Motivación:** ¡Fe clasifica con eficiencia! 👨‍🍳🔄

---

### o2.3.4: 🔍 Búsqueda con For-Else

**📖 Historia:** Elliot ⚡ busca 'Python' en una lista de lenguajes: ['Java', 'C++', 'Ruby', 'Go', 'JavaScript']. Si NO lo encuentra, el `else` del `for` se ejecuta. ¿Lo encontrará?

**📝 Descripción:** Tu programa usa el `else` especial de Python que se ejecuta solo si el `for` NO fue interrumpido con `break`.

**⚙️ Funcionalidades:**
- Crear lista de lenguajes sin 'Python'
- Buscar 'Python' en la lista
- Usar `break` si lo encuentra
- Usar `else` del for si no lo encuentra
- Reportar resultado booleano

**✅ Casos de prueba:**

| Input                                          | Expected Output  |
| ---------------------------------------------- | ---------------- |
| `search='Python', found=False`                 | `found=False`    |
| `search='Java', found=True`                    | `found=True`     |
| `languages=['Java','Python'], search='Python'` | `found=True`     |
| `else_executed (for not found)`                | `True`           |
| `type(found)`                                  | `<class 'bool'>` |

**💻 Código base:**

```python
# For-Else Finder 🔍
languages = ['Java', 'C++', 'Ruby', 'Go', 'JavaScript']
search = 'Python'
found = False  # your code here 💻
else_executed = False  # your code here 💻

# Your loop here 💻
# for lang in languages:
#     if lang == search:
#         found = True
#         break
# else:
#     else_executed = True

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
- 🔹 `else` se ejecuta si NO hubo `break`
- 🔹 Perfecto para "no encontrado"
- 🔹 Característica única de Python

**🚀 Motivación:** ¡Elliot usa for-else como pro! ⚡🔍

---

### o2.3.5: 📊 Análisis de Rango

**📖 Historia:** Fernanda 🧙‍♀️ analiza números del 1 al 20. Necesita: cantidad de pares, impares, múltiplos de 3, múltiplos de 5, y suma total. Todo en un solo bucle eficiente.

**📝 Descripción:** Tu programa usa acumuladores múltiples para extraer varias estadísticas en una sola pasada.

**⚙️ Funcionalidades:**
- Recorrer números del 1 al 20
- Contar pares e impares
- Contar múltiplos de 3
- Contar múltiplos de 5
- Sumar todos los números

**✅ Casos de prueba:**

| Input          | Expected Output |
| -------------- | --------------- |
| `even_count`   | `10`            |
| `odd_count`    | `10`            |
| `mult_3_count` | `6`             |
| `mult_5_count` | `4`             |
| `total_sum`    | `210`           |

**💻 Código base:**

```python
# Range Analyzer 📊
even_count = 0  # your code here 💻
odd_count = 0  # your code here 💻
mult_3_count = 0  # your code here 💻
mult_5_count = 0  # your code here 💻
total_sum = 0  # your code here 💻

# Your loop here 💻
# for i in range(1, 21):

print(f"Pares: {even_count} | Impares: {odd_count}")
print(f"Múltiplos de 3: {mult_3_count} | Múltiplos de 5: {mult_5_count}")
print(f"Suma total: {total_sum}")

# Test cases
print(even_count == 10)
print(odd_count == 10)
print(mult_3_count == 6)
print(mult_5_count == 4)
print(total_sum == 210)
```

**💡 Tips:**
- 🔹 Usa múltiples `if` (no elif) para contar todo
- 🔹 `i % 2 == 0` para pares
- 🔹 `i % 3 == 0` para múltiplos de 3
- 🔹 Acumula suma con `+=`

**🚀 Motivación:** ¡Fernanda analiza como científica de datos! 🧙‍♀️📊

---

## o2.4: Listas - Colecciones Dinámicas

### 🎯 Descripción del Tema

Las listas son la estructura de datos más versátil de Python. Dominarás métodos como `.append()`, `.remove()`, `.sort()`, `.reverse()`, y técnicas de slicing para manipular colecciones.

---

### o2.4.1: ➕ Construir Lista Dinámica

**📖 Historia:** Mijael 🧑‍💻 crea una lista vacía y agrega 5 lenguajes de programación uno por uno: 'Python', 'JavaScript', 'Java', 'C++', 'Ruby'. Usa `.append()` para cada uno.

**📝 Descripción:** Tu programa construye una lista dinámicamente, agregando elementos con el método `.append()`.

**⚙️ Funcionalidades:**
- Iniciar lista vacía `[]`
- Agregar 5 elementos con `.append()`
- Obtener primer y último elemento
- Contar total de elementos
- Verificar tipo de dato

**✅ Casos de prueba:**

| Input                 | Expected Output  |
| --------------------- | ---------------- |
| `languages[0]`        | `'Python'`       |
| `languages[-1]`       | `'Ruby'`         |
| `len(languages)`      | `5`              |
| `'Java' in languages` | `True`           |
| `type(languages)`     | `<class 'list'>` |

**💻 Código base:**

```python
# Dynamic List Builder ➕
languages = []  # your code here 💻
# append: Python, JavaScript, Java, C++, Ruby

print(f"Lista: {languages}")
print(f"Primero: {languages[0]}")
print(f"Último: {languages[-1]}")
print(f"Total: {len(languages)}")

# Test cases
print(languages[0] == 'Python')
print(languages[-1] == 'Ruby')
print(len(languages) == 5)
print('Java' in languages)
print(type(languages) == list)
```

**💡 Tips:**
- 🔹 `.append(elemento)` agrega al final
- 🔹 `lista[0]` primer elemento
- 🔹 `lista[-1]` último elemento
- 🔹 `len(lista)` cuenta elementos

**🚀 Motivación:** ¡Mijael construye colecciones dinámicas! 🧑‍💻➕

---

### o2.4.2: ✂️ Slicing Maestro

**📖 Historia:** Chocolate 🐕 tiene una lista de 10 números: [1,2,3,4,5,6,7,8,9,10]. Necesita extraer: primeros 3, últimos 3, y elementos del medio (índice 3 al 7).

**📝 Descripción:** Tu programa usa slicing `[start:end]` para extraer subsecciones de listas.

**⚙️ Funcionalidades:**
- Crear lista de 10 números
- Extraer primeros 3 con `[0:3]`
- Extraer últimos 3 con `[-3:]`
- Extraer medio con `[3:8]`
- Validar longitudes de slices

**✅ Casos de prueba:**

| Input           | Expected Output   |
| --------------- | ----------------- |
| `first_3`       | `[1, 2, 3]`       |
| `last_3`        | `[8, 9, 10]`      |
| `middle`        | `[4, 5, 6, 7, 8]` |
| `len(middle)`   | `5`               |
| `type(first_3)` | `<class 'list'>`  |

**💻 Código base:**

```python
# List Slicer ✂️
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_3 = []  # your code here 💻
last_3 = []  # your code here 💻
middle = []  # your code here 💻 (index 3 to 7)

print(f"Primeros 3: {first_3}")
print(f"Últimos 3: {last_3}")
print(f"Medio (3-7): {middle}")

# Test cases
print(first_3 == [1, 2, 3])
print(last_3 == [8, 9, 10])
print(middle == [4, 5, 6, 7, 8])
print(len(middle) == 5)
print(type(first_3) == list)
```

**💡 Tips:**
- 🔹 `lista[0:3]` obtiene índices 0, 1, 2
- 🔹 `lista[-3:]` últimos 3 elementos
- 🔹 `lista[3:8]` índices 3, 4, 5, 6, 7
- 🔹 El índice final NO se incluye

**🚀 Motivación:** ¡Chocolate corta listas con precisión! 🐕✂️

---

### o2.4.3: 🔄 Ordenar y Revertir

**📖 Historia:** Amorosa 💖 tiene una lista desordenada: [5, 2, 8, 1, 9, 3]. Necesita crear una copia ordenada ascendente y otra descendente, sin modificar la original.

**📝 Descripción:** Tu programa usa `.sort()` y `.reverse()` para ordenar listas, trabajando con copias.

**⚙️ Funcionalidades:**
- Crear lista desordenada
- Copiar con `.copy()`
- Ordenar ascendente con `.sort()`
- Ordenar descendente con `.sort(reverse=True)`
- Verificar que original no cambió

**✅ Casos de prueba:**

| Input             | Expected Output      |
| ----------------- | -------------------- |
| `original`        | `[5, 2, 8, 1, 9, 3]` |
| `ascending`       | `[1, 2, 3, 5, 8, 9]` |
| `descending`      | `[9, 8, 5, 3, 2, 1]` |
| `original[0]`     | `5`                  |
| `type(ascending)` | `<class 'list'>`     |

**💻 Código base:**

```python
# List Sorter 🔄
original = [5, 2, 8, 1, 9, 3]
ascending = []  # your code here 💻 (copy and sort)
descending = []  # your code here 💻 (copy and reverse sort)

print(f"Original: {original}")
print(f"Ascendente: {ascending}")
print(f"Descendente: {descending}")

# Test cases
print(original == [5, 2, 8, 1, 9, 3])
print(ascending == [1, 2, 3, 5, 8, 9])
print(descending == [9, 8, 5, 3, 2, 1])
print(original[0] == 5)
print(type(ascending) == list)
```

**💡 Tips:**
- 🔹 `lista.copy()` crea copia
- 🔹 `.sort()` modifica la lista
- 🔹 `.sort(reverse=True)` descendente
- 🔹 O usa `sorted(lista)` que NO modifica

**🚀 Motivación:** ¡Amorosa organiza sin perder datos! 💖🔄

---

### o2.4.4: 🗑️ Eliminar Duplicados

**📖 Historia:** Doky 🐕 tiene una lista con duplicados: [1, 2, 2, 3, 4, 3, 5, 1]. Necesita crear una lista nueva con solo valores únicos, manteniendo el orden original.

**📝 Descripción:** Tu programa elimina duplicados recorriendo la lista y verificando existencia antes de agregar.

**⚙️ Funcionalidades:**
- Crear lista con duplicados
- Recorrer lista original
- Verificar con `not in` antes de agregar
- Mantener orden original
- Contar elementos únicos

**✅ Casos de prueba:**

| Input          | Expected Output     |
| -------------- | ------------------- |
| `original`     | `[1,2,2,3,4,3,5,1]` |
| `unique`       | `[1, 2, 3, 4, 5]`   |
| `len(unique)`  | `5`                 |
| `unique[0]`    | `1`                 |
| `type(unique)` | `<class 'list'>`    |

**💻 Código base:**

```python
# Duplicate Remover 🗑️
original = [1, 2, 2, 3, 4, 3, 5, 1]
unique = []  # your code here 💻

# Your loop here 💻
# for item in original:
#     if item not in unique:

print(f"Original: {original}")
print(f"Sin duplicados: {unique}")
print(f"Elementos únicos: {len(unique)}")

# Test cases
print(original == [1, 2, 2, 3, 4, 3, 5, 1])
print(unique == [1, 2, 3, 4, 5])
print(len(unique) == 5)
print(unique[0] == 1)
print(type(unique) == list)
```

**💡 Tips:**
- 🔹 `if item not in unique:` verifica
- 🔹 `.append()` agrega solo si no existe
- 🔹 Mantiene orden de primera aparición
- 🔹 Alternativa: `list(set(lista))` (pierde orden)

**🚀 Motivación:** ¡Doky limpia datos como experto! 🐕🗑️

---

### o2.4.5: 🔧 Métodos de Lista Completos

**📖 Historia:** Fe 👨‍🍳 gestiona su lista de ingredientes: ['sal', 'pimienta', 'azucar']. Necesita: agregar 'aceite', eliminar 'azucar', insertar 'vinagre' en posición 1, y contar elementos finales.

**📝 Descripción:** Tu programa usa múltiples métodos de lista: `.append()`, `.remove()`, `.insert()`, `.pop()`.

**⚙️ Funcionalidades:**
- Iniciar con 3 elementos
- Agregar elemento al final
- Eliminar elemento específico
- Insertar en posición específica
- Usar `.pop()` para eliminar último
- Contar elementos finales

**✅ Casos de prueba:**

| Input                    | Expected Output                |
| ------------------------ | ------------------------------ |
| `initial`                | `['sal','pimienta','azucar']`  |
| `after_operations`       | `['sal','vinagre','pimienta']` |
| `len(after_operations)`  | `3`                            |
| `'azucar' not in final`  | `True`                         |
| `type(after_operations)` | `<class 'list'>`               |

**💻 Código base:**

```python
# List Methods Master 🔧
ingredients = ['sal', 'pimienta', 'azucar']  # your code here 💻
# append 'aceite'
# remove 'azucar'
# insert 'vinagre' at position 1
# pop last

print(f"Lista final: {ingredients}")
print(f"Total elementos: {len(ingredients)}")

# Test cases
print('vinagre' in ingredients)
print('azucar' not in ingredients)
print(len(ingredients) == 3)
print(ingredients[1] == 'vinagre')
print(type(ingredients) == list)
```

**💡 Tips:**
- 🔹 `.append(item)` agrega al final
- 🔹 `.remove(item)` elimina primera ocurrencia
- 🔹 `.insert(index, item)` inserta en posición
- 🔹 `.pop()` elimina y retorna último

**🚀 Motivación:** ¡Fe domina todos los métodos de lista! 👨‍🍳🔧

---

## 🎉 ¡Felicidades! Has completado el Nivel 2

### 📊 Resumen de Logros

**✅ Has dominado:**
- 🎯 **Condicionales II**: Operadores `and`, `or`, `not`, condiciones complejas
- 🔄 **Bucles II**: `break`, `continue`, bucles anidados, control de flujo
- ⚡ **Bucles III**: `enumerate()`, `range()` con steps, `for-else`, acumuladores
- 📊 **Listas**: Métodos `.append()`, `.remove()`, `.sort()`, slicing, copias

**⏰ Tiempo completado:** 8 horas de práctica intensiva

**🎓 Habilidades adquiridas:**
- Lógica compleja con múltiples condiciones
- Control preciso de flujo de ejecución
- Iteración avanzada y eficiente
- Manipulación completa de colecciones dinámicas

**🔜 Próximo nivel:** Nivel 3 - Tuplas, Diccionarios y Sets

---

💪 **¡Excelente trabajo!** Fernanda, Elliot, Fe, Mijael, Chocolate, Doky y Amorosa están orgullosos de ti. ¡Eres un verdadero programador intermedio! 🏆✨🚀
