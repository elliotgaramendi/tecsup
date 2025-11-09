# 🐍 Guía Nivel 2: Dominando Strings, Condicionales y Bucles Avanzados

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

---

## 📖 Introducción

¡Bienvenido al Nivel 2! 🎉 Ya dominas los fundamentos de Python, ahora es momento de profundizar en conceptos más poderosos. En este nivel aprenderás a manipular texto como un profesional, crear lógica compleja con condicionales avanzadas y dominar los bucles para automatizar cualquier tarea repetitiva.

Estos conceptos son esenciales para crear aplicaciones reales que procesen datos, validen información y respondan de manera inteligente a diferentes situaciones. ¡Prepárate para llevar tus habilidades al siguiente nivel! 🚀

---

## 🎯 Descripción de la Guía

Esta guía está diseñada para estudiantes que ya completaron el Nivel 1 y están listos para desafíos más complejos. A través de ejercicios prácticos y proyectos integradores, dominarás:

### ✨ ¿Qué aprenderás?

- 📝 **Strings y Condicionales Avanzadas**: Manipulación de texto y lógica compleja
- 🔄 **Bucles Anidados**: Control de flujo avanzado con break y continue
- 🎨 **Patrones y Algoritmos**: Iteración múltiple y estructuras complejas
- 📊 **Listas Dinámicas**: Colecciones ordenadas y métodos poderosos

### 🎓 Metodología

Cada tema incluye:
- 📚 Conceptos con ejemplos claros
- 💻 3-4 ejercicios prácticos progresivos
- 🏗️ 1 proyecto integrador por tema (2 horas aprox.)
- 💡 Tips profesionales
- 🎉 Motivación constante

**Tiempo estimado por tema: 2 horas**
**Tiempo total del nivel: 8 horas**

---

## 🧠 Conceptos Básicos

### 📝 ¿Qué son los Strings?
Los strings (cadenas de texto) son secuencias de caracteres. En Python, todo texto entre comillas es un string. Son fundamentales porque la mayoría de programas interactúan con usuarios mediante texto.

### 🎯 Condicionales Avanzadas
Las condicionales complejas usan operadores lógicos (`and`, `or`, `not`) para evaluar múltiples condiciones simultáneamente, permitiendo decisiones más sofisticadas.

### 🔁 Bucles Anidados
Un bucle dentro de otro bucle. Son fundamentales para trabajar con estructuras bidimensionales como tablas, matrices o patrones visuales.

### 📊 Listas
Las listas son colecciones ordenadas y modificables que pueden almacenar múltiples valores. Son la estructura de datos más usada en Python.

---

# 📝 o2.1: Strings y Condicionales Avanzadas

## 🎯 Descripción del Tema

En este tema dominarás la manipulación de texto y la lógica compleja. Aprenderás métodos poderosos de strings como `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()` y más. También combinarás múltiples condiciones usando operadores lógicos para crear programas inteligentes que tomen decisiones complejas.

---

## 💻 o2.1.1: 🔤 Conversor de Mayúsculas y Minúsculas

### 🎯 Problema
Convertir un texto ingresado por el usuario a mayúsculas, minúsculas y tipo título.

### 📝 Descripción
Tu programa debe tomar una cadena de texto y mostrar tres versiones: todo en MAYÚSCULAS, todo en minúsculas, y en Formato De Título (cada palabra inicia con mayúscula).

### ⚙️ Funcionalidades
- Solicitar texto al usuario
- Convertir a mayúsculas usando `.upper()`
- Convertir a minúsculas usando `.lower()`
- Convertir a título usando `.title()`

### 🧪 Casos de Prueba
1. text = "hola mundo" → upper = "HOLA MUNDO", lower = "hola mundo", title = "Hola Mundo"
2. text = "PYTHON" → upper = "PYTHON", lower = "python", title = "Python"
3. text = "Aprender Python" → upper = "APRENDER PYTHON", lower = "aprender python", title = "Aprender Python"

### 💻 Código Base
```python
# Text Case Converter 🔤
print("🔤 Conversor de Mayúsculas/Minúsculas")
print("=" * 40)

# Your code here 👇
upper_text = ""
lower_text = ""
title_text = ""

# Example output:
# MAYÚSCULAS: HOLA MUNDO
# minúsculas: hola mundo
# Título: Hola Mundo

# Test cases:
print("=" * 40)
print(upper_text == "HOLA MUNDO" and lower_text == "hola mundo" and title_text == "Hola Mundo")
print(upper_text == "PYTHON" and lower_text == "python" and title_text == "Python")
print(upper_text == "APRENDER PYTHON" and lower_text == "aprender python" and title_text == "Aprender Python")
```

### 💡 Tips Útiles
- `.upper()` convierte todo a mayúsculas
- `.lower()` convierte todo a minúsculas
- `.title()` capitaliza la primera letra de cada palabra
- Los métodos de strings NO modifican el original, devuelven uno nuevo

### 🎉 Motivación
¡Dominas la transformación de texto! Estos métodos son esenciales para validar entradas y formatear datos. 🎨

---

## 💻 o2.1.2: ✂️ Extractor de Palabras

### 🎯 Problema
Dividir una oración en palabras individuales y contar cuántas hay.

### 📝 Descripción
Tu programa debe tomar una oración, separarla en palabras usando `.split()`, contar cuántas palabras hay y mostrar la primera y última palabra.

### ⚙️ Funcionalidades
- Solicitar una oración al usuario
- Dividir en palabras con `.split()`
- Contar total de palabras
- Identificar primera y última palabra

### 🧪 Casos de Prueba
1. sentence = "Python es genial" → count = 3, first = "Python", last = "genial"
2. sentence = "Programar" → count = 1, first = "Programar", last = "Programar"
3. sentence = "Me encanta aprender Python todos los días" → count = 7, first = "Me", last = "días"

### 💻 Código Base
```python
# Word Extractor ✂️
print("✂️ Extractor de Palabras")
print("=" * 30)

# Your code here 👇
word_count = 0
first_word = ""
last_word = ""

# Example output:
# Total de palabras: 3
# Primera palabra: Python
# Última palabra: genial

# Test cases:
print("=" * 30)
print(word_count == 3 and first_word == "Python" and last_word == "genial")
print(word_count == 1 and first_word == "Programar" and last_word == "Programar")
print(word_count == 7 and first_word == "Me" and last_word == "días")
```

### 💡 Tips Útiles
- `.split()` convierte un string en lista de palabras
- `len(lista)` cuenta elementos en una lista
- Primera palabra: `words[0]`
- Última palabra: `words[-1]`

### 🎉 Motivación
¡Procesas texto como datos estructurados! El análisis de texto es fundamental en IA y procesamiento de lenguaje natural. 🧠

---

## 💻 o2.1.3: 🔍 Buscador y Reemplazador

### 🎯 Problema
Buscar una palabra en un texto y reemplazarla por otra.

### 📝 Descripción
Tu programa debe permitir al usuario ingresar un texto, buscar si contiene una palabra específica, y si la encuentra, reemplazarla por otra palabra.

### ⚙️ Funcionalidades
- Solicitar texto original
- Buscar palabra con `in` o `.count()`
- Reemplazar palabra con `.replace()`
- Mostrar texto modificado

### 🧪 Casos de Prueba
1. text = "Python es genial", search = "genial", replace = "increíble" → result = "Python es increíble"
2. text = "Aprender Python", search = "Python", replace = "programación" → result = "Aprender programación"
3. text = "Hola mundo", search = "adiós", replace = "chao" → result = "Hola mundo"

### 💻 Código Base
```python
# Word Finder and Replacer 🔍
print("🔍 Buscador y Reemplazador")
print("=" * 35)

# Your code here 👇
result = ""

# Example output:
# Texto modificado: Python es increíble ✨

# Test cases:
print("=" * 35)
print(result == "Python es increíble")
print(result == "Aprender programación")
print(result == "Hola mundo")
```

### 💡 Tips Útiles
- `palabra in texto` verifica si existe
- `.replace(viejo, nuevo)` reemplaza todas las ocurrencias
- Si no encuentra la palabra, devuelve el texto original
- `.count(palabra)` cuenta cuántas veces aparece

### 🎉 Motivación
¡Manipulas texto dinámicamente! Esta habilidad es clave en editores de texto y procesadores de documentos. ✍️

---

## 💻 o2.1.4: 🎫 Validador de Credenciales

### 🎯 Problema
Validar usuario y contraseña usando condicionales complejas con `and` y `or`.

### 📝 Descripción
Tu programa debe verificar si el nombre de usuario tiene al menos 5 caracteres Y si la contraseña tiene al menos 8 caracteres. Debe dar mensajes específicos para cada tipo de error.

### ⚙️ Funcionalidades
- Solicitar nombre de usuario
- Solicitar contraseña
- Validar longitud del usuario (≥5)
- Validar longitud de contraseña (≥8)
- Usar operadores lógicos `and`/`or`

### 🧪 Casos de Prueba
1. username = "admin", password = "password123" → status = "válido"
2. username = "ana", password = "12345678" → status = "usuario inválido"
3. username = "carlos", password = "1234" → status = "contraseña inválida"

### 💻 Código Base
```python
# Credential Validator 🎫
print("🎫 Validador de Credenciales")
print("=" * 35)

# Your code here 👇
status = ""

# Example output:
# ✅ Credenciales válidas
# ❌ Usuario debe tener al menos 5 caracteres
# ❌ Contraseña debe tener al menos 8 caracteres

# Test cases:
print("=" * 35)
print(status == "válido")
print(status == "usuario inválido")
print(status == "contraseña inválida")
```

### 💡 Tips Útiles
- `len(texto)` devuelve la longitud
- Usa `and` para combinar condiciones que TODAS deben cumplirse
- Usa `or` cuando AL MENOS UNA debe cumplirse
- Valida usuario primero, luego contraseña

### 🎉 Motivación
¡Creas sistemas de seguridad básicos! Las validaciones complejas protegen aplicaciones reales. 🔒

---

## 🎯 o2.1.P: 📋 Proyecto Integrador - Sistema de Registro de Usuario

### 🏆 Descripción del Proyecto

Crea un sistema completo de registro que valide y procese información de usuarios.

### 📝 Requerimientos

Tu sistema debe:

1. **Captura de Datos**
   - Solicitar nombre completo
   - Solicitar correo electrónico
   - Solicitar edad
   - Solicitar nombre de usuario

2. **Validaciones**
   - Nombre debe tener al menos 3 palabras (nombre + apellidos)
   - Email debe contener "@" y "."
   - Edad debe ser entre 18 y 100 años
   - Usuario debe tener al menos 5 caracteres y no tener espacios

3. **Procesamiento**
   - Convertir nombre a formato título
   - Convertir usuario a minúsculas
   - Generar un código de usuario (primeras 3 letras + edad)

4. **Salida**
   - Mostrar todos los datos validados
   - Mostrar código generado
   - Indicar si el registro fue exitoso

### 🧪 Casos de Prueba

1. name = "juan perez gomez", email = "juan@mail.com", age = 25, username = "JUANP" → 
   valid = True, code = "jua25"

2. name = "Ana Lopez", email = "ana@correo", age = 17, username = "ana" → 
   valid = False, error = "edad menor"

3. name = "Carlos Rodriguez Martinez", email = "carlos@gmail.com", age = 30, username = "carlosRM" → 
   valid = True, code = "car30"

### 💻 Código Base

```python
# 📋 User Registration System
print("📋 SISTEMA DE REGISTRO DE USUARIO")
print("=" * 40)

# Your code here 👇
valid = False
user_code = ""
error = ""

# Example output:
# ✅ REGISTRO EXITOSO
# Nombre: Juan Perez Gomez
# Email: juan@mail.com
# Edad: 25 años
# Usuario: juanp
# Código: jua25

# Test cases:
print("=" * 40)
print(valid == True and user_code == "jua25")
print(valid == False and error == "nombre incompleto")
print(valid == True and user_code == "car30")
```

### 💡 Tips Útiles
- Usa `.split()` para contar palabras en el nombre
- `"@" in email and "." in email` para validar email
- `" " in username` detecta espacios
- `username[:3]` obtiene las primeras 3 letras
- Encadena validaciones con `if-elif-else`

### 🎉 Motivación
¡Construiste un sistema real de validación de usuarios! Estos conceptos se usan en TODAS las aplicaciones web. 🌐

---

# 🔄 o2.2: Bucles II - Control de Flujo Avanzado

## 🎯 Descripción del Tema

Dominarás el control avanzado de bucles usando `break` para salir prematuramente, `continue` para saltar iteraciones, y bucles anidados para crear estructuras bidimensionales. También aprenderás a usar `while` con condiciones complejas y a combinar bucles con condicionales para algoritmos más sofisticados.

---

## 💻 o2.2.1: 🛑 Buscador con Break

### 🎯 Problema
Buscar un número específico en un rango y detener la búsqueda cuando lo encuentre.

### 📝 Descripción
Tu programa debe buscar un número objetivo del 1 al 20. Cuando lo encuentre, debe detenerse inmediatamente usando `break` y reportar en qué iteración lo encontró.

### ⚙️ Funcionalidades
- Solicitar número a buscar (1-20)
- Recorrer números del 1 al 20
- Usar `break` cuando encuentre el número
- Contar iteraciones realizadas

### 🧪 Casos de Prueba
1. target = 5 → found = True, iterations = 5
2. target = 1 → found = True, iterations = 1
3. target = 15 → found = True, iterations = 15

### 💻 Código Base
```python
# Number Finder with Break 🛑
print("🛑 Buscador de Números")
print("=" * 30)

# Your code here 👇
found = False
iterations = 0

# Example output:
# ✅ Número 5 encontrado en la iteración 5

# Test cases:
print("=" * 30)
print(found == True and iterations == 5)
print(found == True and iterations == 1)
print(found == True and iterations == 15)
```

### 💡 Tips Útiles
- Usa `for i in range(1, 21):`
- Incrementa `iterations` en cada vuelta
- Usa `if i == target: break`
- `break` sale inmediatamente del bucle

### 🎉 Motivación
¡Optimizas búsquedas! No desperdicies ciclos cuando ya encontraste lo que buscabas. Eficiencia es clave. ⚡

---

## 💻 o2.2.2: ⏭️ Contador de Pares con Continue

### 🎯 Problema
Contar números pares del 1 al 20, pero saltando los múltiplos de 10.

### 📝 Descripción
Tu programa debe contar cuántos números pares hay entre 1 y 20, pero debe saltar (con `continue`) los números 10 y 20 sin contarlos.

### ⚙️ Funcionalidades
- Recorrer números del 1 al 20
- Saltar múltiplos de 10 con `continue`
- Contar solo números pares
- Mostrar total de pares contados

### 🧪 Casos de Prueba
1. Rango 1-20, saltar 10 y 20 → even_count = 8 (2,4,6,8,12,14,16,18)
2. Total iteraciones = 20
3. Múltiplos de 10 no contados

### 💻 Código Base
```python
# Even Counter with Continue ⏭️
print("⏭️ Contador de Pares (sin múltiplos de 10)")
print("=" * 45)

# Your code here 👇
even_count = 0

# Example output:
# Números pares (sin 10 y 20): 8
# Pares encontrados: 2, 4, 6, 8, 12, 14, 16, 18

# Test cases:
print("=" * 45)
print(even_count == 8)
```

### 💡 Tips Útiles
- `if i % 10 == 0: continue` salta múltiplos de 10
- `continue` salta a la siguiente iteración
- Solo cuenta si `i % 2 == 0` y no fue saltado
- `continue` NO sale del bucle, solo salta

### 🎉 Motivación
¡Controlas el flujo con precisión! Saltar iteraciones innecesarias hace tu código más eficiente. 🎯

---

## 💻 o2.2.3: 🎨 Generador de Triángulo

### 🎯 Problema
Crear un triángulo de asteriscos de altura N usando bucles anidados.

### 📝 Descripción
Tu programa debe solicitar la altura del triángulo y dibujarlo usando dos bucles anidados: uno para las filas y otro para las columnas.

### ⚙️ Funcionalidades
- Solicitar altura (N)
- Usar bucle externo para filas
- Usar bucle interno para asteriscos
- Generar patrón creciente

### 🧪 Casos de Prueba
1. height = 3 → pattern = "*\n**\n***"
2. height = 4 → pattern = "*\n**\n***\n****"
3. height = 5 → pattern = "*\n**\n***\n****\n*****"

### 💻 Código Base
```python
# Triangle Generator 🎨
print("🎨 Generador de Triángulo")
print("=" * 30)

# Your code here 👇
pattern = ""

# Example output for height = 3:
# *
# **
# ***

# Test cases:
print("=" * 30)
print(pattern == "*\n**\n***")
print(pattern == "*\n**\n***\n****")
print(pattern == "*\n**\n***\n****\n*****")
```

### 💡 Tips Útiles
- Bucle externo: `for i in range(1, height + 1):`
- Bucle interno: `for j in range(i):` imprime i asteriscos
- Usa `\n` para nueva línea
- Acumula en `pattern += "*" * i + "\n"`

### 🎉 Motivación
¡Creas arte con código! Los bucles anidados son fundamentales para matrices y gráficos. 🖼️

---

## 💻 o2.2.4: 🔢 Tabla de Multiplicar Completa

### 🎯 Problema
Generar tablas de multiplicar del 1 al 5, mostrando cada tabla completamente.

### 📝 Descripción
Tu programa debe usar bucles anidados para generar las tablas del 1, 2, 3, 4 y 5. Cada tabla debe ir del 1 al 10.

### ⚙️ Funcionalidades
- Bucle externo: números del 1 al 5
- Bucle interno: multiplicadores del 1 al 10
- Calcular y mostrar cada producto
- Separar tablas visualmente

### 🧪 Casos de Prueba
1. Tabla 1: suma de productos = 55 (1+2+3...+10)
2. Tabla 5: suma de productos = 275 (5+10+15...+50)
3. Total de operaciones = 50 (5 tablas × 10 operaciones)

### 💻 Código Base
```python
# Complete Multiplication Tables 🔢
print("🔢 Tablas de Multiplicar del 1 al 5")
print("=" * 40)

# Your code here 👇
total_operations = 0
table_5_sum = 0

# Example output:
# Tabla del 1:
# 1 x 1 = 1
# ...
# Tabla del 5:
# 5 x 10 = 50

# Test cases:
print("=" * 40)
print(total_operations == 50)
print(table_5_sum == 275)
```

### 💡 Tips Útiles
- Bucle externo: `for num in range(1, 6):`
- Bucle interno: `for mult in range(1, 11):`
- Resultado: `num * mult`
- Acumula suma para tabla 5 cuando `num == 5`

### 🎉 Motivación
¡Automatizas cálculos masivos! Lo que tomaría horas manualmente, tu código lo hace en milisegundos. 🚀

---

## 🎯 o2.2.P: 🎯 Proyecto Integrador - Juego de Adivina el Número Mejorado

### 🏆 Descripción del Proyecto

Crea un juego completo de adivinanza con múltiples funcionalidades y control de flujo avanzado.

### 📝 Requerimientos

Tu juego debe:

1. **Configuración**
   - Generar número aleatorio entre 1 y 50
   - Dar máximo 7 intentos
   - Contador de intentos

2. **Mecánica del Juego**
   - Solicitar número del jugador
   - Dar pistas: "muy alto", "alto", "bajo", "muy bajo"
   - Pistas especiales: "muy cerca" si está a ±3
   - Usar `break` cuando adivine
   - Usar `continue` si entrada inválida

3. **Sistema de Puntuación**
   - 100 puntos base
   - Restar 10 puntos por intento
   - Bonus de 50 si adivina en ≤3 intentos

4. **Resultados**
   - Mostrar si ganó o perdió
   - Mostrar intentos usados
   - Mostrar puntuación final
   - Opción de jugar de nuevo

### 🧪 Casos de Prueba

1. secret = 25, guesses = [25] → won = True, attempts = 1, score = 140
2. secret = 40, guesses = [20, 30, 35, 38, 40] → won = True, attempts = 5, score = 50
3. secret = 15, guesses = [50, 40, 30, 20, 10, 5, 1] → won = False, attempts = 7, score = 0

### 💻 Código Base

```python
import random

# 🎯 Advanced Number Guessing Game
print("🎯 JUEGO: ADIVINA EL NÚMERO")
print("=" * 35)
print("Adivina un número entre 1 y 50")
print("Tienes 7 intentos máximo")
print("=" * 35)

# Your code here 👇
won = False
attempts = 0
score = 0

# Example output:
# Intento 1: Tu número: 25
# 🎉 ¡CORRECTO! Adivinaste en 1 intento
# 🏆 Puntuación: 140 puntos

# Test cases:
print("=" * 35)
print(won == True and attempts == 1 and score == 140)
print(won == True and attempts == 5 and score == 50)
print(won == False and attempts == 7 and score == 0)
```

### 💡 Tips Útiles
- `import random` y `random.randint(1, 50)` para número secreto
- Usa `while attempts < 7:` para controlar intentos
- `abs(guess - secret) <= 3` detecta "muy cerca"
- `break` cuando `guess == secret`
- Calcula score: `100 - (attempts * 10) + bonus`

### 🎉 Motivación
¡Creaste un videojuego completo con IA básica! Combinas aleatoriedad, lógica y control de flujo avanzado. 🎮

---

# 🔁 o2.3: Bucles III - Iteración Avanzada

## 🎯 Descripción del Tema

Aprenderás técnicas avanzadas de iteración: `enumerate()` para obtener índice y valor simultáneamente, `range()` con pasos personalizados, bucles con else, y patrones de acumulación complejos. Estos conceptos te preparan para trabajar con estructuras de datos más avanzadas.

---

## 💻 o2.3.1: 📇 Enumerador de Elementos

### 🎯 Problema
Mostrar elementos de una lista con su posición usando `enumerate()`.

### 📝 Descripción
Tu programa debe recibir una lista de frutas y mostrar cada una con su índice (posición) usando la función `enumerate()`.

### ⚙️ Funcionalidades
- Definir lista de elementos
- Usar `enumerate()` para obtener índice y valor
- Mostrar posición y elemento
- Contar total de elementos

### 🧪 Casos de Prueba
1. fruits = ["manzana", "pera", "uva"] → count = 3, first = "0: manzana", last = "2: uva"
2. fruits = ["kiwi"] → count = 1, first = "0: kiwi"
3. fruits = ["fresa", "melón", "sandía", "piña"] → count = 4

### 💻 Código Base
```python
# List Enumerator 📇
print("📇 Enumerador de Lista")
print("=" * 25)

# Your code here 👇
fruits = ["manzana", "pera", "uva"]
count = 0
first = ""
last = ""

# Example output:
# 0: manzana
# 1: pera
# 2: uva

# Test cases:
print("=" * 25)
print(count == 3 and first == "0: manzana" and last == "2: uva")
```

### 💡 Tips Útiles
- `enumerate(lista)` devuelve (índice, valor)
- Usa `for i, fruit in enumerate(fruits):`
- Formatea: `f"{i}: {fruit}"`
- `len(fruits)` da el conteo total

### 🎉 Motivación
¡Iteras con información de posición! Esto es esencial para informes, logs y debugging. 📊

---

## 💻 o2.3.2: ⏩ Contador con Saltos

### 🎯 Problema
Contar de 0 a 20 pero solo los múltiplos de 3 usando `range()` con step.

### 📝 Descripción
Tu programa debe usar `range(start, stop, step)` para generar solo los múltiplos de 3 entre 0 y 20, y sumarlos.

### ⚙️ Funcionalidades
- Usar `range(0, 21, 3)` para múltiplos de 3
- Acumular suma de los números
- Contar cuántos números se generaron
- Mostrar lista de números

### 🧪 Casos de Prueba
1. Rango 0-20, step=3 → numbers = [0, 3, 6, 9, 12, 15, 18], sum = 63, count = 7
2. sum_total = 63
3. count = 7

### 💻 Código Base
```python
# Counter with Steps ⏩
print("⏩ Contador con Saltos (Múltiplos de 3)")
print("=" * 45)

# Your code here 👇
sum_total = 0
count = 0

# Example output:
# Múltiplos de 3: 0, 3, 6, 9, 12, 15, 18
# Suma total: 63
# Cantidad: 7

# Test cases:
print("=" * 45)
print(sum_total == 63 and count == 7)
```

### 💡 Tips Útiles
- `range(0, 21, 3)` genera: 0, 3, 6, 9, 12, 15, 18
- El tercer parámetro es el "paso" o "step"
- Acumula: `sum_total += i`
- Cuenta: `count += 1`

### 🎉 Motivación
¡Controlas la secuencia de iteración! Los pasos personalizados son perfectos para patrones específicos. 🎯

---

## 💻 o2.3.3: 🔄 Acumulador de Números Pares e Impares

### 🎯 Problema
Separar y sumar números pares e impares de una lista en un solo bucle.

### 📝 Descripción
Tu programa debe recorrer una lista de números y, en una sola pasada, acumular por separado la suma de pares y la suma de impares.

### ⚙️ Funcionalidades
- Recorrer lista de números
- Identificar si cada número es par o impar
- Acumular suma de pares
- Acumular suma de impares
- Mostrar ambos resultados

### 🧪 Casos de Prueba
1. numbers = [1, 2, 3, 4, 5, 6] → even_sum = 12, odd_sum = 9
2. numbers = [10, 15, 20, 25] → even_sum = 30, odd_sum = 40
3. numbers = [2, 4, 6, 8] → even_sum = 20, odd_sum = 0

### 💻 Código Base
```python
# Even/Odd Accumulator 🔄
print("🔄 Acumulador Pares/Impares")
print("=" * 32)

# Your code here 👇
numbers = [1, 2, 3, 4, 5, 6]
even_sum = 0
odd_sum = 0

# Example output:
# Suma de pares: 12
# Suma de impares: 9

# Test cases:
print("=" * 32)
print(even_sum == 12 and odd_sum == 9)
# Change numbers list for other tests
numbers = [10, 15, 20, 25]
even_sum = 0
odd_sum = 0
# Your loop here again for second test
print(even_sum == 30 and odd_sum == 40)
```

### 💡 Tips Útiles
- Recorre con `for num in numbers:`
- Usa `if num % 2 == 0:` para pares
- Usa `else:` para impares
- Acumula en cada caso correspondiente

### 🎉 Motivación
¡Procesas datos con múltiples criterios simultáneamente! La eficiencia es hacer más con menos bucles. ⚡

---

## 💻 o2.3.4: 🔍 Buscador con Else

### 🎯 Problema
Buscar un elemento en una lista y usar `else` del bucle `for` para detectar si no se encontró.

### 📝 Descripción
En Python, los bucles `for` pueden tener un `else` que se ejecuta solo si el bucle NO fue interrumpido con `break`. Tu programa debe buscar un nombre en una lista.

### ⚙️ Funcionalidades
- Definir lista de nombres
- Buscar nombre específico
- Usar `break` si lo encuentra
- Usar `else` del for si no lo encuentra
- Reportar resultado

### 🧪 Casos de Prueba
1. names = ["Ana", "Carlos", "María"], search = "Carlos" → found = True
2. names = ["Ana", "Carlos", "María"], search = "Pedro" → found = False
3. names = ["Juan"], search = "Juan" → found = True

### 💻 Código Base
```python
# List Searcher with Else 🔍
print("🔍 Buscador con Else")
print("=" * 25)

# Your code here 👇
names = ["Ana", "Carlos", "María"]
search = "Carlos"
found = False

# Example output:
# ✅ Carlos encontrado en la lista

# Test cases:
print("=" * 25)
print(found == True)
search = "Pedro"
found = False
# Your search code here
print(found == False)
```

### 💡 Tips Útiles
- Estructura: `for item in lista: ... else: ...`
- `else` del for se ejecuta si NO hubo `break`
- Usa `if item == search: break` para detener
- El `else` es perfecto para "no encontrado"

### 🎉 Motivación
¡Descubres características únicas de Python! El for-else es elegante y poderoso. 🐍

---

## 🎯 o2.3.P: 🎲 Proyecto Integrador - Analizador de Calificaciones Avanzado

### 🏆 Descripción del Proyecto

Crea un sistema completo que analice calificaciones de múltiples estudiantes con estadísticas detalladas.

### 📝 Requerimientos

Tu sistema debe:

1. **Entrada de Datos**
   - Solicitar número de estudiantes (3-10)
   - Para cada estudiante: nombre y 4 calificaciones
   - Almacenar en listas paralelas

2. **Cálculos por Estudiante**
   - Promedio individual
   - Calificación más alta y más baja
   - Estado: "Aprobado" (≥70) o "Reprobado"

3. **Estadísticas Generales**
   - Promedio general del grupo
   - Mejor promedio individual
   - Peor promedio individual
   - Cantidad de aprobados/reprobados
   - Porcentaje de aprobación

4. **Reportes**
   - Reporte individual por estudiante (con enumerate)
   - Ranking de estudiantes (mejor a peor)
   - Lista de estudiantes en riesgo (promedio < 60)

### 🧪 Casos de Prueba

1. 3 estudiantes: Ana(80,85,90,85), Carlos(70,75,68,72), María(55,60,58,62) →
   group_avg = 72.08, approved = 2, at_risk = 1

2. 2 estudiantes: Luis(90,95,92,88), Elena(78,82,80,85) →
   group_avg = 86.25, best = 91.25, worst = 81.25

### 💻 Código Base

```python
# 🎲 Advanced Grade Analyzer
print("🎲 ANALIZADOR DE CALIFICACIONES AVANZADO")
print("=" * 45)

# Your code here 👇
num_students = 0
group_avg = 0
approved = 0
at_risk = 0
best_avg = 0
worst_avg = 0

# Example output:
# === REPORTE INDIVIDUAL ===
# 0: Ana - Promedio: 85.0 - APROBADO ✅
# 1: Carlos - Promedio: 71.25 - APROBADO ✅
# 2: María - Promedio: 58.75 - REPROBADO ❌
#
# === ESTADÍSTICAS GENERALES ===
# Promedio del grupo: 72.08
# Mejor promedio: 85.0 (Ana)
# Peor promedio: 58.75 (María)
# Aprobados: 2 (66.67%)
# Reprobados: 1 (33.33%)
# En riesgo (<60): 1

# Test cases:
print("=" * 45)
print(abs(group_avg - 72.08) < 0.1 and approved == 2 and at_risk == 1)
```

### 💡 Tips Útiles
- Usa listas para almacenar: `names = []`, `averages = []`
- Para agregar: `names.append(name)`
- `enumerate(names)` para índice y nombre
- `max(averages)` y `min(averages)` para mejor/peor
- `sum(averages) / len(averages)` para promedio general
- Usa `for name, avg in zip(names, averages):` para iterar paralelo

### 🎉 Motivación
¡Sistema profesional de análisis educativo! Combinas múltiples técnicas de iteración y análisis de datos. 📊

---

# 📊 o2.4: Listas - Colecciones Dinámicas

## 🎯 Descripción del Tema

Las listas son la estructura de datos más versátil de Python. Aprenderás a crear, modificar, ordenar y manipular listas usando métodos como `.append()`, `.remove()`, `.sort()`, `.reverse()`, y técnicas de slicing `[start:end]`. Las listas son fundamentales para almacenar y procesar colecciones de datos.

---

## 💻 o2.4.1: ➕ Constructor de Lista

### 🎯 Problema
Crear una lista vacía y agregar 5 elementos ingresados por el usuario.

### 📝 Descripción
Tu programa debe iniciar con una lista vacía, solicitar 5 nombres al usuario y agregarlos uno por uno usando `.append()`.

### ⚙️ Funcionalidades
- Crear lista vacía con `[]`
- Solicitar 5 elementos en un bucle
- Agregar con `.append()`
- Mostrar lista completa al final

### 🧪 Casos de Prueba
1. Elementos: "Python", "Java", "C++", "Ruby", "Go" → list_size = 5, first = "Python", last = "Go"
2. Elementos: "A", "B", "C", "D", "E" → list_size = 5, first = "A"
3. Verificar que lista tiene exactamente 5 elementos

### 💻 Código Base
```python
# List Builder ➕
print("➕ Constructor de Lista")
print("=" * 27)
print("Ingresa 5 lenguajes de programación:")

# Your code here 👇
languages = []
list_size = 0
first = ""
last = ""

# Example output:
# Lista creada: ['Python', 'Java', 'C++', 'Ruby', 'Go']
# Primer elemento: Python
# Último elemento: Go

# Test cases:
print("=" * 27)
print(list_size == 5 and first == "Python" and last == "Go")
```

### 💡 Tips Útiles
- Inicia con `languages = []`
- Usa `for i in range(5):` para solicitar 5 veces
- `languages.append(item)` agrega al final
- `languages[0]` es el primero, `languages[-1]` es el último
- `len(languages)` da el tamaño

### 🎉 Motivación
¡Construyes colecciones dinámicamente! Las listas crecen según necesites. 📦

---

## 💻 o2.4.2: ✂️ Cortador de Listas (Slicing)

### 🎯 Problema
Extraer diferentes partes de una lista usando slicing.

### 📝 Descripción
Dada una lista de 10 números, tu programa debe extraer: los primeros 3, los últimos 3, y los elementos del medio (índice 3 al 6).

### ⚙️ Funcionalidades
- Definir lista de 10 números
- Extraer primeros 3 con `[0:3]`
- Extraer últimos 3 con `[-3:]`
- Extraer del medio con `[3:7]`
- Mostrar cada sublista

### 🧪 Casos de Prueba
1. numbers = [1,2,3,4,5,6,7,8,9,10] → first_3 = [1,2,3], last_3 = [8,9,10], middle = [4,5,6,7]
2. Verificar longitudes: len(first_3)=3, len(last_3)=3, len(middle)=4

### 💻 Código Base
```python
# List Slicer ✂️
print("✂️ Cortador de Listas")
print("=" * 24)

# Your code here 👇
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_3 = []
last_3 = []
middle = []

# Example output:
# Lista original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Primeros 3: [1, 2, 3]
# Últimos 3: [8, 9, 10]
# Del medio (3-6): [4, 5, 6, 7]

# Test cases:
print("=" * 24)
print(first_3 == [1, 2, 3] and last_3 == [8, 9, 10] and middle == [4, 5, 6, 7])
```

### 💡 Tips Útiles
- `lista[0:3]` obtiene índices 0, 1, 2
- `lista[-3:]` obtiene los últimos 3
- `lista[3:7]` obtiene índices 3, 4, 5, 6
- El índice final NO se incluye en el slice
- `lista[:]` copia toda la lista

### 🎉 Motivación
¡Extraes datos con precisión quirúrgica! El slicing es una característica súper poderosa de Python. ✨

---

## 💻 o2.4.3: 🔄 Ordenador y Reversor

### 🎯 Problema
Ordenar una lista de números de forma ascendente y descendente.

### 📝 Descripción
Tu programa debe tomar una lista desordenada, crear una copia ordenada ascendente con `.sort()` y otra descendente con `.reverse()`.

### ⚙️ Funcionalidades
- Definir lista desordenada
- Ordenar ascendente con `.sort()`
- Ordenar descendente con `.sort(reverse=True)`
- Mostrar original y ambas ordenadas

### 🧪 Casos de Prueba
1. original = [5, 2, 8, 1, 9] → ascending = [1, 2, 5, 8, 9], descending = [9, 8, 5, 2, 1]
2. original = [3, 3, 1, 2] → ascending = [1, 2, 3, 3]
3. Verificar que original no cambió

### 💻 Código Base
```python
# List Sorter 🔄
print("🔄 Ordenador de Listas")
print("=" * 26)

# Your code here 👇
original = [5, 2, 8, 1, 9]
ascending = []
descending = []

# Example output:
# Original: [5, 2, 8, 1, 9]
# Ascendente: [1, 2, 5, 8, 9]
# Descendente: [9, 8, 5, 2, 1]

# Test cases:
print("=" * 26)
print(ascending == [1, 2, 5, 8, 9] and descending == [9, 8, 5, 2, 1])
```

### 💡 Tips Útiles
- Copia con `ascending = original.copy()`
- `.sort()` modifica la lista original
- `.sort(reverse=True)` ordena descendente
- O usa `sorted(lista)` que NO modifica original
- Importante: crear copias para no perder datos

### 🎉 Motivación
¡Organizas datos automáticamente! El ordenamiento es fundamental en algoritmos y bases de datos. 📈

---

## 💻 o2.4.4: 🗑️ Eliminador de Duplicados

### 🎯 Problema
Eliminar elementos duplicados de una lista manteniendo solo valores únicos.

### 📝 Descripción
Tu programa debe tomar una lista con duplicados y crear una nueva lista con solo valores únicos, manteniendo el orden original.

### ⚙️ Funcionalidades
- Definir lista con duplicados
- Recorrer lista original
- Verificar si elemento ya existe en nueva lista
- Agregar solo si no existe
- Mostrar lista limpia

### 🧪 Casos de Prueba
1. original = [1, 2, 2, 3, 4, 3, 5] → unique = [1, 2, 3, 4, 5], count = 5
2. original = ["a", "b", "a", "c"] → unique = ["a", "b", "c"], count = 3
3. original = [1, 1, 1] → unique = [1], count = 1

### 💻 Código Base
```python
# Duplicate Remover 🗑️
print("🗑️ Eliminador de Duplicados")
print("=" * 31)

# Your code here 👇
original = [1, 2, 2, 3, 4, 3, 5]
unique = []
count = 0

# Example output:
# Original: [1, 2, 2, 3, 4, 3, 5]
# Sin duplicados: [1, 2, 3, 4, 5]
# Elementos únicos: 5

# Test cases:
print("=" * 31)
print(unique == [1, 2, 3, 4, 5] and count == 5)
```

### 💡 Tips Útiles
- Recorre con `for item in original:`
- Verifica con `if item not in unique:`
- Agrega con `unique.append(item)`
- Cuenta con `len(unique)`
- Alternativa avanzada: `list(set(original))` (pero pierde orden)

### 🎉 Motivación
¡Limpias datos como un profesional! La eliminación de duplicados es crucial en procesamiento de datos. 🧹

---

## 🎯 o2.4.P: 📚 Proyecto Integrador - Sistema de Gestión de Biblioteca

### 🏆 Descripción del Proyecto

Crea un sistema completo de biblioteca que gestione libros con múltiples operaciones.

### 📝 Requerimientos

Tu sistema debe tener un **menú interactivo** con estas opciones:

1. **Agregar Libro**
   - Solicitar título del libro
   - Agregar a la lista de libros
   - Confirmación de agregado

2. **Mostrar Todos los Libros**
   - Listar con enumerate (posición + título)
   - Mostrar cantidad total
   - Mensaje si está vacía

3. **Buscar Libro**
   - Solicitar título a buscar
   - Mostrar posición si existe
   - Mensaje si no se encuentra

4. **Eliminar Libro**
   - Solicitar título a eliminar
   - Remover de la lista con `.remove()`
   - Confirmación de eliminación

5. **Ordenar Libros**
   - Ordenar alfabéticamente
   - Mostrar lista ordenada

6. **Estadísticas**
   - Total de libros
   - Libro con título más largo
   - Libro con título más corto

7. **Salir**
   - Usar `break` para salir del menú

### 🧪 Casos de Prueba

1. Agregar 3 libros: "Python Básico", "Algoritmos", "Estructuras de Datos" →
   total = 3, longest = "Estructuras de Datos"

2. Buscar "Algoritmos" → found = True, position = 1

3. Eliminar "Python Básico" → total = 2

4. Ordenar → books[0] = "Algoritmos"

### 💻 Código Base

```python
# 📚 Library Management System
print("📚 SISTEMA DE GESTIÓN DE BIBLIOTECA")
print("=" * 40)

# Your code here 👇
books = []
total = 0
longest = ""
found = False
position = -1

# Example output:
# === MENÚ ===
# 1. Agregar libro
# 2. Mostrar libros
# 3. Buscar libro
# 4. Eliminar libro
# 5. Ordenar libros
# 6. Estadísticas
# 7. Salir
#
# Libros en biblioteca:
# 0: Algoritmos
# 1: Estructuras de Datos
